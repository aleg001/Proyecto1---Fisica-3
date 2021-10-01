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
def OperacionesFisicas (CargaParticula, voltajeP1, MasaParticula, distanciaP1, VoltajeAceleracionElectron, distanciaP2, deltaX):
    
    # Operaciones matematicas de Electron
    VelocidadX = ((2*CargaParticula*VoltajeAceleracionElectron)/MasaParticula)pow(2)
    deltaT = deltaX/VelocidadX
    aceleracionY= (CargaParticula*voltajeP1)/(MasaParticula*distanciaP1)
    deltaY = aceleracion

    # Crear listas para primera pareja de placas
    xCol1 = np.arange(0,0.031, 0.001)
    yCol1 = []

    # Calculos para variable y
    for i in range(31):
        xValue = xCol1[i]
        xValue = round(xValue, 3)
        y = ((CargaParticula*VoltajeAceleracionElectron)/(2*MasaParticula*distanciaP1))*((xValue/VelocidadX)**2)
        yCol1.append(y)

    # Crear listas para primera pareja de placas
    xCol2 = np.arange(0,0.031, 0.001)
    yCol2 = []

    # Calculos para variable y
    for i in range(31):
        xValue = xCol2[i]
        xValue = round(xValue, 3)
        y = ((CargaParticula*VoltajeAceleracionElectron)/(2*MasaParticula*distanciaP2))*((xValue/VoElectron)**2)
        yCol2.append(y)

    # Indica si la partícula se mueve para arriba o para abajo
    plt.scatter(xCol1,yCol1)
    plt.title("MOVIMIENTO DE UNA PARTICULA CARGADADA\nEN PRESENCIA DE UN POTENCIAL")
    plt.ylabel("Desplazamiento en y")
    plt.xlabel("Desplazamiento en x")
    plt.ylim(-0.03,0.03)
    plt.show()
    
    # Indica si la partícula se mueve para la derecha o para la izquierda
    plt.scatter(xCol2,yCol2)
    plt.title("MOVIMIENTO DE UNA PARTICULA CARGADADA\nEN PRESENCIA DE UN POTENCIAL")
    plt.ylabel("Desplazamiento en y")
    plt.xlabel("Desplazamiento en x")
    plt.ylim(-0.03,0.03)
    plt.show()

    # Calcular las distancia l
    DistanciaL1 = AnguloP1(xCol1[30], yCol1[30]) # Para arriba o abajo
    DistanciaL2 = AnguloP2(xCol2[30], yCol2[30]) # Para los lados



def AnguloP1(PosicionX, PosicionY):
    CalculoAngulo = math.degrees(math.atan(PosicionY/PosicionX))
    if (CalculoAngulo < 0):
        CalculoAngulo = 90 + CalculoAngulo

    print("Angulo Vertical: ",CalculoAngulo)
    VariableTemp = DistanciaL(CalculoAngulo, 0.8)
    return VariableTemp

def AnguloP2(PosicionX, PosicionY):
    CalculoAngulo = math.degrees(math.atan(PosicionY/PosicionX))
    if (CalculoAngulo < 0):
        CalculoAngulo = 90 + CalculoAngulo
    print("Angulo Horizontal: ",CalculoAngulo)
    return DistanciaL(CalculoAngulo, 0.8)

def DistanciaL(angulo, distancia):
    vTOA = (math.degrees(math.atan(angulo)))*distancia
    print("Distancia L:",vTOA)

"""
La presente funcion se encarga de mostrar
el grafico para la vista principal del
simulador.

"""
def VistaPrincipal(ValorEnx, ValorEny):
    ValoresSinosoidales = linspace(-pi,pi,100)
    plt.title("Vista principal")
    plt.plot(ValorEnx, ValorEny)
    plt.show

