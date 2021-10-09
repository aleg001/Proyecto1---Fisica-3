# Universidad del Valle de Guatemala
# Fisica 3 - Proyecto 1
# Integrantes: Alejandro Gómez 20347 y Paola de León 20361
# Fecha de creacion: 30/09/2021
# Ultima modificacion 30/09/2021
# Modulo: Interfaz Grafica

"""
Modulo de prueba de interfaz grafica:
Se implementará totalmente en la entrega
final del proyecto. Utilizado para
presentar los datos de forma ordenada
y amigable con el usuario.

"""

import tkinter
from tkinter import *
from tkinter import ttk
from Calculos import *

# Variables manejadas por el usuario:

# Import de GraficoDinamico
#from InterfazGraficaDinamico import *

def ModoEstatico(CargaParticula, MasaParticula, distanciaP1, distanciaP2, deltaX):

    VentanaPrincipal = Tk()
    VentanaPrincipal.title('Modo Estático - Pantalla Frontal')
    VentanaPrincipal.config(bg='white')
    VentanaPrincipal.geometry("1280x720")
    Titulo_1=Label(VentanaPrincipal,text=("Modo Estático"),background="blue",foreground="White", font =("Arial",30), width = 30)
    Titulo_1.pack(side=TOP,fill=tkinter.Y)

    #Boton para ingresar Alfa
    VoltajeHorizontal=Label(text=("Ingrese el voltaje horizontal "), bd=2, bg='#CCCCCC', relief=SOLID, padx=10, pady=10)
    VoltajeHorizontal.place(x=20,y=50+15)

    #Boton para ingresar Beta
    VoltajeVertical=Label(text=("Ingrese el voltaje vertical "), bd=2, bg='#CCCCCC', relief=SOLID, padx=10, pady=10)
    VoltajeVertical.place(x=20,y=200+15)

    # Ingreso de valores de Alfa y Beta
    Horizontal=Entry(VentanaPrincipal)
    Horizontal.place(x=20,y=120)
    Vertical=Entry(VentanaPrincipal)
    Vertical.place(x=20,y=280)

    # Boton para cambiar entre ventanas
    def CambiarVentana():
        VentanaPrincipal.destroy()

    # Funcion para mostrar grafico con datos ingresados
    def EnviarDatos():
        VHorizontal = int(Horizontal.get())
        VVertical = int(Vertical.get())
        #LLAMAR A GRAFICOS LATERAL, SUPERIOR Y PUNTO FIJO
        OperacionesFisicas (CargaParticula, MasaParticula, distanciaP1, distanciaP2, deltaX, VHorizontal, VVertical)

    # Boton para mostrar la gráfica
    Grafico=Button(text=("Mostrar gráficos"),command=EnviarDatos, width = 25, bg = "orange", fg = "white", height = 2)
    Grafico.place(x=800+70,y=625)

    # Regresar al modo anterior
    Estatico=Button(text=("Regresar a menu"),command=CambiarVentana , width = 25, bg = "red", fg = "black", height = 2)
    Estatico.place(x=940,y=90)

    VentanaPrincipal.resizable()
    VentanaPrincipal.mainloop()
