#Ejercicio Número 8
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Programa para determinar la clasificacion de edades")

#Empezamos la solicitud de la edad a el usuario, y utilizamos int, por que solo se trata de enteros

edad = int(input("Introduce tu edad: "))

#Aqui empezamos con la clasificaicion de edades, utilizamos las condiciones if(SI), elif(Sino,si), else(Sino)

if edad >= 0 and edad <= 12: #Aqui determinamos si es menor de edad
    print("Eres un menor de edad.")

elif edad >= 13 and edad <= 17:  #Aqui determinamos si es un adolescente
    print("Eres un adolescente.")

else:                               #Aqui determinamos si es un adulto
    print("Eres un adulto.")
