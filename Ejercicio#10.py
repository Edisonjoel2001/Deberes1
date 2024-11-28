#Ejercicio Número 10
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Programa para calcular si es año bisiesto o no es año bisiesto")

#Empezamos por solicitar el año a la persona que utilice el programa
#Utilizamos variable anio y int para que solo sean numeros enteros
anio = int(input("Por favor, Introduzca el año: "))

#Aqui es donde vamos a determinar el tipo de año, y utilizamos las condionales if(Si) y else(Sino)

if (anio % 4 == 0 and anio % 100 != 0) or  (anio % 400 == 0): #Tambien utilizamos operadores logicos and y or
    print(f"El año que usted ingreso {anio} es bisiesto.") #Imprimimos si es año bisiesto
else:
    print(f"El año que usted ingreso {anio} no es bisiesto") #Imprimimos si no es año bisiesto

