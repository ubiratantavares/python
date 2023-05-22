"""
teste de uso da classe Conta
"""

from conta import Conta
from clientepf import ClientePF
from clientepj import ClientePJ

cliente1 = ClientePF("Ana", "Rua Um", "XXX.XXX.XXX-XX", "1995-05-20")
conta1 = Conta(1111, cliente1)

cliente2 = ClientePJ('Loja X', 'Praça Central', "XX.XXX.XXX/YYYY-ZZ")
conta2 = Conta(2222, cliente2)

conta2.depositar(500)

conta1.imprime()
print("\n")
conta2.imprime()
print("\n")

if conta2.sacar(1000):
    print("Saque realizado com sucesso.")
else:
    print("Não há saldo suficiente para o saque.")
print("\n")

if conta2.transferir(conta1, 200.0):
    print("Transferência de valor realizado com sucesso.")
else:
    print("Não há saldo suficiente para transferência.")
print("\n")

conta1.imprime()
print("\n")
conta2.imprime()
print("\n")

print('Contas criadas: ', Conta.quantidade())
