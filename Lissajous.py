# Universidad del Valle de Guatemala
# Fisica 3 - Proyecto 1
# Integrantes: Alejandro Gómez 20347 y Paola de León 20361
# Fecha de creacion: 28/09/2021
# Ultima modificacion 30/09/2021
# Modulo: Pantalla lateral

import numpy as np
import math
import matplotlib.pyplot as plt

RangoPi = linspace(0.0,2*pi,300)

def CurvasLissajous(Lado1, DeltaX, XPosition, YPosition):
    
    if XPosition == 0:
        PosicionX = sin(Lado1*RangoPi+DeltaX)
    else:
        PosicionX = XPosition*sin(Lado1*RangoPi*DeltaX)

    if YPosition == 0:
        PosicionY = sin(Lado1*RangoPi+DeltaX)
    else:
        PosicionY = YPosition*sin(Lado1*RangoPi*DeltaX)
    
    plt.title("Pantalla")
    plot(XPosition, YPosition)