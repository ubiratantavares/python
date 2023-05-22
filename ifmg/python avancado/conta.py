"""
@auhor Ubiratan
"""

class Conta:
    """
    esta classe modelo uma conta
    """
    _quantidade = 0

    def __init__(self, numero, cliente):
        self.adiciona_conta()
        self.__numero = numero
        self.__cliente = cliente
        self.__saldo = 0.0

    @property
    def saldo(self):
        """
        get Saldo
        """
        return self.__saldo
    @saldo.setter
    def saldo(self, valor):
        """
        set Saldo
        """
        self.__saldo = valor

    @classmethod
    def adiciona_conta(cls):
        """
        metodo da classe que adiciona uma unidade ao atributo de classe quantidade
        """
        cls._quantidade += 1

    @classmethod
    def quantidade(cls):
        """
        metodo de classe que retorna o atributo quantidade
        """
        return cls._quantidade

    def depositar(self, valor):
        """
        este método adiciona o valor no saldo
        """
        self.__saldo += valor

    def tem_saldo(self, valor):
        """
        este método verifica se existe saldo suficiente para saque de um valor
        """
        if self.__saldo >= valor:
            return True
        return False

    def sacar(self, valor):
        """
        este método realiza o saque de um valor
        """
        if self.tem_saldo(valor):
            self.__saldo -= valor
            return True
        return False

    def transferir(self, destino, valor):
        """
        este método realiza a transferencia do valor desta conta para outra conta.
        """
        if self.tem_saldo(valor):
            self.sacar(valor)
            destino.depositar(valor)
            return True
        return False
    def imprime(self):
        """
        este método imprime os atrinbutos de um cliente
        """
        print("Conta: ", str(self.__numero), '\nSaldo: ', str(self.__saldo))
        self.__cliente.imprime()

    def __str__(self):
        return f"Numero: {self.__numero}\nSaldo: {self.__saldo}\n"+ self.__cliente.imprime()


class ContaInvestimento(Conta):
    """
    classe filha da classe Conta
    """

    def depositar(self, valor):
        self.saldo += valor * 1.01
