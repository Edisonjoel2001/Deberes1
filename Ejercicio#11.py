#Ejercicio Número 1
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Programa para verificar que la contraseña sea correcta")

#Primero vamos a definir la contraseña correcta
contraseña = "031201"

#Ahora vamos a pedir al usuario que ingrese una contraseña

contraseña1 = input("Por favor, introduzca la contraseña: ")

#Ahora vamos a empezar a validar si las contraseñas coinciden
#Utilziamos condicionales if(Si) y else(Sino)

if contraseña == contraseña1:
    print("La contraseña que usted ingreso es correcta. Bienvenido")
else:
    print("La contraseña que ustes ingreso es incorrecta. Acceso denegado")