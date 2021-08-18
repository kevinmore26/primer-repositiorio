numero1 = 10
numero2= 80

persona1="Eduardo"

persona2="Ricardo"

#suma
# NOTA:SI LAS 2 O MÁS VARIABLES SON NUMÉRICAS SE REALIZARÁ LA SUMA,
# SI ES QUE NO Y SON STRING O CARACTERES, SE CONCATENARÁN
# EN JAVASCRIPT SÍ SE PODÍA UNIR, PERO EN PYTHON NO SE PUEDE UNIR UN STRING CON UNA VARIABLE NUMÉRICA    

# print(numero1+persona2)

# para convertir un numeral al string
numero1_string= str(numero1)
print(numero1_string+persona1)

# RESTA

print(numero1 - numero2)
# print(personal - persona2)


# no se puede restar con varriables no numéricas

# MULTIPLICACION

print(numero1 * numero2)
print(persona1* 2)


numero3= 80
numero4=10

print("La multiplicación de {} y{} es :{}".format(numero3,numero4,numero3*numero4))

# DIVISION
# TODA DIVISION AÚN ASÍ SEA ENTERA SIEMPRE SER+A FLOTANTE(UNA PARTE ENTERA Y OTRA DECIMAL)

print(numero2/numero1)
print(numero1/numero2)

# MODULO
# el módulo es el resultado de la división(residuo)

print(numero2%numero1)

# COCIENTE (parte entera)
print(numero2//numero1)
print(numero1//numero2)