#Deber Numero #1
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa
print("Bienvenido Programa para calcular si un numero es mayor o menor que 10")

#Empezamos nuestro programa pidiendo al usuario que ingrese un numero Lo cual vamos a escoger el nombre de RESULTADO, para definirlo como la variable

#Float es para representar un numero flotante o un decimal
resultado = float(input("Ingrese un numero: "))

# Utilizamos las condiciones If(si), Elif(Sino,si) y else (Sino)

if resultado > 10:
    print("El número es mayor que 10.") #Imprimimos si el numero es Mayor

elif resultado < 10:
    print("El número es menor que 10.")#Imprimimos si el numero es Menor

else:
    print("El número es igual a 10.")#Imprimimos el Resultado

