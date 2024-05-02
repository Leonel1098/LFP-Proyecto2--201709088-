from Errores.Errores import *
from Abstract.Abstract import Expression
from Reporte_Errores import reporterror

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
                        return 'Error: Falta la palabra reservada new'
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
                        return 'Error: Falta la palabra reservada new'
                else:
                    return 'Error: Falta el simbolo ='
            else:
                return 'Error: Falta el nombre de la base de datos'
        
        if self.crear == 'CrearColeccion':
            if self.nombre != None:
                if self.igual == '=':
                        if self.nueva == 'new':
                            "=============== AQUI COMIENZA EL ANALISIS DEL NOMBRE DE LA COLECCION ======================"
                            #Mandar a aalizar la cadena 
                            #ver que diga CrearColeccion
                            #CC VARIABLE PARA VERFICAR
                            cc= ""
                            verificarNombre = False

                            nombreColeccion = ''
                            puntero = 0
                        #! leemos self.crear2 y separamaos para poder ver que coisida y so no error 
                            for caracter in self.crear2:
                            
                                if caracter != '(':
                                    cc += caracter
                                    puntero += 1
                                if caracter == '(':
                                    'verificacmos para los errores '
                                    if cc ==  "CrearColeccion":  
                                        break
                                    
                                    else:
                                        return '[ERROR ] FALTA LA PALABRA RESERVADA CrearColeccion'
                                    break
                            'extraemos el nombre de la colleccion'
                            nombreColeccion = self.crear2[puntero:]
                            'se tendria que verificar el orden y que tenga  los () pero no hay teimpo'
                            'se quitan ()'
                            nombreColeccion = nombreColeccion.replace('(','')
                            nombreColeccion = nombreColeccion.replace(')','')
                            #nombreColeccion = nombreColeccion.replace('\"','')
                            return'db.createCollection(' + nombreColeccion + ');'
                        else:
                            return 'Error: Falta la palabra reservada new'
                else:
                    return 'Error: Falta el simbolo ='
            else:
                return 'Error: Falta el nombre de la coleccion'
            
        if self.crear == 'EliminarColeccion':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'new':
                            "=============== AQUI COMIENZA EL ANALISIS DEL NOMBRE DE LA COLECCION ======================"
                                #Mandar a aalizar la cadena 
                                #ver que diga CrearColeccion
                                #CC VARIABLE PARA VERFICAR
                            cc= ""
                            verificarNombre = False

                            nombreColeccion = ''
                            puntero = 0
                        #! leemos self.crear2 y separamaos para poder ver que coisida y so no error 
                            for caracter in self.crear2:
                                
                                    if caracter != '(':
                                        cc += caracter
                                        puntero += 1
                                    if caracter == '(':
                                        'verificacmos para los errores '
                                        if cc ==  "EliminarColeccion":  
                                            break
                                        
                                        else:
                                            return '[ERROR ] FALTA LA PALABRA RESERVADA EliminarColeccion'
                                        break
                            'extraemos el nombre de la coleccion'
                            nombreColeccion = self.crear2[puntero:]
                            'se tendria que verificar el orden y que tenga  los () pero no hay teimpo'                                
                            'se quitan ()'
                            nombreColeccion = nombreColeccion.replace('(','')
                            nombreColeccion = nombreColeccion.replace(')','')
                                #nombreColeccion = nombreColeccion.replace('\"','')
                            return'db.' + nombreColeccion + '.drop();'
                    else:
                        return 'Error: Falta la palabra reservada new'
                else:
                    return 'Error: Falta el simbolo ='
            else:
                return 'Error: Falta el nombre de la coleccion'
            
        if self.crear == 'InsertarUnico':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'new':
                            "=============== AQUI COMIENZA EL ANALISIS DEL NOMBRE DE LA COLECCION ======================"
                                #Mandar a aalizar la cadena 
                                #ver que diga CrearColeccion
                                #CC VARIABLE PARA VERFICAR
                            cc= ""
                            verificarNombre = False

                            nombreColeccion = ''
                            puntero = 0
                        #! leemos self.crear2 y separamaos para poder ver que coisida y so no error 
                            for caracter in self.crear2:
                                
                                    if caracter != '(':
                                        cc += caracter
                                        puntero += 1
                                    if caracter == '(':
                                        'verificacmos para los errores '
                                        if cc ==  "InsertarUnico":  
                                            break
                                        
                                        else:
                                            return '[ERROR ] FALTA LA PALABRA RESERVADA InsertarUnico'
                                        break
                            'extraemos el nombre de la coleccion'
                            nombreColeccion = self.crear2[puntero:]
                            'se tendria que verificar el orden y que tenga  los () pero no hay teimpo' 
                            'se quitan ()'
                            nombreColeccion = nombreColeccion.replace('(','')
                            nombreColeccion = nombreColeccion.replace(')','')
                                #nombreColeccion = nombreColeccion.replace('\"','')
                            return'db.'+ nombreColeccion +'.insertOne();'
                    else:
                        return 'Error: Falta la palabra reservada new'
                else:
                    return 'Error: Falta el simbolo ='
            else:
                return 'Error: Falta el nombre de la funcion'
            
        if self.crear == 'ActualizarUnico':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'new':
                            "=============== AQUI COMIENZA EL ANALISIS DEL NOMBRE DE LA COLECCION ======================"
                                #Mandar a aalizar la cadena 
                                #ver que diga CrearColeccion
                                #CC VARIABLE PARA VERFICAR
                            cc= ""
                            verificarNombre = False

                            nombreColeccion = ''
                            puntero = 0
                        #! leemos self.crear2 y separamaos para poder ver que coisida y so no error 
                            for caracter in self.crear2:
                                
                                    if caracter != '(':
                                        cc += caracter
                                        puntero += 1
                                    if caracter == '(':
                                        'verificacmos para los errores '
                                        if cc ==  "ActualizarUnico":  
                                            break
                                        
                                        else:
                                            return '[ERROR ] FALTA LA PALABRA RESERVADA ActualizarUnico'
                                        break
                            'extraemos el nombre de la coleccion'
                            nombreColeccion = self.crear2[puntero:]
                            'se tendria que verificar el orden y que tenga  los () pero no hay teimpo' 
                            'se quitan ()'
                            nombreColeccion = nombreColeccion.replace('(','')
                            nombreColeccion = nombreColeccion.replace(')','')
                                #nombreColeccion = nombreColeccion.replace('\"','')
                            return'db.'+ nombreColeccion +'.updateOne();'
                    else:
                        return 'Error: Falta la palabra reservada new'
                else:
                    return 'Error: Falta el simbolo ='
            else:
                return 'Error: Falta el nombre de la funcion'
            
        if self.crear == 'EliminarUnico':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'new':
                            "=============== AQUI COMIENZA EL ANALISIS DEL NOMBRE DE LA COLECCION ======================"
                                #Mandar a aalizar la cadena 
                                #ver que diga CrearColeccion
                                #CC VARIABLE PARA VERFICAR
                            cc= ""
                            verificarNombre = False

                            nombreColeccion = ''
                            puntero = 0
                        #! leemos self.crear2 y separamaos para poder ver que coisida y so no error 
                            for caracter in self.crear2:
                                
                                    if caracter != '(':
                                        cc += caracter
                                        puntero += 1
                                    if caracter == '(':
                                        'verificacmos para los errores '
                                        if cc ==  "EliminarUnico":  
                                            break
                                        
                                        else:
                                            return '[ERROR ] FALTA LA PALABRA RESERVADA EliminarUnico'
                                        break
                            'extraemos el nombre de la coleccion'
                            nombreColeccion = self.crear2[puntero:]
                            'se tendria que verificar el orden y que tenga  los () pero no hay tiempo' 
                            'se quitan ()'
                            nombreColeccion = nombreColeccion.replace('(','')
                            nombreColeccion = nombreColeccion.replace(')','')
                                #nombreColeccion = nombreColeccion.replace('\"','')
                            return'db.'+ nombreColeccion +'.deleteOne();'
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
                            "=============== AQUI COMIENZA EL ANALISIS DEL NOMBRE DE LA COLECCION ======================"
                                #Mandar a aalizar la cadena 
                                #ver que diga CrearColeccion
                                #CC VARIABLE PARA VERFICAR
                            cc= ""
                            verificarNombre = False

                            nombreColeccion = ''
                            puntero = 0
                        #! leemos self.crear2 y separamaos para poder ver que coisida y so no error 
                            for caracter in self.crear2:
                                
                                    if caracter != '(':
                                        cc += caracter
                                        puntero += 1
                                    if caracter == '(':
                                        'verificacmos para los errores '
                                        if cc ==  "BuscarTodo":  
                                            break
                                        
                                        else:
                                            return '[ERROR ] FALTA LA PALABRA RESERVADA BuscarTodo'
                                        break
                            'extraemos el nombre de la coleccion'
                            nombreColeccion = self.crear2[puntero:]
                            'se tendria que verificar el orden y que tenga  los () pero no hay tiempo' 
                            'se quitan ()'
                            nombreColeccion = nombreColeccion.replace('(','')
                            nombreColeccion = nombreColeccion.replace(')','')
                                #nombreColeccion = nombreColeccion.replace('\"','')
                            return'db.'+ nombreColeccion +'.find();'
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
                            "=============== AQUI COMIENZA EL ANALISIS DEL NOMBRE DE LA COLECCION ======================"
                                #Mandar a aalizar la cadena 
                                #ver que diga CrearColeccion
                                #CC VARIABLE PARA VERFICAR
                            cc= ""
                            verificarNombre = False

                            nombreColeccion = ''
                            puntero = 0
                        #! leemos self.crear2 y separamaos para poder ver que coisida y so no error 
                            for caracter in self.crear2:
                                
                                    if caracter != '(':
                                        cc += caracter
                                        puntero += 1
                                    if caracter == '(':
                                        'verificacmos para los errores '
                                        if cc ==  "BuscarUnico":  
                                            break
                                        
                                        else:
                                            return '[ERROR ] FALTA LA PALABRA RESERVADA BuscarUnico'
                                        break
                            'extraemos el nombre de la coleccion'
                            nombreColeccion = self.crear2[puntero:]
                            'se tendria que verificar el orden y que tenga  los () pero no hay tiempo' 
                            'se quitan ()'
                            nombreColeccion = nombreColeccion.replace('(','')
                            nombreColeccion = nombreColeccion.replace(')','')
                                #nombreColeccion = nombreColeccion.replace('\"','')
                            return'db.'+ nombreColeccion +'.findOne();'
                    else:
                        return 'Error: Falta la palabra reservada new'
                else:
                    return 'Error: Falta el simbolo ='
            else:
                return 'Error: Falta el nombre de la funcion'
            
        else:
             errores =Errores(self.crear,"Sintactico", self.getFila(), self.getColumna())
             return errores


    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()
    
    def Errores_Sintacticos(self):
        error = Errores()
        print(error)

    def getPeueba(self):
        return super().getPeueba()