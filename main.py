import json
import simpy
import os

from simulador.helps.gravar_dados import GravarDados
from simulador.helps.converter import Converter
from simulador.helps.tempo import Tempo
from simulador.helps.usuarios_help import UsuariosHelp
from simulador.montador import Montador



print('*************************************************')
modelo_dados = int(input('1- Completo \n2- Simples \nSelecione o tipo: '))

if not(modelo_dados == 1 or modelo_dados == 2):
     raise Exception('entrada inálida. Valores esparados são 1 ou 2')

print('*************************************************')
dias_simulacao = int(input('Quantidade de dias: '))
rotinas = [r.split('.')[0] for r in os.listdir('./rotinas/')]
dict_rotina = dict(zip(range(1, len(rotinas)+1), rotinas))
print('*************************************************')
for i in dict_rotina.keys():
    print(f'({i}) - {dict_rotina[i]}')
    
cod_rotina = int(input('Digite o código da rotina: '))
print('*************************************************')
arquivo_rotina = f'./rotinas/{dict_rotina[cod_rotina]}.json'



def inicia_simulacao(env, dias_simulados):
    data = Tempo.data_inicio_simulacao(dias_simulados)
    print(f'data inicio simulação: {data}')
    env.run(until=Converter.dias_para_segundos(dias_simulados))
    print(f'data final simulação: {Tempo.data_atual_simulacao(env)}')


with open(arquivo_rotina) as json_file:
    ############################### INSTANCIA ELEMENTOS ###############################
    dados = json.load(json_file)

    env = simpy.Environment()
    montador = Montador()
    comodos_da_casa = montador.monta_comodo(env, dados["COMODOS"], modelo_dados)
    grafo_comodos = montador.cria_grafo(dados["GRAFO_COMODOS"], comodos_da_casa)
    atividades = montador.monta_atividade(env, comodos_da_casa, dados["ATIVIDADES"])
    usuarios = montador.monta_usuario(env, dados["USUARIOS"])
    automacao = montador.monta_automacao(env, comodos_da_casa, dados["AUTOMACAO"])
    # nx.draw(grafo_comodos, with_labels=True)
    montador.relaciona_atividades_e_usuario(atividades, usuarios)
    montador.inicializa_processos(env, usuarios, grafo_comodos, automacao)

    ############################### INICIA APLICAÇÃO ###############################
    UsuariosHelp(usuarios)
    inicia_simulacao(env, dias_simulacao)
    GravarDados.gravar("./dados")

