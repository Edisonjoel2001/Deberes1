#Ejercicio Número 21
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Solicita un numero y calcula la suma de sus digitos")

# Solicitamos un numero entero
num = int(input("Ingresa un número entero: "))

# Calculamos las la suma de el numero entero ingresado
suma = sum(int(digit) for digit in str(abs(num)))

# Mostramos el resutado de la suma de los digitos del numero entero
print(f"La suma de los dígitos de {num} es: {suma}")
