#Ejercicio Número 7
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Programa para determinar de tres numeros cual es el mayor")

#Entonces pedimos ingreso de 3 numero con Float para tambien escoger a los decimales

num1 = float(input("Por favor, introduzca el primer numero: "))
num2 = float(input("Por favor, introduzca el segundo numero: "))
num3 = float(input("Por favor, introduzca el tercer numero: "))

#Determinamos cual de los tres numero es el mayor y utilizamos la condicion if(SI)

mayor = num1  # Asumimos que el primer número es el mayor

if num2 > mayor:
    mayor = num2  # Aqui determinamos, si es mayor o no
if num3 > mayor:
    mayor = num3  # Aqui determinamos, si es mayor o no

#Imprimimos el resultado Dando a entender cual es el mayor
print(f"El número mayor es: {mayor}")
