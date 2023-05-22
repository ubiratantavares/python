#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jan 06 2021

@author: kon
"""

class Poligono:
    """
    esta é a classe Polígono
    """
    def __init__(self, numero_de_lados):
        self.numero = numero_de_lados
        self.lados = [0 for i in range(numero_de_lados)]

    def le_lados(self):
        """
        este método lê valores dos lados de um poligono.
        """
        self.lados = [float(input("Digite tamanho do lado " + str(i+1) + ": "))
                      for i in range(self.numero)]

    def mostra_lados(self):
        """
        este método mostra os valores dos lados de um polígono.
        """
        for i in range(self.numero):
            print("Lado", i+1, "tem comprimento", self.lados[i])


class Triangulo(Poligono):
    """
    esta é o modelo da classe Triangulo.
    """
    def __init__(self):
        Poligono.__init__(self, 3)

    def area(self):
        """
        este método calcula a área de um triângulo.
        """
        lado1, lado2, lado3 = self.lados
        # calcula o semi-perímetro
        semiperimetro = (lado1 + lado2 + lado3) / 2
        area = (semiperimetro*(semiperimetro - lado1) * \
                (semiperimetro - lado2) * (semiperimetro - lado3)) ** 0.5
        print(f'A área do triângulo é {area:0.2f}')


class Retangulo(Poligono):
    """
    este é o modelo da classe Retângulo.
    """
    def __init__(self):
        Poligono.__init__(self, 4)

    def le_lados(self):
        """
        este método sobreescreve o método da classe Polígono.
        """
        lado1 = float(input("Digite tamanho do lado 1: "))
        lado2 = float(input("Digite tamanho do lado 2: "))
        self.lados[0] = self.lados[2] = lado1
        self.lados[1] = self.lados[3] = lado2

    def area(self):
        """
        este método calcula a área de um retângulo.
        """
        return self.lados[0] * self.lados[1]

    def diagonal(self):
        """
        este método calcula a diagonal do retângulo
        """
        return (self.lados[0] ** 2 + self.lados[1] ** 2) ** 0.5


class TrianguloRetangulo(Triangulo):
    """
    este é o modelo da classe TrianguloRetangulo.
    """
    def eh_triangulo_retangulo(self):
        """
        este método verifica se o traingulo é retângulo.
        """
        return(self.lados[0]**2 == self.lados[1]**2 + self.lados[2]**2
               or self.lados[1]**2 == self.lados[0]**2 + self.lados[2]**2
               or self.lados[2]**2 == self.lados[0]**2 + self.lados[1]**2)
