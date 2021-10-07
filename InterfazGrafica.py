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

from tkinter import *
from tkinter import ttk

# Variables manejadas por el usuario:



VentanaPrincipal = Tk()
VentanaPrincipal.title('Proyecto - Fisica 3')
VentanaPrincipal.config(bg='white')
VentanaPrincipal.geometry("1280x720")

f = ('Arial', 11)

left_frame = Frame(
    VentanaPrincipal, 
    bd=2, 
    bg='#CCCCCC',   
    relief=SOLID, 
    padx=10, 
    pady=10
    )

Label(
    left_frame, 
    text="Ingrese el voltaje vertical: ", 
    bg='#CCCCCC',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(
    left_frame, 
    text="Ingrese el voltaje horizontal: ", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, pady=10)

VoltajeVertical  = Entry(
    left_frame, 
    font=f,
    #textvariable = V_Vertical
    )

IngresoUsuario_V = VoltajeVertical.get()


VoltajeHorizontal= Entry(
    left_frame, 
    font=f,
    #textvariable = V_Horizontal

    )

IngresoUsuario_H = VoltajeHorizontal.get()

EnvioInfo = Button(
    left_frame, 
    width=15, 
    text='Enviar Datos', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=exit
    )

VoltajeHorizontal.grid(row=0, column=1, pady=5, padx=15)
VoltajeVertical.grid(row=1, column=1, pady=5, padx=15)
EnvioInfo.grid(row=2, column=1, pady=5, padx=15)
left_frame.pack()


VentanaPrincipal.mainloop()