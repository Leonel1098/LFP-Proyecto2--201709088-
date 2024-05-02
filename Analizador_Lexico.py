from Token import Token
from Errores.Errores import *
from Reporte_Token import reportoken
from Reporte_Errores import reporterror
import re


class Analizador_lexico:


    def __init__(self):
        self.listTokens = []
        self.listError = []
        self.listReservadas = []
        self.listValores = []
        self.elementos = {}
    def analizador(self,entry):
        #Reiniciar listas para que en cada análisis se reinicie y poder analizar sin reiniciar el programa
        self.listTokens = []
        self.listError = []
        self.listReservadas = []
        valor = ""
        clave = ""
        buffer = ""
        Titulo = ""
        centinela = "$"
        entry += centinela
        self.elementos = {} 
        self.argsDeElementos ={}
        linea = 1
        columna = 1

        estado = 0

        index = 0
        
        while index < len(entry):
            caracter = entry[index]

            if estado == 0:
                #Reconociendo los signos 
                if caracter == ":":
                    #Se suma uno a la columna
                    columna += 1
                    #Se agrega el caracter al buffer 
                    buffer += caracter
                    #Se crea y agrega el token a la lista de tokens
                    token = Token("DOS PUNTOS", buffer,linea, columna)
                    self.listTokens.append(token)
                    #Se limpia el buffer
                    buffer = ""
                    #Se cambia de estado 
                    estado = 0
                
                elif caracter == "{":
                    columna +=1
                    buffer += caracter
                    token = Token("LLAVE QUE ABRE", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0
                    

                elif caracter == "}":
                    columna +=1
                    buffer += caracter
                    token = Token("LLAVE QUE CIERRA", buffer, linea, columna)
                    self.listTokens.append(token)
                    self.elementos[Titulo] = self.argsDeElementos
                    self.argsDeElementos = {}
                    #print("=================Elemento ==================")
                    #print(self.elementos)
                    #print("================= ==================")
                  
                    Titulo =""
                    buffer = ""
                    estado = 0
                
                elif caracter == "\"":
                    columna +=1
                    buffer += caracter
                    token = Token("COMILLA DOBLE", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0
                
                elif caracter == ">":
                    columna +=1
                    buffer += caracter
                    token = Token("MAYOR QUE", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0

                elif caracter == "<":
                    columna +=1
                    buffer += caracter
                    token = Token("MENOR QUE", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0

                elif caracter == "/":
                    columna +=1
                    buffer += caracter
                    token = Token("BARRA", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0

                elif caracter == "-":
                    columna +=1
                    buffer += caracter
                    token = Token("GUION", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0

                elif caracter == "*":
                    columna +=1
                    buffer += caracter
                    token = Token("ASTERISCO", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0
                
                elif caracter == "'":
                    columna +=1
                    buffer += caracter
                    token = Token("COMILLA SIMPLE", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0

                elif caracter == "!":
                    columna +=1
                    buffer += caracter
                    token = Token("ADMIRACION CIERRA", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0

                elif caracter == "+":
                    columna +=1
                    buffer += caracter
                    token = Token("SUMA", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0

                elif caracter == ";":
                    columna +=1
                    buffer += caracter
                    token = Token("PUNTO Y COMA", buffer, linea, columna)
                    self.listTokens.append(token)
                    self.argsDeElementos[clave] = valor
                    
                    valor = ""
                    clave = ""

                    buffer = ""
                    estado = 0

                elif caracter == ",":
                    columna +=1
                    buffer += caracter
                    token = Token("COMA", buffer, linea, columna)
                    self.listTokens.append(token)
                    

                    buffer = ""
                    estado = 0
                
                elif caracter == "[":
                    columna +=1
                    buffer += caracter
                    token = Token("CORCHETE ABRE", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0
                    
                elif caracter == "]":
                    columna +=1
                    buffer += caracter
                    token = Token("CORCHETE CIERRA", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0
                
                elif caracter == "(":
                    columna +=1
                    buffer += caracter
                    token = Token("PARENTESIS ABRE", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0

                elif caracter == ")":
                    columna +=1
                    buffer += caracter
                    token = Token("PARENTESIS CIERRA", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0

                elif caracter == "=":
                    columna +=1
                    buffer += caracter
                    token = Token("IGUAL", buffer, linea, columna)
                    self.listTokens.append(token)
                    

                    buffer = ""
                    estado = 0
                
                elif caracter == ".":
                    columna +=1
                    buffer += caracter
                    token = Token("PUNTO", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0

                elif caracter == "\n":
                    columna = 1
                    linea += 1
                    estado = 0 

                elif caracter == " ":
                    columna +=1
                    buffer += caracter
                elif caracter == "\t":
                    columna += 1
                
                elif re.search(r"[a-zA-Z0-9]", caracter):
                    columna +=1
                    buffer += caracter
                    estado = 1
                
                else: 
                    estado = 3
                    buffer += caracter
            
            #Palabras Reservadas
            elif estado == 1:
                if re.search(r"[a-zA-ZÁ\u00f1\u00d1\u00E0-\u00FC]",caracter) or caracter == "":
                    if caracter == " ":
                        columna += 1
                        estado = 1
                    elif caracter == "\ñ":
                        columna += 1
                        estado = 1
                    elif caracter == "\t":
                        columna +=1

                    elif caracter == "\n":
                        linea +=1
                        columna = 1

                    else: 
                        buffer += caracter
                        estado = 1
                else:
                    Tokentipo = ""

                    if buffer == "CrearBD":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                    
                    elif buffer == "EliminarBD":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        Titulo = buffer
                    
                    elif buffer == "CrearColeccion":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        clave = buffer
                    
                    elif buffer == "EliminarColeccion":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        Titulo = buffer
                    
                    elif buffer =="InsertarUnico":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        Titulo = buffer

                    elif buffer == "ActualizarUnico":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        clave = buffer
                    
                    elif buffer == "EliminarUnico":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        clave = buffer
                    
                    elif buffer == "BuscarTodo":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        clave = buffer
                    
                    elif buffer == "BuscarUnico":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        clave = buffer

                    elif buffer == "nueva":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        Titulo = buffer
                        
                    else:
                        Tokentipo = "IDENTIFICADOR"
                        valor +=  buffer

                    token = Token(Tokentipo,buffer,linea,columna)
                    self.listTokens.append(token)
                    
                    buffer = ""
                    index -= 1
                    estado = 0

            elif estado == 2:
                if re.search(r"[a-zA-Z]",caracter) or re.search(r"[\"]",caracter) or caracter == ' ' or caracter == '-' or caracter == '\t' or caracter  == '\n' or re.search(r"[\:]",caracter):

                    if caracter == "\t":
                        columna += 1

                    elif caracter == "\n":
                        linea += 1
                        columna = 1

                    elif re.search(r"[\:]",caracter):
                        columna += 1
                        buffer += caracter
                        estado = 2
                    
                    elif caracter == '"':
                        token = Token("IDENTIFICADOR", buffer,linea,columna)
                        self.listTokens.append(token)
                        self.listValores.append(buffer)

                        token2 = Token("COMILLA DOBLE",caracter,linea,columna)
                        self.listTokens.append(token2)
                        estado = 2
                        buffer = ""
                    
                    else: 
                        columna += 1
                        estado = 2
                        buffer += caracter
                else:
                    estado = 0 
                    index -= 1

            elif estado == 3:
                errores = Errores("ERROR LEXICO", buffer,linea,columna)
                self.listError.append(errores)
                buffer = ""
                estado = 0
                columna += 1
                index -= 1
            index += 1
       

        return entry
    
    def ErrorToken(self):
        reportoken(self.listTokens)

    def ErrorReporte(self):
        reporterror(self.listError)
    


    def imprimirInfo(self):
        print("\n\n\n")
        print("======= Lista de Tokens =======")
        
        for token in self.listTokens:
            token.getInfo()

    def imprimirErrores(self):
        print("\n\n\n")
        print("======= Lista de Errores =======")
        
        i = 0
        for errores in self.listError:
            print(i+1)
            errores.getError()
            i += 1

