import json
from datetime import timedelta

def calcula_horario_atividade(rotina, atividades):
    horario = timedelta(0)

    for u in rotina:
       horario += timedelta(minutes=atividades[u.capitalize()]["duracao"])
    return horario


with open('./rotinas/Grafo_casa-ROTINA_ARTIGO(2usuarios_bemDefinido_semvariacao_02).json') as json_file:
    dados = json.load(json_file)
    rotina_dia = ["ACORDAR_QUARTO_01", "CAFE_DA_MANHA", "USAR_BANHEIRO_01", "FAZER_NADA"]
    # ["ACORDAR_QUARTO_01", "ESCOVAR_DENTES_BANHEIRO_02", "TRABALHAR_FORA", "PASSEAR_30_MINUTOS", "PASSEAR_30_MINUTOS", "ASSISTIR_TV_120_MINUTOS", "JANTAR", "ASSISTIR_TV_120_MINUTOS", "TOMAR_BANHO_BANHEIRO_02","DORMIR_QUARTO_01"]

    
    horario = calcula_horario_atividade(rotina_dia, dados['ATIVIDADES'])

    print(horario)

