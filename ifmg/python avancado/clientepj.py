"""
@auhor Ubiratan
"""

from cliente import Cliente

class ClientePJ(Cliente):
    """
    esta classe modela um cliente pessoa jurídica
    """
    def __init__(self, nome, endereco, cnpj):
        super().__init__(nome, endereco)
        self.__cnpj = cnpj

    def imprime(self):
        """
        este método imprime os atrinbutos de um cliente PF
        """
        print(f"Cliente: {self.nome}\nCNPJ: {self.__cnpj}")
