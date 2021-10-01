# Universidad del Valle de Guatemala
# Fisica 3 - Proyecto 1
# Integrantes: Alejandro Gómez 20347 y Paola de León 20361
# Fecha de creacion: 28/09/2021
# Ultima modificacion 30/09/2021
# Modulo: Pantalla principal

import numpy as np
import math
import matplotlib.pyplot as plt

"""
En esta funcion se realizan los calculos pertinentes
a la obtencion de valores fisicos para fines de
la simulacion.
"""


def OperacionesFisicas(CargaParticula, voltajeP1, MasaParticula, distanciaP1, VoltajeAceleracionElectron, distanciaP2, deltaX):

    # Operaciones matematicas de electron para placa 1
    VelocidadX = (((2*CargaParticula*1000)/MasaParticula)**(1/2))
    deltaT = deltaX/VelocidadX
    aceleracionY = (CargaParticula*voltajeP1)/(MasaParticula*distanciaP1)
    deltaY = (aceleracionY/2)*(deltaT**2)
    CalculoAngulo = math.degrees(math.atan(deltaY/0.02))

    # Operaciones matematicas de electron para placa 2
    VelocidadX2 = (((2*CargaParticula*1000)/MasaParticula)**(1/2))
    deltaT2 = deltaX/VelocidadX2
    aceleracionY2 = (CargaParticula*voltajeP1)/(MasaParticula*distanciaP2)
    deltaY2 = (aceleracionY2/2)*(deltaT2**2)
    CalculoAngulo2 = math.degrees(math.atan(deltaY2/deltaX))

    LadoOpuesto1 = 0.03 * (math.degrees(math.atan(CalculoAngulo)))
    LadoOpuesto2 = 0.03 * (math.degrees(math.atan(CalculoAngulo2)))
    
    # Imprimir L
    print ("L1 = " , LadoOpuesto1)
    print ("L2 = " , LadoOpuesto2)

    x = LadoOpuesto1
    y = LadoOpuesto2

    plt.plot([0,0],[x,y], "ro")
    plt.title("Comportamiento de un Tubo\nde Rayos Catodicos:")
    plt.ylabel("Desplazamiento en y")
    plt.xlabel("Desplazamiento en x")
    plt.show()

"""
La presente funcion se encarga de mostrar
el grafico para la vista principal del
simulador.

"""
def VistaPrincipal (ValorEnx, ValorEny):
    ValoresSinosoidales = linspace(-pi, pi, 100)
    plt.title("Vista principal")
    plt.plot(ValorEnx, ValorEny)
    plt.show
