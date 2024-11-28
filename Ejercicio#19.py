#Ejercicio Número 19
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Ingrese el numero para hacerlo factotial. ")

# Solicitamos el numero al usuario para empezar el ejercicio
num = int(input("Introduce un número para calcular su factorial: "))

# Iniciamos el resultado del factorial en 1
factorial = 1

# Utilizamos el bucle for para empezar
for i in range(1, num + 1):
    factorial *= i  # Multiplicar el resultado por cada número de 1 hasta el número ingresado

# Mostramos el resultado a el usuario
print(f"El factorial de {num} es: {factorial}")
