from datetime import datetime

import pandas as pd

from simulador.helps.usuarios_help import UsuariosHelp


class GravarDados:
    contador_eventos = 0
    contador_arquivos = 0
    dataFrame = pd.DataFrame(columns=['device', 'devId', 'productKey', 'message', 'sensorType', 'group', 'userAction', 'activityUserAction', 'timeStamp', 'space'])
    @staticmethod
    def envia_dados(device, devId, productKey, status, tipo, nome_usuario, atividade,  hora_ativacao, comodo):
        # print(f"'device': {device}, 'message': {status}, 'sensorType': {tipo}, 'group': {UsuariosHelp.name_usuarios_in_home()}, 'userAction': {nome_usuario}, 'activityUserAction': {atividade}, 'timeStamp': {hora_ativacao}, 'space': {comodo}")

        __class__.dataFrame.loc[__class__.contador_eventos] = [device, devId, productKey, status, tipo, UsuariosHelp.name_usuarios_in_home(), nome_usuario, atividade, hora_ativacao, comodo]
        __class__.contador_eventos = __class__.contador_eventos + 1

    @staticmethod
    def gravar(caminho_pasta: str):
        __class__.dataFrame.to_csv(f"{caminho_pasta}/dados-{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.csv", index=False)

