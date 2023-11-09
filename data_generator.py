import json
import sys

import simpy
import os

from menu import menu
from simulador.helps.gravar_dados import GravarDados
from simulador.helps.converter import Converter
from simulador.helps.tempo import Tempo
from simulador.helps.usuarios_help import UsuariosHelp
from simulador.montador import Montador


def inicia_simulacao(env, dias_simulados):
    data = Tempo.data_inicio_simulacao(dias_simulados)
    print(f'data inicio simulação: {data}')
    env.run(until=Converter.dias_para_segundos(dias_simulados))
    print(f'data final simulação: {Tempo.data_atual_simulacao(env)}')


def generate_data():
    initial_path = './dados'

    tipos = ['completo', 'simples', 'back']
    max_size = max(len(option) for option in tipos)
    title = '*' * (max_size // 2) + ' SELECT THE TYPE ' + '*' * (max_size // 2)
    modelo_dados = menu(list(map(str.capitalize, tipos)), title)
    tipo_selecionado = tipos[modelo_dados]
    if tipo_selecionado != 'back':
        dias_simulacao = int(input('Quantidade de dias: '))

        rotinas = [r.split('.')[0] for r in os.listdir('./rotinas/')]
        max_size = max(len(option) for option in rotinas)
        title = '*' * (max_size // 2) + ' SELECT THE ROUTINE ' + '*' * (max_size // 2)
        rotina_selecionada = menu(rotinas, title)

        arquivo_rotina = f'./rotinas/{rotinas[rotina_selecionada]}.json'

        if not 'dados' in os.listdir():
            os.mkdir('dados')

        if not 'original' in os.listdir(initial_path):
            os.mkdir('/'.join([initial_path, 'original']))

        initial_path += '/original/'
        if not tipo_selecionado in os.listdir(initial_path):
            os.mkdir('/'.join([initial_path, tipo_selecionado]))
        initial_path += tipo_selecionado

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
            GravarDados.gravar(initial_path)
        return False
    else:
        sys.stdout.write('\r')
        return True
