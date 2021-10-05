# Universidad del Valle de Guatemala
# Fisica 3 - Proyecto 1
# Integrantes: Alejandro Gómez 20347 y Paola de León 20361
# Fecha de creacion: 28/09/2021
# Ultima modificacion 5/10/2021
# Modulo: Pantalla - Curvas Lissajous

import numpy as np
import math
import matplotlib.pyplot as plt
from math import sin
from matplotlib.pyplot import plot
from numpy import linspace
from matplotlib.animation import FuncAnimation

RangoPi = linspace(0.0,2*3.141592653589793,300)

# Definicion de limites de los ejes
XLimiteIzq = -1.5
XLimiteDer = 1.5
YLimiteAbajo = -1.5
YLimiteArriba = 1.5

"""

Para el desarrollo de la vista de curvas lissajous, se modificó
el código realizado para una práctica de laboratorio previa.
Para animar la gráfica, se basó en el tutorial de:
https://www.youtube.com/watch?v=aNuOq3vMw50&ab_channel=cctmexico

"""

def CurvasLissajous(Alfa, Beta, Delta):
    
    CambioDelta = Delta*3.141592653589793
    fig, ax = plt.subplots()

    listaPosicionX, listaPosicionY = [], []
    Grafico, = plt.plot([], [], 'ro')

    """Se define una función para inicializar la gráfica"""
    def GraficoIniciado():
        ax.set_xlim(XLimiteIzq, XLimiteDer)
        ax.set_ylim(YLimiteAbajo, YLimiteArriba)
        return Grafico,

    def ActualizacionDelGrafico(frame):

        # Se agregan los valores correspondientes al eje X
        listaPosicionX.append(np.sin((Alfa*frame) + Delta))

        # Se agregan los valores correspondientes al eje Y
        listaPosicionY.append(np.sin(Beta*frame))

        Grafico.set_data(listaPosicionX, listaPosicionY)

        #Color del grafico
        Grafico.set_color("blue")

        return Grafico,

    ani = FuncAnimation(fig, ActualizacionDelGrafico, frames=np.linspace(2, 20, 650), init_func=GraficoIniciado, blit=True, interval = 7)

    plt.clf()
    
    plt.title("Curvas Lissajous")

    #Posicion del grafico
    #plt.subplot(1,1,2)

    plot(listaPosicionX, listaPosicionY)
    plt.show()

"""
A continuacion se definen numeros de prueba para asegurarse que todas las curvas de Lissajous funcionen
USAR DE REFERENCIA LA TABLA INCLUIDA EN LA GUIA

Descomentar la que se quiera probar
"""

# Curvas 1:1 :

CurvasLissajous(1,1,0)
CurvasLissajous(1,1,0.25)
#CurvasLissajous(1,1,0.5)
#CurvasLissajous(1,1,0.75)
#CurvasLissajous(1,1,1)

#Curvas 1:2 :

#CurvasLissajous(1,2,0.5)
CurvasLissajous(1,2,0.25)
#CurvasLissajous(1,2,0.5)
#CurvasLissajous(1,2,0.75)
#CurvasLissajous(1,2,1)

#Curvas 1:3 :

#CurvasLissajous(1,3,0.5)
CurvasLissajous(1,3,0.25)
CurvasLissajous(1,3,0.5)
CurvasLissajous(1,3,0.75)
#CurvasLissajous(1,3,1)

#Curvas 2:3 :

CurvasLissajous(2,3,0.5)
#CurvasLissajous(2,3,0.25)
#CurvasLissajous(2,3,0.5)
CurvasLissajous(2,3,0.75)
#CurvasLissajous(2,3,1)