from simulador.usuario import Usuario


class UsuariosHelp:
    usuarios = []

    def __init__(self, usuarios):
        __class__.usuarios = usuarios

    @staticmethod
    def name_usuarios_in_home() -> list[str]:
        return [usuario.nome for usuario in __class__.usuarios if usuario.comodo_atual != "RUA"]

    @staticmethod
    def name_usuarios_in_comodo(nome_comodo: str) -> list[str]:
        return [usuario.nome for usuario in __class__.usuarios if usuario.comodo_atual == nome_comodo]

    @staticmethod
    def usuarios_in_comodo(nome_comodo: str) -> list[Usuario]:
        return [usuario for usuario in __class__.usuarios if usuario.comodo_atual == nome_comodo]
