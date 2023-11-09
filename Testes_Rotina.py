import json
from datetime import timedelta

def calcula_horario_atividade(rotina, atividades):
    horario = timedelta(0)

    for u in rotina:
       horario += timedelta(minutes=atividades[u.capitalize()]["duracao"])
    return horario


with open('./rotinas/Grafo_casa-ROTINA_TRABALHO_PRESENCIAL(2usuarios).json') as json_file:
    dados = json.load(json_file)
    rotina_dia = ["ACORDAR_QUARTO_01", "USAR_BANHEIRO_02", "CAFE_DA_MANHA", "TOMAR_BANHO_BANHEIRO_02", "USAR_BANHEIRO_02", "BEBER_AGUA", "TRABALHAR_FORA", "TOMAR_BANHO_BANHEIRO_02", "JANTAR", "ASSISTIR_TV_30_MINUTOS", "BEBER_AGUA", "CAGA_BANHEIRO_02", "ASSISTIR_TV_90_MINUTOS", "ESCOVAR_DENTES_BANHEIRO_02", "TOMAR_BANHO_BANHEIRO_02","DORMIR_QUARTO_01"]
    horario = calcula_horario_atividade(rotina_dia, dados['ATIVIDADES'])

    print(horario)

