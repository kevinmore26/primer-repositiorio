from _typeshed import Self


class Electrodomestico:
    def __init__(self):
        self.__nombre=''
        self._color=''
    
    def __setNombre(self,nombre):
        # el setter sirve para definir el contenido del atributo de una manera más formal 
        self.__nombre=nombre

    def __getNombre (self):
        # el getter sirve para devolver el valor del atributo provado
        return self.__nombre

    def __deleteNombre(self):
    # el deleter sIrve para eliminar el contenido del atributo provado 
        del self.__nombre

    nombre = property(__getNombre,__setNombre,__deleteNombre)

    objElectrodomestico =Electrodomestico()
    objElectrodomestico.nombre ="lavadora"