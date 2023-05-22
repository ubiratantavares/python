"""
@auhor Ubiratan
"""

from cliente import Cliente

class ClientePF(Cliente):
    """
    esta classe modela um cliente pessoa física.
    """

    def __init__(self, nome, endereco, cpf, nascimento):
        super().__init__(nome, endereco)
        self.__cpf = cpf
        self.__nascimento = nascimento

    def imprime(self):
        """
        este método imprime os atrinbutos de um cliente PF
        """
        print(f"Cliente: {self.nome}\nCPF:{self.__cpf}\nNascimento: {self.__nascimento}")
