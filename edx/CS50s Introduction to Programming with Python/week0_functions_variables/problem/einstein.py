"""
@ author Ubiratan da SIlva Tavares
"""

def energy(mass):
    """
    mass: massa
    """
    constant_c = 300000000
    return mass * constant_c**2

def main():
    """
    funcao principal
    """
    mass = int(input(""))
    energia = energy(mass)
    print(energia)

main()
