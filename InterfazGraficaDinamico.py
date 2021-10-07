# Universidad del Valle de Guatemala
# Fisica 3 - Proyecto 1
# Integrantes: Alejandro Gómez 20347 y Paola de León 20361
# Fecha de creacion: 30/09/2021
# Ultima modificacion 30/09/2021
# Modulo: Interfaz Grafica - Modo dinamico

"""
Modulo para la interfaz gráfica del
modo dinámico (Curvas Lissajous)
"""

from tkinter import *
from tkinter import ttk
import tkinter

#Se llama a función lissajous
from Lissajous import *

PiValue = 2
Alfa = 1
Beta = 1


VentanaPrincipal = Tk()
VentanaPrincipal.title('Modo Dinámico - Curvas de Lissajous')
VentanaPrincipal.config(bg='white')
VentanaPrincipal.geometry("1280x720")
Titulo_1=Label(VentanaPrincipal,text=("Modo Dinámico"),background="blue",foreground="White", font =("Arial",30), width = 30)
Titulo_1.pack(side=TOP,fill=tkinter.Y)


# Funciones para definir valor de Pi
def PiCero():
    PiValue = 0
    print(PiValue)

def PiCuartos():
    PiValue = 1/4
    print(PiValue)

def PiMedios():
    PiValue = 1/2
    print(PiValue)

def PiTresPiCuartos():
    PiValue = 3/4
    print(PiValue)

def PiUno():
    PiValue = 1
    print(PiValue)

def GenerarGrafico():
    CurvasLissajous(Alfa, Beta, PiValue)

#Boton para ingresar Alfa


#Boton para ingresar Beta


#Seleccion del valor de Pi

BotonCero = Button(text = "Cero", width=7, bg = "green", fg = "white", command = PiCero, height = 2, font = ("Arial", 15))
BotonCero.place(x=120+50,y=620)

BotonPiCuartos = Button(text = "Pi/4", width=7, bg = "green", fg = "white", command = PiCuartos, height = 2, font = ("Arial", 15))
BotonPiCuartos.place(x=240+50,y=620)

BotonPiMedios = Button(text = "Pi/2", width=7, bg = "green", fg = "white", command = PiMedios, height = 2, font = ("Arial", 15))
BotonPiMedios.place(x=360+50,y=620)

BotonTresPiCuartos = Button(text = "3Pi/4", width=7, bg = "green", fg = "white", command = PiTresPiCuartos, height = 2, font = ("Arial", 15))
BotonTresPiCuartos.place(x=480+50,y=620)

BotonPi = Button(text = "Pi", width=7, bg = "green", fg = "white", command = PiUno, height = 2, font = ("Arial", 15))
BotonPi.place(x=600+50,y=620)





VentanaPrincipal.resizable()
VentanaPrincipal.mainloop()