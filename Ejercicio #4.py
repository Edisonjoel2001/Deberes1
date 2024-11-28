#Ejercicio Número 4
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Programa para determinar si un alumno reprobo o aprobo")

#Vamos a utilizar la variable nota y otra ves float para agarrar a los numeros decimales
nota = float(input("Ingrese la nota del alumno"))
#Utilizamos las condiciones If(Si) y Else(Sino)

if nota >= 7:
    print("El alumno esta aprobado. ") #Imprimimos si el alumno esta aprobado
else:
    print("El alumno esta reprobado") #Imprimimos si el alumno esta reprobado