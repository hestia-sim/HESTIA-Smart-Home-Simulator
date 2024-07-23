import math
from datetime import datetime
from random import uniform

import networkx as nx

from simulador.helps.tempo import Tempo


class Usuario:

    def __init__(self, env, nome, prioridade, comodo_atual, preferencia, rotina_semana=[]):
        self.env = env
        self.nome = nome
        self.prioridade = prioridade
        self.comodo_atual = comodo_atual
        self.rotina_semana = rotina_semana
        self.preferencia = preferencia
        self.contador_evento = None
        self.semana_anterior = None
        self.atividade_atual = None

    def gerar_evento(self, grafo_casa):
        while True:
            self.contador_index_evento()
            atividade = self._define_periodo_atividade()
            self.atividade_atual = atividade

            if self.comodo_atual != atividade.local_atividade.nome:
                self.comodo_atual.desativa_sensor(self)
            yield self.env.process(self.rota_ate(grafo_casa, self.comodo_atual, atividade.local_atividade.nome))
            self.comodo_atual = atividade.local_atividade
            # self.comodo_atual.ativa_sensor(self)
            yield self.env.process(atividade.executar(self, atividade.local_atividade))

    def _define_periodo_atividade(self):
        atividade = self.rotina_semana[Tempo.dia_da_semana(self.env)][self.contador_evento]

        # ferifica a o tempo restante do dia e atribui para a ultima atividade
        if atividade == self.rotina_semana[Tempo.dia_da_semana(self.env)][-1]:
            t = self.env.now
            atividade.duracao = 86400 - (self.env.now % 86400)
            return atividade
        # realiza a variação do tempo de cada atividade
        if atividade.inicio_ocorrencia is not None and atividade.fim_ocorrencia is not None:
            atividade.duracao = (datetime.strptime(atividade.fim_ocorrencia, "%H:%M:%S") - datetime.strptime(
                atividade.inicio_ocorrencia, "%H:%M:%S")).total_seconds()
            atividade.variacao = int(uniform(0, atividade.duracao * atividade.taxa_erro))
            # atividade.duracao = periodo_atividade_variavel
            return atividade

        atividade.variacao = int(uniform(0, atividade.duracao * atividade.taxa_erro))
        return atividade

    def proxima_atividade(self):
        atividade = self.rotina_semana[Tempo.dia_da_semana(self.env)][self.contador_evento]

    def contador_index_evento(self):
        semana_atual = Tempo.dia_da_semana(self.env)
        tr = len(self.rotina_semana[Tempo.dia_da_semana(self.env)]) - 1
        if self.contador_evento is None:
            self.contador_evento = 0
            self.semana_anterior = Tempo.dia_da_semana(self.env)
        elif self.contador_evento >= tr or semana_atual != self.semana_anterior:
            self.contador_evento = 0
        else:
            self.contador_evento += 1
        self.semana_anterior = Tempo.dia_da_semana(self.env)

    # RETORNA A ROTA MAIS CURTA DE UM PONTO ATÉ O OUTO COMODO
    def rota_ate(self, grafo, localAtual, objetivo):
        caminho = nx.astar_path(grafo, source=localAtual, target=objetivo)[1:]
        for i in caminho:
            if i.nome != objetivo:
                self.comodo_atual = i
                yield self.env.process(i.passar(self))
