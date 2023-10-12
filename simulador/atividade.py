

class Atividade:
    def __init__(self, env, local_atividade, duracao, nome, taxa_erro, lista_atuadores_atividade={},
                 inicio_ocorrencia=None, fim_ocorrencia=None):
        self.env = env
        self.local_atividade = local_atividade
        self.duracao = duracao
        self.nome = nome
        self.taxa_erro = taxa_erro
        self.lista_atuadores_atividade = lista_atuadores_atividade
        self.inicio_ocorrencia = inicio_ocorrencia
        self.fim_ocorrencia = fim_ocorrencia
        self.variacao = 0

    def executar(self, usuario_action, local_atividade):
        tempo = self.duracao + self.variacao
        yield self.env.process(
            local_atividade.entrar(tempo, usuario_action, self.lista_atuadores_atividade, local_atividade))

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.nome

    def __eq__(self, other):
        return self.nome == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.nome)
