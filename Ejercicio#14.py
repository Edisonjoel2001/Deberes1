#Ejercicio Número 14
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Programa para ingresar una calificacion numerica y nos devuelva una letra. ")

# Tambien utilizamos float, para hagarrar numeros flotantes y decimales

nota = float(input("Por favor, introduzca la calificacion correspondiente: ")) #Pedimos al profesor la nota numerica

#Utilizamos condicionales if(Si), elif(Sino,si) y else(Sino)

if 90 <= nota <= 100:   # Si es entre 90 y 100
    letra = "A"         # Obtiene la letra A

elif 80 <= nota <= 89:  # Si es entre 80 y 89
    letra = "B"         # Obtiene la letra B

elif 70 <= nota <= 79:  # Si es entre 70 y 79
    letra = "C"         # Obtiene la letra C

elif 60 <= nota <= 69:  # Si es entre 60 y 69
    letra = "D"         # Obtiene la letra D

else:
    letra = "F"         # Obtiene la letra F

#Aqui es donde imprimimos la letra de la nota obtenida

print(f"Tu nota en letra es {letra}.")