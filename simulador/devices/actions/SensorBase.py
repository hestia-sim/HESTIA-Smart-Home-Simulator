from abc import ABC

from simulador.devices.actions.DeviceBase import DeviceBase


class SensorBase(DeviceBase, ABC):
    def __init__(self, env, nome_comodo, tipo, modelo_dados: int, tipoEnv):
        super().__init__(env, nome_comodo, tipo, modelo_dados, tipoEnv)
