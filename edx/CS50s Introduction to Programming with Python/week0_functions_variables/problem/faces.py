"""
@author Ubiratan da Silva Tavares
"""

entrada = input().strip().split()
saida = ""
for i, _ in enumerate(entrada):
    if entrada[i] == ':)':
        saida += '\U0001F642'
    elif entrada[i] == ':(':
        saida += '\U0001F641'
    else:
        saida += entrada[i]
    saida += " "
print(saida)
