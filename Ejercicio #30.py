#Ejercicio Número 30
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Solicita un nombre de usuario y contraseña, y valida si ambos son correctos.")

# Primero creamos el usario y contraseña original
usuario1 = "Edison"
contrasena1 = "Joel"

# Escribimos el numero maximo de intentos
intentos_maximos = 3

# El bucle for nos va a permitir que es usuario solo tenga tres intentos
for intento in range(intentos_maximos):
    usuario = input("Ingresa tu nombre de usuario: ")
    contrasena = input("Ingresa tu contraseña: ")

    # Aqui vamos a validar que los datos sean los correctos si no se bloqueara el acceso
    if usuario == usuario1 and contrasena == contrasena1:
        print("Acceso concedido.")
        break  # Si los datos son correctos, salir del bucle
    else:
        intentos_restantes = intentos_maximos - (intento + 1)
        if intentos_restantes > 0:
            print(f"Datos incorrectos. Te quedan {intentos_restantes} intentos.")
        else:
            print("Acceso bloqueado. Has superado el número de intentos permitidos.")
