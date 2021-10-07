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

# Librerias importadas
from tkinter import *
from tkinter import ttk
import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

#Se llama a función lissajous
from Lissajous import *




Alfa: int
Beta: int
PiValue: int


VentanaPrincipal = Tk()
VentanaPrincipal.title('Modo Dinámico - Curvas de Lissajous')
VentanaPrincipal.config(bg='white')
VentanaPrincipal.geometry("1280x720")
Titulo_1=Label(VentanaPrincipal,text=("Modo Dinámico"),background="blue",foreground="White", font =("Arial",30), width = 30)
Titulo_1.pack(side=TOP,fill=tkinter.Y)


# Funciones para definir valor de Pi
def PiCero():
    global PiValue
    PiValue = 0
    return PiValue

def PiCuartos():
    global PiValue
    PiValue = 1/4
    print(PiValue)

def PiMedios():
    global PiValue
    PiValue = 1/2
    print(PiValue)

def PiTresPiCuartos():
    global PiValue
    PiValue = 3/4
    print(PiValue)

def PiUno():
    global PiValue
    PiValue = 1
    print(PiValue)

#Boton para ingresar Alfa
ValorAlfa=Label(text=("Ingrese valor de A: "), bd=2, 
    bg='#CCCCCC',   
    relief=SOLID, 
    padx=10, 
    pady=10)
ValorAlfa.place(x=20,y=50+15)

#Boton para ingresar Beta
ValorBeta=Label(text=("Ingrese valor de B: "), bd=2, 
    bg='#CCCCCC',   
    relief=SOLID, 
    padx=10, 
    pady=10)
ValorBeta.place(x=20,y=200+15)

# Ingreso de valores de Alfa y Beta
A=Entry(VentanaPrincipal)
A.place(x=20,y=120)
B=Entry(VentanaPrincipal)
B.place(x=20,y=280)

def EnviarDatos():
    Alfa = int(A.get())
    Beta = int(B.get())
    CurvasLissajous(Alfa, Beta, PiValue)

def CerrarGrafico():
    plt.close()


# Seleccion del valor de Pi

# Pi = 0
BotonCero = Button(text = "Cero", width=7, bg = "green", fg = "white", command = PiCero, height = 2, font = ("Arial", 15))
BotonCero.place(x=120+70,y=620)

# Pi = 1/4
BotonPiCuartos = Button(text = "Pi/4", width=7, bg = "green", fg = "white", command = PiCuartos, height = 2, font = ("Arial", 15))
BotonPiCuartos.place(x=240+70,y=620)

# Pi = 1/2
BotonPiMedios = Button(text = "Pi/2", width=7, bg = "green", fg = "white", command = PiMedios, height = 2, font = ("Arial", 15))
BotonPiMedios.place(x=360+70,y=620)

# Pi = 3/4
BotonTresPiCuartos = Button(text = "3Pi/4", width=7, bg = "green", fg = "white", command = PiTresPiCuartos, height = 2, font = ("Arial", 15))
BotonTresPiCuartos.place(x=480+70,y=620)

# Pi = 1
BotonPi = Button(text = "Pi", width=7, bg = "green", fg = "white", command = PiUno, height = 2, font = ("Arial", 15))
BotonPi.place(x=600+70,y=620)


Grafico=Button(text=("Mostrar gráfica dinámica"),command=EnviarDatos, width = 25, bg = "orange", fg = "white", height = 2)
Grafico.place(x=800+70,y=625)


# Regresar al modo anterior
Grafico=Button(text=("Regresar Modo Estático"),command=lambda: controller.show_frame("Proyecto - Fisica 3") , width = 25, bg = "red", fg = "black", height = 2)
Grafico.place(x=940,y=90)

# Cerrar grafico actual
Grafico=Button(text=("X"),command=CerrarGrafico, width = 3, bg = "red", fg = "white", height = 2)
Grafico.place(x=90,y=625)

VentanaPrincipal.resizable()
VentanaPrincipal.mainloop()