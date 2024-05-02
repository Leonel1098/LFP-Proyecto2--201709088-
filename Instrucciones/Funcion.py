from Errores.Errores import *
from Abstract.Abstract import Expression

class Funcion(Expression):
    def __init__(self, crear, nombre, igual, nueva, crear2, fila, columna):
        self.crear = crear
        self.nombre = nombre
        self.igual = igual
        self.nueva = nueva
        self.crear2 = crear2
        super().__init__(fila, columna)

    def operar(self, arbol):
        pass

    def ejecutarT(self):

        if self.crear == 'CrearBD':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'new':
                        if self.crear2 == 'CrearBD()':
                            return 'use(' + self.nombre + ');'
                        else:
                            return 'Error: falta la palabra reservada CrearBD()'
                    else:
                        return 'Error: Falta la palabra reservada nueva'
                else:
                    return 'Error: Falta el simbolo ='
            else:
                return 'Error: Falta el nombre de la base de datos'
            
        elif self.crear == 'EliminarBD':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'new':
                        if self.crear2 == 'EliminarBD()':
                            return 'db.dropDatabase(' + self.nombre + ');'
                        else:
                            return 'Error: falta la palabra reservada EliminarBD()'
                    else:
                        return 'Error: Falta la palabra reservada elimina'
                else:
                    return 'Error: Falta el simbolo ='
            else:
                return 'Error: Falta el nombre de la base de datos'
        
        if self.crear == 'CrearColeccion':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'new':
                        if self.crear2 == 'CrearColeccion("NombreColeccion")':
                            if self.crear2.startswith('CrearColeccion("') and self.crear2.endswith('")'):
                                nombre_coleccion = self.crear2[len('CrearColeccion("'):-2]
                                return nombre_coleccion
                            return 'db.createCollection(' + self.nombre + ');'

                            """print(self.crear2)
                            palabra = ""
                            for i in self.crear2:
                                palabra +=i
                                if palabra == 'CrearColeccion(':
                                    print(self.crear2)
                                    palabra=""
                            '"""
                        else:
                            return 'Error: falta la palabra reservada CrearColeccion("NombreColeccion")'
                    else:
                        return 'Error: Falta la palabra reservada nueva'
                else:
                    return 'Error: Falta el simbolo ='
            else:
                return 'Error: Falta el nombre de la coleccion'
            
        if self.crear == 'EliminarColeccion':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'new':
                        if self.crear2 == 'EliminarColeccion(“NombreColeccion”)':
                            return 'db.' + self.nombre + '.drop();'
                        else:
                            return 'Error: falta la palabra reservada EliminarColeccion(“NombreColeccion”)'
                    else:
                        return 'Error: Falta la palabra reservada nueva'
                else:
                    return 'Error: Falta el simbolo ='
            else:
                return 'Error: Falta el nombre de la coleccion'
            
        if self.crear == 'InsertarUnico':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'new':
                        if self.crear2 == 'InsertarUnico(“NombreColeccion”)':
                            return 'db.' + self.nombre + '.insertOne(ARCHIVOJSON);'
                        else:
                            return 'Error: falta la palabra reservada InsertarUnico(“NombreColeccion”)'
                    else:
                        return 'Error: Falta la palabra reservada nueva'
                else:
                    return 'Error: Falta el simbolo ='
            else:
                return 'Error: Falta el nombre de la funcion'
            
        if self.crear == 'ActualizarUnico':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'new':
                        if self.crear2 == 'ActualizarUnico(“NombreColeccion”)':
                            return 'db.' + self.nombre + '.updateOne(ARCHIVOJSON);'
                        else:
                            return 'Error: falta la palabra reservada ActualizarUnico(“NombreColeccion”)'
                    else:
                        return 'Error: Falta la palabra reservada nueva'
                else:
                    return 'Error: Falta el simbolo ='
            else:
                return 'Error: Falta el nombre de la funcion'
            
        if self.crear == 'EliminarUnico':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'new':
                        if self.crear2 == 'EliminarUnico(“NombreColeccion”)':
                            return 'db.' + self.nombre + '.deleteOne(ARCHIVOJSON);'
                        else:
                            return 'Error: falta la palabra reservada EliminarUnico(“NombreColeccion”)'
                    else:
                        return 'Error: Falta la palabra reservada nueva'
                else:
                    return 'Error: Falta el simbolo ='
            else:
                return 'Error: Falta el nombre de la funcion'
            
        if self.crear == 'BuscarTodo':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'new':
                        if self.crear2 == 'BuscarTodo(“NombreColeccion”)':
                            return 'db.' + self.nombre + '.find();'
                        else:
                            return 'Error: falta la palabra reservada BuscarTodo(“NombreColeccion”)'
                    else:
                        return 'Error: Falta la palabra reservada nueva'
                else:
                    return 'Error: Falta el simbolo ='
            else:
                return 'Error: Falta el nombre de la funcion'
            
        if self.crear == 'BuscarUnico':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'new':
                        if self.crear2 == 'BuscarUnico(“NombreColeccion”)':
                            return 'db.' + self.nombre + '.findOne();'
                        else:
                            return 'Error: falta la palabra reservada BuscarUnico(“NombreColeccion”)'
                    else:
                        return 'Error: Falta la palabra reservada nueva'
                else:
                    return 'Error: Falta el simbolo ='
            else:
                return 'Error: Falta el nombre de la funcion'
        

        
            
        else:
            return Errores(self.crear,"Sintactico", self.getFila(), self.getColumna())
        


       
        
        

        


    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()
    
    def getPeueba(self):
        return super().getPeueba()