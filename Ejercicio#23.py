#Ejercicio Número 23
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Programa para solicitar calificaciones al usuario (hasta que ingrese -1) y calcula el promedio. ")

# Iniciamos escogiendo las varaibles que vamos a utilizar
total_notas = 0
cantidad_notas = 0

# Con el bucle While true, pedimos que ingrese las notas hasta que ingrese (-1)
while True:
    calificacion = float(input("Ingresa una calificación (o -1 para terminar): "))

    if calificacion == -1:
        break  # Salir del ciclo si el usuario ingresa -1

    total_notas += calificacion
    cantidad_notas += 1

# Calcular y mostrar el promedio, para lo cual debemos utilizar las condicionales if(Si) y else(Sino)
if cantidad_notas > 0:
    promedio = total_notas / cantidad_notas
    print(f"El promedio de las calificaciones es: {promedio}") # Imprimimos el promedio final
else:
    print("No se ingresaron calificaciones.") # Imprimimos si no se ingresaron calificaciones
