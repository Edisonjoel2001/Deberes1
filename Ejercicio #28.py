#Ejercicio Número 28
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Crea una función que reciba el radio de un círculo y retorne su área. ")

# Primero importamos una libreira nueva

import math  # Importamos la librería math para obtener el valor de pi

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2  # Escribimos la formula para obtener el area del circulo
    return area   #Aqui retornamos el area


radio = float(input("Por favor,Ingresa el radio del círculo: "))  # Pedimos al usuario que ingrese el radio

area = calcular_area_circulo(radio)

print(f"El área del círculo con radio {radio} es: {area}") # Devolvemos el area
