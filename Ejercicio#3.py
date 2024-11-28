#Ejercicio Número 3
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Bienvenido Con este programa determinamos si el numeor es par o impar")

# Utilizamos un numero al usuario y determinamos con INT que sea un numero entero
digito = int(input("Introduce un número: "))

# Comprobamos si el numero es par o impar, y utilizamos if(SI) y else(Sino) como condiciones
if digito % 2 == 0:
    print(f"El número ingresado {digito} es par.")#Imprimos si es par

else:
    print(f"El número ingresado {digito} es impar.")#Imprimos si es impar
