# try:
#     numero = 5/0
#     print(f"El numero es {numero}")
#     sumar=1+"1"
# except ZeroDivisionError:
#     print("Hubo un error al hacer la división")
# except TypeError:
#     print("No se puede sumar entre strings y números ")
# except:
#     print("error desconocido")
# else:
#     print("todo bien bro")
# finally:
    # print("igual me ejecuto jeje")   
    # finally se ejecuta si hay o no error
numeros=[]
while len(numeros)!=4:
    try: 
        numero=int(input("Ingrese 4 números : "))
        numeros.append(numero)
    except:
        pass
print("los números son {} ".format(numeros))
    