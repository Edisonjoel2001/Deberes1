#Deber Número #
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa
print("Bienvenido, programa para determinar si un numero es positivo, negativo o cero ")

#Pedimos ingreso de número para determinar, Tambien utilziamos float para representar a un numero fltante o decimal

resultado = float(input("Ingrese un numero: "))

# Utilizamos las condiciones If(si), Elif(Sino,si) y else (Sino)

if resultado > 0:
    print("El número es positivo.") #Imprimimos si el numero es Positivo

elif resultado < 0:
    print("El número es negativo.")#Imprimimos si el numero es Negativo

else:
    print("El número es cero.")#Imprimimos si el numero es 0