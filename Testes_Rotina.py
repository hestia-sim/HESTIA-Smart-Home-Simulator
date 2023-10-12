import json
from datetime import timedelta

def calcula_horario_atividade(rotina, atividades):
    horario = timedelta(0)

    for u in rotina:
       horario += timedelta(minutes=atividades[u.capitalize()]["duracao"])
    return horario

with open('./rotinas/Grafo_teste-grupo(3usuarios).json') as json_file:
    dados = json.load(json_file)
    rotina_dia = ["CHEGAR","CHEGAR","CHEGAR","CHEGAR","CHEGAR","CHEGAR","CHEGAR","CHEGAR", "CHEGAR_30M", "ASSISTIR_TV_120_MINUTOS", "ASSISTIR_TV_30_MINUTOS", "SAIR_COMODO", "SAIR_COMODO", "SAIR_COMODO", "ASSISTIR_TV_120_MINUTOS", "ASSISTIR_TV_120_MINUTOS", "SAIR_COMODO", "ASSISTIR_TV_120_MINUTOS", "ASSISTIR_TV_30_MINUTOS", "FIM_ROTINA"]




    horario = calcula_horario_atividade(rotina_dia, dados['ATIVIDADES'])

    print(horario)



