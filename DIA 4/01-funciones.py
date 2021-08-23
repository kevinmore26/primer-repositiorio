# una función es un bloque de código que se va a ejecutar cuántas veces sea llamada la funcíon

def saludar():
    print("hola buenas tardes")

saludar()


# funciones con parámetros

def saludarPersona(nombre):
    edad=40
    print(f"hola{nombre} como te va")


def sin_nombre():
    print("yo soy una función sin nombre")

sin_nombre()

# las funciones pueden recibir parámetros y estos pueden ser opcionales
# el None es para que pueda ser opcional
def registro(nombre,correo=None):
    print("registro existoso")

registro("kevin")
registro("kevin","keviskdja@ladklñaskd.com")


# def identificación(nombre,apellido,nacionalidad=None):


# el parametro que tiene el valor * es un parametro especial de python que sirve  para almacenar n valores 
# def alumnos (*args):
#     print alumnos 

# en la funcion alumnos_notas se recibira una cantidad N de alumnos en la cual se debe indicar cuantos aprobaron y cuantos desaprobaron siendo la nota minima 11

def alumnos_notas(*args):
    # todo: implementar logica
    print(args)
    notaaprobado=0
    notadesaprobado=0
    for nota in args:
        if nota['promedio']>=11:
            notaaprobado+=1
    else:
        
        notadesaprobado+=1

print(f"hay {notaaprobado} aprobados y también hay {notadesaprobado}desaprobados")


alumnos_notas(
    {"nombre":"Raul", "promedio": 17},
    {"nombre": "Roxana", "promedio": 20},
    {"nombre": "Alfonso", "promedio": 10},
    {"nombre": "Pedro", "promedio": 8},
    {"nombre": "Katherine", "promedio": 16},
)


