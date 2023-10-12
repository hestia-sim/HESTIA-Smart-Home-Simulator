from datetime import timedelta

import simpy

from simulador.helps.status import Status
from simulador.helps.tempo import Tempo
from simulador.helps.usuarios_help import UsuariosHelp
from simulador.usuario import Usuario


class Comodo:
    def __init__(self, env, nome, ocupacao_maxima, atuadores=[]):
        self.env = env
        self.resource = simpy.Resource(env, capacity=ocupacao_maxima)
        self.atuadores = atuadores
        self.nome = nome

    def add_atuador(self, atuador):
        self.atuadores.append(atuador)

    def entrar(self, duracao, usuario_action, lista_atuadores_atividade, local_atividade):
        with self.resource.request() as rq:
            yield rq
            usuario_action.comodo_atual = local_atividade
            self._ativa_sensor(usuario_action, rq)

            yield from self.inicia_atuadores(lista_atuadores_atividade, usuario_action)
            yield self.env.timeout(duracao)
            yield from self.finaliza_atuadores(lista_atuadores_atividade, usuario_action)

            self._desativa_sensor(usuario_action, rq)

    def usuario_prioritario(self) -> Usuario:
        lista_usuarios_no_comodo = UsuariosHelp.usuarios_in_comodo(self.nome)

        usuario_prioritario = None
        for usuario in lista_usuarios_no_comodo:
            if usuario_prioritario is None or usuario.prioridade > usuario_prioritario.prioridade:
                usuario_prioritario = usuario
        return usuario_prioritario

    def finaliza_atuadores(self, lista_atuadores_atividade, usuario_action):
        if lista_atuadores_atividade is None:
            return

        for tipo_atuador in lista_atuadores_atividade:
            if tipo_atuador in self.atuadores:
                atuador = self.atuadores[self.atuadores.index(tipo_atuador)]
                if not atuador.is_ligado():
                    continue

                usuarios_comodo = UsuariosHelp.usuarios_in_comodo(self.nome)
                desativa = True
                if len(usuarios_comodo) > 1:
                    for u in usuarios_comodo:
                        if u == usuario_action:
                            continue
                        if u.atividade_atual.lista_atuadores_atividade[tipo_atuador] == Status.ON:
                            desativa = False

                if desativa:
                    with atuador.resource.request() as rq3:
                        yield rq3
                        yield self.env.timeout(5)
                        atuador.finalizar_uso(usuario_action)

    def inicia_atuadores(self, lista_atuadores_atividade, usuario_action: Usuario):
        if lista_atuadores_atividade is None:
            return

        for tipo_atuador, valor in lista_atuadores_atividade.items():
            horario_utilizacao_lampada = timedelta(hours=17, minutes=30)
            horario_atual = Tempo.hora_atual_simulacao(self.env)
            if tipo_atuador == "LAMPADA" and horario_atual < horario_utilizacao_lampada:
                continue

            if tipo_atuador in self.atuadores:
                atuador_atual = self.atuadores[self.atuadores.index(tipo_atuador)]


                usuarios_comodo = UsuariosHelp.usuarios_in_comodo(self.nome)
                usuario_prioritario = self.usuario_prioritario()
                if len(usuarios_comodo) > 1 or usuario_prioritario == usuario_action:
                    if self.nome in usuario_action.preferencia:
                        prederencia_comodo = usuario_action.preferencia[self.nome]
                        if atuador_atual.tipo in prederencia_comodo:
                            with atuador_atual.resource.request() as rq2:
                                yield rq2
                                yield self.env.timeout(5)
                                atuador_atual.mudar(usuario_action, **prederencia_comodo[atuador_atual.tipo])
                        else:
                            if atuador_atual.status() != valor:
                                yield from self.inicio_simples(atuador_atual, usuario_action)
                    else:
                        if atuador_atual.status() != valor:
                            yield from self.inicio_simples(atuador_atual, usuario_action)
                else:
                    if atuador_atual.status() != valor:
                        yield from self.inicio_simples(atuador_atual, usuario_action)

    def inicio_simples(self, atuador_atual, usuario_action):
        with atuador_atual.resource.request() as rq2:
            yield rq2
            yield self.env.timeout(5)
            atuador_atual.iniciar_uso(usuario_action)

    def passar(self, usuario: Usuario):
        with self.resource.request() as rq:
            yield rq
            self._ativa_sensor(usuario, rq)
            yield self.env.timeout(20)
            self._desativa_sensor(usuario, rq)

    def _ativa_sensor(self, usuario_action, rq):
        if rq.resource.count > 1 or self.nome == "RUA":
            return

        if "SENSOR_PRESENCA" in self.atuadores:
            atuador_atual = self.atuadores[self.atuadores.index("SENSOR_PRESENCA")]
            atuador_atual.iniciar_uso(usuario_action)

    def _desativa_sensor(self, usuario_action, rq):
        if rq.resource.count > 1 or self.nome == "RUA":
            return

        if "SENSOR_PRESENCA" in self.atuadores:
            atuador_atual = self.atuadores[self.atuadores.index("SENSOR_PRESENCA")]
            atuador_atual.finalizar_uso(usuario_action)

    def __str__(self) -> str:
        return self.nome

    def __repr__(self):
        return self.nome

    def __eq__(self, other):
        return self.nome == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.nome)
