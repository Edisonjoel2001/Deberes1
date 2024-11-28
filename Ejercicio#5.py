#Ejercicio Número 5
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Programa para determinar el descuento en una tienda")

#Vamos a utilizar la variable precio y otra ves float para agarrar a los numeros decimales

precio = float(input("Ingrese el precio del producto: "))

#Utilizamos las condiciones If(Si) y Else(Sino)

if precio > 100:
    descuento = precio * 0.20 #Aqui es donde vamos a calcular el descuento del 20%

    precio_final =precio - descuento #Aqui nos reflejara el precio de la compra total

    print(f"Se aplicó un descuento de ${descuento:.2f}. El monto final a pagar es ${precio_final:.2f}.")#Aqui se imprime si se aplica el descuento  debido al consumo de 100

else:
    print(f"No se aplica descuento. El monto final a pagar es ${precio:.2f}.") #Aqui se imprime si no se aplica el descuento  debido al consumo de 100



