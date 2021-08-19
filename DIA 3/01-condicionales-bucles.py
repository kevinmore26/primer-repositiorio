# # CONDICIONALES
# # If(si) (edad>18) .... else
# # variable=20

# #elif => sino si | siempre va después de un if o después de otro elif a diferencia del else, este lleva a una condición
# edad=78
# if edad>=18 and edad<=64 : 
#     print("puedes vacunarte")
#     print("ashuda")
    

# elif edad >65:
#     print("necesitas tercera dosis") 

# else:
#     print("todavía no puedes vacunarte")

# print("yo me ejecuto así se cumpla o no el if ")

# # OPERADOR TERNARIO
# # FORMA DE VALIDACION PERO DE FORMA SIMPLIFICADA

# texto="Eres mayor de edad" if edad >= 18 else "Eres menor de edad"


# # destructuración de variables lista o tupla
# # variable1,variable2,variable3=['juan','pedro','kevin']
# # print(variable1)
# # print(variable2)

# numeroparami=2
# numero=int(input("ingrese un número unu : "))  
# if((numero%numeroparami)==0):     
#     print("es par") 

# elif((numero//numeroparami)!=0):     
#     print("es impar")

# elif((numero==0)):
#     print("soy 0")

# else:
#     print("no sé que soy :(")

# # bucles
# # for => repite hasta
# meses=['agosto','septiembre','octubre','noviembre','diciembre']
# # si nosotros queremos iterar una colección  de datos   la mejor forma es mediante un FOR
# for mes in meses:
#     print(mes)

# # for(let i=0;i<10;i++){..}

# for numero in range(10):
#     print(numero)


# print("-----------------")
# for numero in range(1,10,3):
#     print(numero)

    # --------------------------
print("-----------------")
numeros=[-4,7,-10,8,25,25,-7]
positivos=0
negativos=0
num_positivos=[]
num_negativos=[]
for numero in numeros:
    if(numero>0):
        num_positivos.append(numero)
        positivos+=1
    else:
        num_negativos.append(numero)
        negativos+=1

print(f"hay {negativos} negativos los cuales son{num_negativos}, {positivos} positivos los cuales son {num_positivos}")
#  el f es format para ya no declarar variables más adelante al final del print

# BRAKE

for segundo in range(60):
    print(segundo)
    if segundo ==10:
        continue
    print(numero)

# 
numeros=[1,2,5,9,12,15,17,21,39]
multide3=0
multide5=0
multiambos=0
for numeromulti in numeros:
    if((numeromulti%5 == 0 )):
        multide5+=1

    elif(numeromulti%3 == 0):
        multide3+=1

    elif((numeromulti%3 and numeromulti%5)==0):
        continue
        
print(f"hay {multide3} multiplos de 3, también hay {multide5} multiplos de 5 ")
# 

# print("----------------------")
numero=int(input("ingrese un números aleatorios menores que el 20 : ")) 
numero_adivinar = 10

for numerosadivinar in range(20):
    print(segundo)
    if numerosadivinar>10 or numerosadivinar>10:
        continue
    print(numero)