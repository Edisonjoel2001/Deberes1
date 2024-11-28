#Ejercicio Número 21
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Programa para invertir un numero entero ")

# Utilizamos la variable num, y que sea int: para recoger solo numeros enteros
num = int(input("Ingresa un número entero: "))

# Convertimoa el número a una cadena,la invertimoa y mostramos el resultado
numero = str(abs(num))[::-1]  # Invertir la cadena

# Si el número era negativo, agregar el signo de nuevo
if num < 0:
    numero = "-" + numero

print(f"El numero invertido de {num} es: {numero}")
