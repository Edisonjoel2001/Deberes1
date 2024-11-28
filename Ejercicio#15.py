#Ejercicio Número 14
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Programa para ingresar usuario y contraseña y denegar a los 3 intentos fallidos. ")

# Definir el nombre de usuario y la contraseña correctos
usuario1 = "Edison"
contraseña1= "031201"

# Inicializar el contador de intentos
intentos = 0

# Establecer el límite de intentos
limite_intentos = 3

# Ciclo para permitir hasta tres intentos
while intentos < limite_intentos:
    # Solicitar el nombre de usuario y la contraseña
    usuario2 = input("Introduce tu nombre de usuario: ")
    contraseña2 = input("Introduce tu contraseña: ")

    # Validar si el nombre de usuario y la contraseña son correctos
    if usuario2 == usuario1 and contraseña2 == contraseña1:
        print("Acceso concedido.")
        break  # Salir del ciclo si los datos son correctos
    else:
        intentos += 1
        if intentos < limite_intentos:
            print(f"Datos incorrectos. Te quedan {limite_intentos - intentos} intentos.")
        else:
            print("Has superado el número máximo de intentos. Acceso bloqueado.")
