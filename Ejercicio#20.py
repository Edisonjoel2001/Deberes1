#Ejercicio Número 20
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Encuentra e imprime todos los números primos entre 1 y 50.")

# Función para verificar si un número es primo
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Solo verificar hasta la raíz cuadrada del número
        if num % i == 0:
            return False
    return True

# Imprimir los números primos entre 1 y 50
for i in range(1, 51):
    if es_primo(i):
        print(i)
