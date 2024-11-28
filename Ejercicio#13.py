#Ejercicio Número 13
   #Edison Cabezas
     #Tercer Semestre
        #Primero escribirmos un mensaje de Bienvenida a nuestro programa

print("Programa para consultar que signo zodiacal eres. ")

# Pedimos al usuario que ingrese su fecha de nacimiento, solo dia y mes
#Tenemos las variables mes y dia, que son enteras

dia = int(input("Por favor, introduce tu dia de nacimiento (1-31): "))
mes = int(input("Por favor, introduce el mes de tu nacimiento (1-12): "))

#Aqui utilziamos condicionales if(Si) y elif (Sino,si)
# Tambien operadores logicos como and y or

if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    signo = "Aries"
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    signo = "Tauro"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    signo = "Géminis"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    signo = "Cáncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    signo = "Leo"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    signo = "Virgo"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    signo = "Libra"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    signo = "Escorpio"
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    signo = "Sagitario"
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    signo = "Capricornio"
elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    signo = "Acuario"
else:
    signo = "Piscis"

# Al final mostramos a la persona interesado su signo zodiacal
print(f"Tu signo zodiacal es {signo}.") #Imprimimos el signo zodiacal
