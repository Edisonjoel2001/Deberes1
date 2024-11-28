#Ejercicio Número 12
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa
#Importamos la libreria random

import random

print("Programa para adivinar un numero entre el 1 y el 10")

# Empezamos por la generacion de un numero Random entre el 1 y el 10

numero = random.randint(1, 10)

# Pedimos al jugador que ingrese el numero y utilizamos int para definir que solo sean numeros enteros

juego = int(input("Adivina el número entre 1 y 10: ")) #Usuario ingresa el numero

# Aqui verificamos si acerto o no al numero y utilizamos las condicionales if(Si) y else(Sino)
if juego == numero:
    print("¡Felicidades! Adivinaste el número correctamente.") #Imprimimos si el numero fue el acertado
else:
    print(f"Lo siento, el número correcto era {numero}. Intenta de nuevo.") # Imprimimos si no fue el correcto y decimos que intente de nuevo
