# Universidad del Valle de Guatemala
# Fisica 3 - Proyecto 1
# Integrantes: Alejandro Gómez 20347 y Paola de León 20361
# Fecha de creacion: 28/09/2021
# Ultima modificacion 30/09/2021
# Modulo: Pantalla principal

import math
import numpy as np
from math import sin
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot

"""
En esta funcion se realizan los calculos pertinentes
a la obtencion de valores fisicos para fines de
la simulacion.
"""

pi = 3.14159

def OperacionesFisicas(CargaParticula, MasaParticula, distanciaP1, distanciaP2, deltaX, voltajeP1, voltajeP2):

    # Operaciones matematicas de electron para placa 1
    VelocidadX = (((2*CargaParticula*1000)/MasaParticula)**(1/2))
    deltaT = deltaX/VelocidadX
    aceleracionY = (CargaParticula*voltajeP1)/(MasaParticula*distanciaP1)
    deltaY = (aceleracionY/2)*(deltaT**2)
    CalculoAngulo = math.degrees(math.atan(deltaY/0.02))

    # Operaciones matematicas de electron para placa 2
    VelocidadX2 = (((2*CargaParticula*1000)/MasaParticula)**(1/2))
    deltaT2 = deltaX/VelocidadX2
    aceleracionY2 = (CargaParticula*voltajeP2)/(MasaParticula*distanciaP2)
    deltaY2 = (aceleracionY2/2)*(deltaT2**2)
    CalculoAngulo2 = math.degrees(math.atan(deltaY2/deltaX))

    LadoOpuesto1 = 0.03 * (math.degrees(math.atan(CalculoAngulo)))
    LadoOpuesto2 = 0.03 * (math.degrees(math.atan(CalculoAngulo2)))

    x = LadoOpuesto1
    y = LadoOpuesto2

    # plt.plot([0,0],[x,y], "ro")
    plt.subplot(3,1,1)
    plt.plot(x, y, "ro")
    plt.ylabel("Desplazamiento en y")
    plt.xlabel("Desplazamiento en x")
    plt.title("Comportamiento en pantalla de un Tubo\nde Rayos Catodicos:")

    # VISTA LATERAL
    # Crear lista con valores de X
    xColLateral = np.arange(0,0.031, 0.001)
    # Crear lista con valores de Y
    yColLateral = []
    for i in range(31):
        xValue = xColLateral[i]
        xValue = round(xValue, 3)
        y = (1/2*aceleracionY*((xValue/VelocidadX)**2))
        yColLateral.append(y)
    
    #Posicion de la grafica
    plt.subplot(3,1,2)
    plt.title("Comportamiento lateral de un Tubo\nde Rayos Catodicos:")
    plt.ylabel("Desplazamiento en y")
    plt.xlabel("Desplazamiento en x")
    #plt.ylim(-0.03,0.03)
    plt.scatter(xColLateral,yColLateral)

    # VISTA ARRIBA
    # Crear lista con valores de X
    xColArriba = np.arange(0,0.031, 0.001)
    # Crear lista con valores de Y
    yColArriba = []
    for i in range(31):
        xValue = xColArriba[i]
        xValue = round(xValue, 3)
        y = (1/2*aceleracionY2*((xValue/VelocidadX2)**2))
        yColArriba.append(y)
    
    #Posicion de la grafica
    plt.subplot(3,1,3)
    plt.title("Comportamiento arriba de un Tubo\nde Rayos Catodicos:")
    plt.ylabel("Desplazamiento en y")
    plt.xlabel("Desplazamiento en x")
    #plt.ylim(-0.03,0.03)
    plt.scatter(xColArriba,yColArriba)

    plt.tight_layout()

    plt.show()
