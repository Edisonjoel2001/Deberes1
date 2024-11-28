#Ejercicio Número 26
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Crea una función que reciba un número y retorne True si es par y False si es impar.")

def es_par(num): #
    if num % 2 == 0:
        return True
    else:
        return False

 # Empezamos el ejericio, difiniendo variables y int para que solo sean numero enteros
num = int(input("Ingresa un número: "))  #Pedimos el numero
resultado = es_par(num)

if resultado:
    print(f"El número {num} es par.") # Entregamos el resultado a el usuario
else:
    print(f"El número {num} es impar.") # Entregamos el resultado a el usuario

