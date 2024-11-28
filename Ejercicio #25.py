#Ejercicio Número 25
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Escribe una función que reciba dos números como parámetros y retorne su suma.")

# Empezamos con definir la funcion sumar
def sumar(num1, num2): #Definimos la funcion y variables
    return num1 + num2  # Definimos el retorno que va a se la suma de las dos variables

 # Empezamos el ejericio, difiniendo variables y dando float para que tengamos flotantes y decimales
numero = float(input("Por favor, ingresa el primer número: ")) #Pedimos el primer numero
numero1 = float(input("Por favor, ingresa el segundo número: ")) #Pedimos el segundo numero

resultado = sumar(numero, numero1)
print(f"La suma de {numero} y {numero1} es: {resultado}") # Entregamos el resultado a el usuario

