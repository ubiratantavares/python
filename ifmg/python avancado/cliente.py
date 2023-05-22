"""
@auhor Ubiratan
"""

class Cliente:
    """
    esta classe modela um cliente
    """
    def __init__(self, nome, endereco):
        self.__nome = nome
        self.__endereco = endereco

    @property
    def nome(self):
        """
        getNome
        """
        return self.__nome

    @nome.setter
    def nome(self, nome):
        """
        setNome
        """
        self.__nome = nome

    @property
    def endereco(self):
        """
        getEndereco
        """
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        """
        setEndereco
        """
        self.endereco = endereco

    def imprime(self):
        """
        este método imprime os atrinbutos de um cliente
        """
        print("Cliente: ", self.__nome, '\nEndereco: ', self.__endereco)
