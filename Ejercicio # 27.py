#Ejercicio Número 27
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Escribe una función que reciba un número y retorne su cuadrado.")


def calcular_cuadrado(num): # Empezamos definiendo la funcion calcular cuadrado
    return num ** 2

# Aqui se empieza el ejercicio

numero = float(input("Ingresa un número: ")) # Pedimos al usario que ingrese le numero, tambien pueden ser decimales

resultado = calcular_cuadrado(numero)

print(f"El cuadrado de {numero} es: {resultado}") #Retornamos el cuadrado del numero
