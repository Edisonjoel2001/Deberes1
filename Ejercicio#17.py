#Ejercicio Número 17
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Programa para crear tabla de multiplicar, pidiendo numero al usuario. ")

# Solicitamos el numero al usuario, para crear la tabla de multiplicar

num = int(input("Introduce un número para ver su tabla de multiplicar: ")) #Pedimos el numero al usuario

# Mostrar la tabla de multiplicar del número

for i in range(1, 11):   #Ocupamos el bucle for

    resultado = num * i

    print(f"{num} x {i} = {resultado}") #Imprimimos el resultado
