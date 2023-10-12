import hashlib
from abc import ABC, abstractmethod

import simpy

from simulador.helps.status import Status
from simulador.usuario import Usuario


class DeviceBase(ABC):
    _contador_instancias = 0

    def __init__(self, env, nome_comodo, tipo, modelo_dados: int, tipoEnv: str):
        __class__._contador_instancias += 1
        self.modelo_dados = modelo_dados
        self.env = env
        self.resource = simpy.Resource(env)
        self.tipo = tipo
        self.tipoEnv = tipoEnv
        self.device = f'{nome_comodo}_{tipo}-{__class__._contador_instancias:03}'
        self.devId = f"disp{hashlib.md5(self.device.encode()).hexdigest()}"
        self.nome_comodo = nome_comodo

    def __str__(self) -> str:
        return self.device

    def __repr__(self) -> str:
        return self.device

    def __eq__(self, other) -> bool:
        return self.tipo == other

    def __ne__(self, other) -> bool:
        return not self.__eq__()

    def __hash__(self) -> int:
        return hash(self.device)

    def iniciar_uso(self, usuario_action: Usuario) -> None:
        self._ligar()
        self._mensagem(usuario_action)

    def finalizar_uso(self, usuario_action: Usuario) -> None:
        self._desligar()
        self._mensagem(usuario_action)

    @abstractmethod
    def is_ligado(self) -> bool:
        pass

    @abstractmethod
    def _ligar(self) -> None:
        pass

    @abstractmethod
    def _desligar(self) -> None:
        pass

    @abstractmethod
    def _mensagem(self, usuario: Usuario) -> None:
        pass

    @abstractmethod
    def status(self) -> str:
        pass

    @abstractmethod
    def mudar(self, **kwargs):
        pass
