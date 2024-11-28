#Ejercicio Número 23
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Programa para crear una función que reciba un nombre como parámetro y retorne un saludo.")

# Empezamos definiendo la funcion saludar
def saludar(nombre):
    return f"Hola, Buen dia {nombre}!"

# Ejemplo de uso
nombre1 = input("Ingresa tu nombre: ") #Pedimos al usuario que ingrese su nombre
saludo = saludar(nombre1)
print(saludo)

