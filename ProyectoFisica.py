# Universidad del Valle de Guatemala
# Fisica 3 - Proyecto 1
# Integrantes: Alejandro Gómez 20347 y Paola de León 20361
# Fecha de creacion: 28/09/2021
# Ultima modificacion 1/10/2021

# Llamado a librerias
import numpy as np
import math
import matplotlib.pyplot as plt
from time import sleep
import time as t
import sys

# Llamado a los modulos desarrollados
from PantallaPrincipal import *
from VistaLateral import *
from VistaArriba import *
from InterfazGrafica import *


# Variables Fisicas fijadas

""" 
Tamano Pantalla
Area Placas Deflexion
Distancia Entre Placas
Distancia desde placas verticales a horizontales """

CargaParticula = 1.6E-19
MasaParticula = 9.11E-31
distanciaP1 = 0.12
distanciaP2 = 0.12
deltaX = 0.02


"""
Se realiza una funcion para verificar
que el valor ingresado sea
un numero.
"""
def VerificacionNum(num):
    try:
        num = int(num)
        return num
    except ValueError:
        print("Solamente puedes ingresar numeros")


def ImpresionTitulo():
    texto = ("\nBienvenido a la Simulación del Comportamiento de un Tubo de Rayos Catodicos:\n ")
    for i in texto:
        sys.stdout.write(i)
        sys.stdout.flush()
        t.sleep(0.04)



# Variables fisicas controladas por usuario

"""
Voltaje de aceleracion de los electrones
Voltaje de placas de deflexion vertical
Voltaje de deflexion horizontal

Boton de cambio de modo
Control de señal sinusoidal (Todavía no)
Tiempo de latencia del punto en la pantalla

"""

#Mensaje de bienvenida
ImpresionTitulo()

"""
Funcion realizada para
todos los procesos relacionados
con el menú.
"""
def Menu():
    #Variable de menu
    salir = False
        
    #Ciclo del menu
    while salir == False:
        #Se muestran las opciones del menú
        print("\nQue desea hacer? ")
        print(" 1) Iniciar simulacion")
        print(" 2) Salir")
        opcion = input("Ingrese su opción: ")
        #Se verifica si se ingresa un numero o no
        try:
            opcion = int(opcion)
        except ValueError:
            print("Solamente puedes ingresar numeros")
        
        if (opcion == 1):
            print("\nIniciando simulacion...")
            
            # Solicitar valor de voltaje de placas
            valido = False
            while (valido == False):
           
                
                voltajeP1 = input ( " >> Ingrese el voltaje vertical: " )
                voltajeP2 = input ( " >> Ingrese el voltaje horizontal: " )

                voltajeP1 = int(voltajeP1)
                voltajeP2 = int(voltajeP2)

                VoltajeAceleracionElectron = input(" >> Ingrese el voltaje de aceleracion: ")
                VoltajeAceleracionElectron = int(VoltajeAceleracionElectron)
                
                # Verificar que el voltaje esté definido dentro del intervalo
                if (voltajeP1 >= -1000 and voltajeP1 <= 1000):
                    if (voltajeP2 >= -1000 and voltajeP2 <= 1000):
                        if ( VoltajeAceleracionElectron >= -1000 and VoltajeAceleracionElectron <= 1000):
                            valido = True
            print("\n")
            OperacionesFisicas (CargaParticula, voltajeP1, MasaParticula, distanciaP1, VoltajeAceleracionElectron, distanciaP2, deltaX)
            

        #Opcion de salida
        if (opcion == 2):
            print("Gracias por usar este programa")
            salir = True
            
Menu()

