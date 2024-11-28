#Ejercicio Numero 6
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Bienvenido, programa para determinar si esta en edad para votar ")

#Vamos a utilizar la variable Edad y la variable int, para tener solo numeros enteros

Edad = int(input("Por favor ingrese su edad: "))

#Utilizamos las condiciones If(Si) y Else(Sino)

if Edad >= 18:
    print("Usted es apto para votar. ") #Imprimimos si esa persona es apta para votar
else:
    print("Usted no es apto para votar") #Imprimimos si esa persona no es apta para votar