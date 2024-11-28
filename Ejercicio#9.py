#Ejercicio Número 9
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Calculadora Basica")

# Primero pedimos al usuario ingreso de numeros, y utilizamos la variable num para definir y float para tambien aceptar con decimales
num1 = float(input("Por favor, introduzca el primer numero: "))
num2 = float(input("Por favor, introduzca el segundo numero: "))

# Aqui vamos a pedir al usuraio que ingrese el tipo de operacion a realizar
operacion = input("Introduce la operación (+, -, *, /): ")

# Aqui se va a realizar el calculo, segun lo escogido por el usuraio, sea Suma, Resta, Multiplicacion y Division
# Tambien vamos a utilizar las condicionales if (Si), elif(Sino,si), else(Sino)
if operacion == "+":
    total = num1 + num2     #Aqui realizamos la Suma
    print(f"El resultado de {num1} + {num2} es: {total}")
elif operacion == "-":
    total = num1 - num2         #Aqui realizamos la Resta
    print(f"El resultado de {num1} - {num2} es: {total}")
elif operacion == "*":
    total = num1 * num2     #Aqui realizamos la Multiplicacion
    print(f"El resultado de {num1} * {num2} es: {total}")
elif operacion == "/":
    if num2 != 0:
        total = num1 / num2  #Aqui realizamos la Divsion
        print(f"El resultado de {num1} / {num2} es: {total}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operación no válida. Por favor, elige entre +, -, * o /.")
