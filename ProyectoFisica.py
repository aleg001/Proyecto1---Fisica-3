# Universidad del Valle de Guatemala
# Fisica 3 - Proyecto 1
# Integrantes: Alejandro Gómez 20347 y Paola de León 20361
# Fecha de creacion: 28/09/2021
# Ultima modificacion 30/09/2021

#Mensaje de bienvenida
print("Bienvenido a la SIMULACIÓN DEL COMPORTAMIENTO DE UN TUBO DE RAYOS CATÓDICOS: \n")


# Variables Fisicas fijadas

""" Tamano Pantalla
 Area Placas Deflexion
Distancia Entre Placas
Distancia desde placas verticales a horizontales """


# Variables fisicas controladas por usuario

"""
Voltaje de aceleracion de los electrones
Voltaje de placas de deflexion vertical
Voltaje de deflexion horizontal

Boton de cambio de modo
Control de señal sinusoidal
Tiempo de latencia del punto en la pantalla

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
            print("Iniciando simulacion xddd")

        
        #Opcion para decodificar
        if (opcion == 2):
            print("Gracias por usar este programa")
            salir = True
            
Menu()

