# List => Listas
# ordenadas, y modificables
colores=['morado','azul','rosado','amarillo']
mezclada =['otoño',14,False,15.2,[1,2,3]]

# imprimir la primera posición
# en python si la posición no existe, lanzará un error, a diferencia de JS, que indicará undfined
print(colores[0])
# se puede contar al revés contando de derecha a izquierda comenzando por el " -1 "
print(colores[-1])
# el de abajo significa que está dentro de 1 y el que está antes que 3 (<"3") (mayor y menor que)
print(colores[1:3])
# traeme menor que 2
print(colores[:2])

# sirve para copiar el contenido de la lista  más no su ubicación de memoria
colores_2=colores[:]
print(id(colores_2))
print(id(colores))

print(colores[1:-1])

# Método para agregar un elemento a una lista

colores.append('naranja')
print(colores)

# método para eliminar un valor 
# solamente si existe lo eliminará,sino lanzará un error
# colores.remove(True)
print(colores)
colores.remove('azul')
print(colores)

# si quieres eliminarlo y además guardar el valor eliminado en una variable
color_eliminado = colores.pop(0)
print(colores)
print(color_eliminado)

# el método para eliminar el valor 
# nombre="eduardo"
# del nombreprint(nombre)
# solo eliminar esa parte(abajo)
del colores[0]
print(colores)

# sacar la longitud de la lista 
print(len(colores))

# TUPLAS
# la tupla a diferencia de la lista es una colección de datos ordenada PERO que una vez creada no se puede editar 
# tupla va entre PARENTÉSIS
notas =(10,15,20,9,17)
print(notas[0])
print(len(notas))

print(notas.count(10))
# DICCIONARIOS
persona={
    'nombre':'Eduardo',
    'apellido':'de River',
    'correo':'corre@correo.com',
    'edad':28,
    'donacion_organos':True,
    'hobbies':[
        {
            'nombre':'volar drones',
            'conocimiento':'avanzado'
        },
        {
            'nombre':'montar bici',
            'conocimiento':'intermedio'
        }
    ]

}
# PARA RECORRER

print(persona["edad"])
print(persona['nombre'])
# para crear más
persona['edad']=35
print(persona)
print(persona['hobbies'[0]])

# para extraer solamente las llaves
print(persona.keys())
# forma de extraer solamente los valores 
print(persona.values())

persona.clear()
print(persona)

# conjuntos 
# colección de datos desordenada, que una vez que la creemos podremos acceder a us posiciones que ya estarán ordenadas aleatoriamente

alumnos={'kevin','khaterine','ricardo','aylin'}
print(alumnos)
alumnos.add('Diego')
print(alumnos)
alumnos.remove('Eduardo')
print(alumnos)

# generalmente se usa para guardar valores in la necesidad de llaves
print('matematicas' in cursos)