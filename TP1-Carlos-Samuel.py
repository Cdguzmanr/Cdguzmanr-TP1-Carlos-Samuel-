#######################################################
#Creado por: Carlos Guzmán, Samuel Garcés
#Fecha de creación: 4/4/2022 7:00 pm
#Última modificación: 22/4/2022 7:50 am 
#Versión de python: 3.10.2
#######################################################

# Importación de librerias
import re

# Validación general
def validarString(string): # Valida que solo ingrese valores alphabéticos
    """
    Funcionamiento: Validar las entradas afabéticas
    Entradas: string (str) dato a trabajar
    Salidas: (Booleano) realimentar al usuario con la corrección de posibles errores o permitir el avance del proceso.
    """
    if re.match("^[a-z]+$", string):
        return True
    elif re.match("^[^a-z]+$", string):   
        print("Debe ingresar solamente valores alphabeticos")
        return False            
    else:
        print("Valor inválido, por favor intentelo nuevamente")
        return False   

def validarFrase(pValidar):
    """
    Funcionamiento: Validar las entradas para el ejercicio
    Entradas: pstringValidar (str) dato con el que se trabaja.
    Salidas: realimentar al usuario con la corrección de posibles errores o emitir el resultado correcto 
    """
    if re.match("^[a-z ]+$", pValidar):
        return True
    elif re.match("^[^a-z ]+$", pValidar):   
        print("Debe ingresar solamente valores alphabeticos o espacios")
        return False            
    else:
        print("Valor inválido, por favor intentelo nuevamente")
        return False   

def validarOpcion(opcion, tope): 
    """
    Funcionamiento: Validar las entradas del menú
    Entradas: opcion (str) dato a trabajar, tope (int) valor mayor de las opciones seleccionables
    Salidas: (Booleano) realimentar al usuario con la corrección de posibles errores o permitir el avance del proceso.
    """
    if re.match("^\d{1}$", opcion) and int(opcion)>= 0 and int(opcion)<= tope: # Valida que el dato sea de tipo entero, dentro del rango establecido 
        return True
    elif re.match("^\D+$", opcion):
        print("Debe ingresar un valor numérico")
        return False
    else: 
        print("Debe ingresar una opción valida")
        return False        

def validarNumero(pnum, numeroMinimo):
    """
    Funcionamiento: Validar las entradas numericas
    Entradas: pnum (str) número a trabajar, numeroMinimo (int) parametro que define el número minimo con el que desea trabajar
    Salidas: (Booleano) realimentar al usuario con la corrección de posibles errores o permitir el avance del proceso.
    """
    if re.match("^\d+$", pnum): # Opción correcta
        if int(pnum)>=numeroMinimo: 
            return True
        else:
            print("Debe ingresar un número mayor o igual que "+str(numeroMinimo))
            return False
    elif pnum.find(" ") != -1:    # Valida en caso de ingresar espacios en blanco entre los dígitos             
        print ("No debe digitar espacios")
        return False
    elif pnum == "":    # Valida en caso de no ingresar ningún valor                                     
        print("Debe ingresar un valor numérico")
        return False
    elif re.match("^\D+$", pnum): # Valida en caso de ingresar un valor no-numérico
        print("El valor debe de ser un número entero")
        return False
    else: # Valida cualquier otro error
        print("Valor inválido, inténtelo nuevamente")
        return False

def validarNumero2Digitos(pnum, numeroMinimo, numeroMaximo):
    """
    Funcionamiento: Validar las entradas numericas
    Entradas: pnum (str) número a trabajar, numeroMinimo (int) parametro que define el número minimo con el que desea trabajar
    Salidas: (Booleano) realimentar al usuario con la corrección de posibles errores o permitir el avance del proceso.
    """
    if re.match("^\d+$", pnum): # Opción correcta
        if int(pnum)>=numeroMinimo and int(pnum)<=numeroMaximo: 
            return True
        else:
            print("Debe ingresar un número mayor o igual que "+str(numeroMinimo)+" y menor o igual que "+str(numeroMaximo))
            return False
    elif pnum.find(" ") != -1:    # Valida en caso de ingresar espacios en blanco entre los dígitos             
        print ("No debe digitar espacios")
        return False
    elif pnum == "":    # Valida en caso de no ingresar ningún valor                                     
        print("Debe ingresar un valor numérico")
        return False
    elif re.match("^\D+$", pnum): # Valida en caso de ingresar un valor no-numérico
        print("El valor debe de ser un número entero")
        return False
    else: # Valida cualquier otro error
        print("Valor inválido, inténtelo nuevamente")
        return False

    ### Definición de Funciones ###

# Funciones generales
def esPar(digito):
    if digito % 2 == 1:
        return False
    else:
        return True

# 1 - Cifrado César
def procesarCodCesar(pfrase): # Proceso de Codificación
    """
    Funcionamiento: Codificar una frase con el método de Cifrado César
    Entradas: pfrase(string)
    Salidas: Resultado del proceso  
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    fraseCodificada, letraFrase, posicion= "",0,0
    while letraFrase <= len(pfrase)-1:
        if pfrase[letraFrase] == " ":
            fraseCodificada+= " "
            letraFrase+=1
        if (alfabeto.find(pfrase[letraFrase]) != -1):
            posicion = alfabeto.find(pfrase[letraFrase])
            fraseCodificada+= alfabeto[posicion+3]
        letraFrase+=1
    return "Mensaje codificado: "+fraseCodificada.upper()
def procesarDecodCesar(pfrase): # Proceso de Decodificación
    """
    Funcionamiento: Decodificar una frase con el método de Cifrado César
    Entradas: pfrase(string)
    Salidas: Resultado del proceso  
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    fraseCodificada, letraFrase, posicion= "",0,0
    while letraFrase <= len(pfrase)-1:
        if pfrase[letraFrase] == " ":
            fraseCodificada+= " "
            letraFrase+=1
        if (alfabeto.find(pfrase[letraFrase]) != -1):
            posicion = alfabeto.find(pfrase[letraFrase])
            fraseCodificada+= alfabeto[posicion-3]
        letraFrase+=1
    return "Mensaje decodificado: "+fraseCodificada.lower()
def obtenerCodCesar(accion):
    """
    Funcionamiento: Solicita los datos con los que se trabajarán e imprime los resultados
    Entradas: accion (str) acción que se realizará posteriormente 
    Salidas: Continua con el procesamiento respectivo
    """
    print(f"\n_____________________________________________________________\nCifrado César - ({accion})\n") 
    frase = input(f"Por favor, ingrese la frase que desea {accion}: ").lower()
    if validarFrase(frase)==False:
        return obtenerCodCesar(accion)
    if accion == "codificar":
        print(procesarCodCesar(frase)) 
        return menu()
    else:
        print(procesarDecodCesar(frase))
        return menu()

# 2- Cifrado por llave
def procesarCodLlave(pfrase, pclave): # Proceso de Codificación
    """
    Funcionamiento: Codificar una frase con el método de llave
    Entradas: pfrase (str) frase a trabajar, pclave (str) clave utilizada
    Salidas: Resultado del proceso  
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz"  # Variable utilizada para definir los valores de las letras
    fraseCodificada, letraClave, letraFrase = "", 0, 0
    while letraClave <= len(pclave)-1:
        if pfrase[letraFrase] == " ":
            fraseCodificada+= " "
            letraFrase+=1
        resultado = (alfabeto.index(pfrase[letraFrase])+1)+(alfabeto.index(pclave[letraClave])+1)
        letraClave+=1
        letraFrase+=1
        if resultado > 26:
            fraseCodificada += (alfabeto[resultado-27])
        else:
            fraseCodificada+= (alfabeto[resultado-1])
        if letraFrase == len(pfrase):
            break
        if letraClave == len(pclave):
            letraClave = 0
    return "Mensaje codificado: "+fraseCodificada
def procesarDecodLlave(pfrase, pclave): # Proceso de Decodificación
    """
    Funcionamiento: Decodificar una frase con el método de llave
    Entradas: pfrase (str) frase a trabajar, pclave (str) clave utilizada
    Salidas: Resultado del proceso  
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz"  # Variable utilizada para definir los valores de las letras
    fraseCodificada, letraClave, letraFrase = "", 0, 0
    while letraClave <= len(pclave)-1:
        if pfrase[letraFrase] == " ": # Actúa en caso de encontrar un espacio
            fraseCodificada+= " "
            letraFrase+=1
        resultado = (alfabeto.index(pfrase[letraFrase])+1)-(alfabeto.index(pclave[letraClave])+1) # 
        letraClave+=1
        letraFrase+=1
        if resultado > 26:
            fraseCodificada += (alfabeto[resultado-27])
        else:
            fraseCodificada+= (alfabeto[resultado-1])
        if letraFrase == len(pfrase):
            break
        if letraClave == len(pclave):
            letraClave = 0
    return "Mensaje decodificado: "+fraseCodificada
def obtenerCodLlave(accion):
    """
    Funcionamiento: Solicita los datos con los que se trabajarán e imprime los resultados
    Entradas: accion (str) acción que se realizará posteriormente 
    Salidas: Continua con el procesamiento respectivo
    """
    print(f"\n_____________________________________________________________\nCifrado por llave - ({accion})\n") 
    frase = input(f"Por favor, ingrese la frase que desea {accion}: ").lower()
    if validarFrase(frase)==False:
        return obtenerCodLlave(accion)
    clave = input("Por favor, ingrese la clave: ").lower()
    if validarString(clave)==False:
        return obtenerCodLlave(accion)
    if accion == "codificar":
        print(procesarCodLlave(frase, clave))
        return menu()
    else:
        print(procesarDecodLlave(frase, clave))
        return menu()

# 3 - Sustitución Vigenére
def procesarCodVigenere(pfrase):
    """
    Funcionamiento: Codificar una frase con el método de Sustitución Vigenére
    Entradas: pfrase(string)
    Salidas: Resultado del proceso
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    fraseCodificada, letraFrase, posicion, aux= "",0,0,1
    while letraFrase <= len(pfrase)-1:
        if pfrase[letraFrase] == " ":
            fraseCodificada+= " "
            letraFrase+=1
            aux = 1
        posicion = alfabeto.find(pfrase[letraFrase])
        if esPar(aux)==False:
            if (alfabeto.find(pfrase[letraFrase]) != -1):
                fraseCodificada+= alfabeto[posicion+2]
        else:
            if (alfabeto.find(pfrase[letraFrase]) != -1):
                fraseCodificada+= alfabeto[posicion+3]
        letraFrase+=1
        aux+=1
    return "Mensaje codificado: "+fraseCodificada
def procesarDecodVigenere(pfrase):
    """
    Funcionamiento: Decodificar una frase con el método de Sustitución Vigenére
    Entradas: pfrase(string)
    Salidas: Resultado del proceso
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    fraseCodificada, letraFrase, posicion, aux= "",0,0,1
    while letraFrase <= len(pfrase)-1:
        if pfrase[letraFrase] == " ":
            fraseCodificada+= " "
            letraFrase+=1
            aux = 1
        posicion = alfabeto.find(pfrase[letraFrase])
        if esPar(aux)==False:
            if (alfabeto.find(pfrase[letraFrase]) != -1):
                fraseCodificada+= alfabeto[posicion-2]
        else:
            if (alfabeto.find(pfrase[letraFrase]) != -1):
                fraseCodificada+= alfabeto[posicion-3]
        letraFrase+=1
        aux+=1
    return "Mensaje decodificado: "+fraseCodificada
def obtenerCodVigenere(accion):
    """
    Funcionamiento: Solicita los datos con los que se trabajarán e imprime los resultados
    Entradas: accion (str) acción que se realizará posteriormente 
    Salidas: Continua con el procesamiento respectivo
    """
    frase,cifra='',0
    print(f"\n_____________________________________________________________\nSustitución Vigenére - ({accion})\n") 
    frase = input(f"Por favor, ingrese la frase que desea {accion}: ").lower()
    if validarFrase(frase)==False:
        return obtenerCodVigenere(accion)
    cifra = input("Por favor, ingrese la cifra: ")
    if validarNumero2Digitos(cifra,10,99)==False:
        return obtenerCodVigenere(accion)
    if accion == "codificar":
        print(procesarCodVigenere(frase)) 
        return menu()
    else:
        print(procesarDecodVigenere(frase))
        return menu()

# 4 - Sustitución XOR y llave
def procesarCodXOR(pfrase, pclave): # Proceso de Codificación
    """
    Funcionamiento: Codificar una frase con el método de Sustitución XOR y llave
    Entradas: pfrase (str) frase a trabajar, pclave (str) clave utilizada
    Salidas: Resultado del proceso  
    """
    fraseCodificada, letraClave, letraFrase = "", 0, 0 # Definición de variables
    while letraClave < len(pclave):
        valor = chr(ord(pfrase[letraFrase])^ord(pclave[letraClave])) #Define el caracter del XOR entre las letras que se trabajan
        fraseCodificada+=valor 
        letraClave+=1 # Sigue avanzando por las palabras
        letraFrase+=1
        if letraFrase == len(pfrase):
            break
        if letraClave == len(pclave):
            letraClave = 0
    return f"Mensaje codificado: {repr(fraseCodificada)}"
def procesarDecodXOR(pfrase, pclave): # Proceso de Decodificación
    """
    Funcionamiento: Decodificar una frase con el método de Sustitución XOR y llave
    Entradas: pfrase (str) frase a trabajar, pclave (str) clave utilizada
    Salidas: Resultado del proceso  
    """
    # Insertar proceso de DECODIFICACIÓN
    return "Mensaje decodificado: "
def obtenerCodXOR(accion):
    """
    Funcionamiento: Solicita los datos con los que se trabajarán e imprime los resultados
    Entradas: accion (str) acción que se realizará posteriormente 
    Salidas: Continua con el procesamiento respectivo
    """
    print(f"\n_____________________________________________________________\nSustitución XOR y llave - ({accion})\n") 
    frase = input(f"Por favor, ingrese la frase que desea {accion}: ").lower()
    if validarFrase(frase)==False:
        return obtenerCodXOR(accion)
    clave = input("Por favor, ingrese la clave: ").lower()
    if validarString(clave)==False:
        return obtenerCodXOR(accion)
    if accion == "codificar":
        print(procesarCodXOR(frase, clave))
        return menu()
    else:
        print(procesarDecodXOR(frase, clave))
        return menu()

# 5 - Palabra inversa
def procesarCodPalabraInver(pfrase, accion):
    """
    Funcionamiento: Codifica y decodifica una frase con el método de Palabra inversa
    Entradas: pfrase(string)
    Salidas: Resultado del proceso
    """
    palabra,inversa=[],""
    palabra = pfrase[::-1].split(" ")
    i=-1
    for n in range(len(palabra)):
        inversa+= palabra[i]
        inversa+=" "
        i-=1
    return f"Mensaje {accion}: {inversa}"
def validarMInverso(pValidar):
    """
    Funcionamiento: Validar las entradas para el ejercicio
    Entradas: pstringValidar (str) dato con el que se trabaja.
    Salidas: realimentar al usuario con la corrección de posibles errores o emitir el resultado correcto 
    """
    if re.match("^[a-zA-Z ]+$", pValidar):
        return True
    elif re.match("^[^a-zA-Z ]+$", pValidar):   
        print("Debe ingresar solamente valores alphabeticos o espacios")
        return False            
    else:
        print("Valor inválido, por favor intentelo nuevamente")
        return False   
def obtenerCodPalabraInver(accion):
    """
    Funcionamiento: Solicita los datos con los que se trabajarán e imprime los resultados
    Entradas: accion (str) acción que se realizará posteriormente 
    Salidas: Continua con el procesamiento respectivo
    """
    frase=""
    print(f"\n_____________________________________________________________\nPalabra inversa - ({accion})\n") 
    frase = input(f"Por favor, ingrese la frase que desea {accion}: ").lower()
    if validarMInverso(frase)==False:
        return obtenerCodPalabraInver(accion)
    if accion == "codificar":
        print(procesarCodPalabraInver(frase, "codificado"))
        return menu()
    else:
        print(procesarCodPalabraInver(frase, "decodificado"))
        return menu()

# 6 - Mensaje inverso
def procesarCodMInverso(pfrase, accion): # Proceso de Codificación
    """
    Funcionamiento: Codificar una frase con el método de Mensaje inverso
    Entradas: pfrase (str) frase a trabajar, accion (str) acción que se realizará
    Salidas: Resultado del proceso  
    Comentario adicional: Este método es muy sencillo, la codificación y decodificación utilizan el mismo proceso.
    Por lo tanto, unicamente diferencié la impresión del resultado, utilizando el segundo parámetro (accion)    
    """
    return f"Mensaje {accion}: {pfrase[::-1]}"
def validarMInverso(pValidar):
    """
    Funcionamiento: Validar las entradas para el ejercicio
    Entradas: pstringValidar (str) dato con el que se trabaja.
    Salidas: realimentar al usuario con la corrección de posibles errores o emitir el resultado correcto 
    """
    if re.match("^[a-zA-Z ]+$", pValidar):
        return True
    elif re.match("^[^a-zA-Z ]+$", pValidar):   
        print("Debe ingresar solamente valores alphabeticos o espacios")
        return False            
    else:
        print("Valor inválido, por favor intentelo nuevamente")
        return False   
def obtenerCodMInverso(accion):
    """
    Funcionamiento: Solicita los datos con los que se trabajarán e imprime los resultados
    Entradas: accion (str) acción que se realizará posteriormente 
    Salidas: Continua con el procesamiento respectivo
    """
    print(f"\n_____________________________________________________________\nMensaje inverso - ({accion})\n") 
    frase = input(f"Por favor, ingrese la frase que desea {accion}: ")
    if validarMInverso(frase)==False:
        return obtenerCodMInverso(accion)
    if accion == "codificar":
        print(procesarCodMInverso(frase, "codificado")) 
        return menu()
    else:
        print(procesarCodMInverso(frase, "decodificado"))
        return menu()

# 7 - Cifrado por código telefónico
def procesarCodTel(pfrase):
    """
    Funcionamiento: Codifica y decodifica una frase con el método de Palabra inversa
    Entradas: pfrase(string)
    Salidas: Resultado del proceso
    """
    resultado=""
    n1,n2,n3,n4,n5,n6,n7,n8 = ["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]
    for n in pfrase:
        i,m=1,0
        for m in range(3):
            if n == n1[m]:
                resultado+= f"2{i}"
                break
            if n == n2[m]:
                resultado+= f"3{i}"   
                break
            if n == n3[m]:
                resultado+= f"4{i}"
                break
            if n == n4[m]:
                resultado+= f"5{i}"
                break
            if n == n5[m]:
                resultado+= f"6{i}"
                break
            if n == n6[m]:
                resultado+= f"7{i}"
                break
            if n == n7[m]:
                resultado+= f"8{i}"
                break
            if n == n8[m]:
                resultado+= f"9{i}"
            i+=1
        i,m=3,4
        if n == n6[i]:
            resultado+= f"7{i+1}"
        if n == n8[i]:
            resultado+= f"9{i+1}"
        if n == " ":
            resultado+="*"
        resultado+=" "
    return f"Mensaje codificado: {resultado}"
def procesarDecodTel(pfrase):
    """
    Funcionamiento: Codifica y decodifica una frase con el método de Palabra inversa
    Entradas: pfrase(string)
    Salidas: Resultado del proceso
    """
    resultado,i,boton,bandera="",0,"",False
    n1,n2,n3,n4,n5,n6,n7,n8 = ["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]
    for n in pfrase:
        if bandera==True:
            if boton == "*":
                resultado+=" "
            else:
                i=int(n)
            if boton == "2":
                if i==1:
                    resultado+= "a"
                elif i==2:
                    resultado+= "b"
                else:
                    resultado+= "c"
            elif boton == "3":
                if i==1:
                    resultado+= "d"
                elif i==2:
                    resultado+= "e"
                else:
                    resultado+= "f" 
            elif boton == "4":
                if i==1:
                    resultado+= "g"
                elif i==2:
                    resultado+= "h"
                else:
                    resultado+= "i" 
            elif boton == "5":
                if i==1:
                    resultado+= "j"
                elif i==2:
                    resultado+= "k"
                else:
                    resultado+= "l" 
            elif boton == "6":
                if i==1:
                    resultado+= "m"
                elif i==2:
                    resultado+= "n"
                else:
                    resultado+= "o" 
            elif boton == "7":
                if i==1:
                    resultado+= "p"
                elif i==2:
                    resultado+= "q"
                elif i==3:
                    resultado+= "r"
                else:
                    resultado+= "s" 
            elif boton == "8":
                if i==1:
                    resultado+= "t"
                elif i==2:
                    resultado+= "u"
                else:
                    resultado+= "v" 
            elif boton == "9":
                if i==1:
                    resultado+= "w"
                elif i==2:
                    resultado+= "x"
                elif i==3:
                    resultado+= "y"
                else:
                    resultado+= "z" 
            else:
                cosa = 0 # Esto solo permite terminar el proceso y evitar errores
            bandera=False
        if i==0:
            if bandera==False:
                boton=n
            if boton!="" and boton!=" ":
                bandera=True
        i=0
    return f"Mensaje decodificado: {resultado}"
def validarCodTel(pValidar):
    """
    Funcionamiento: Validar las entradas para el ejercicio
    Entradas: pValidar (str) dato con el que se trabaja.
    Salidas: Realimentar al usuario con la corrección de posibles errores o emitir el resultado correcto 
    """
    if re.match("^[0-9* ]+$", pValidar):
        return True
    elif re.match("^[^0-9* ]+$", pValidar):   
        print("Debe ingresar solamente valores numéricos, espacios o asteriscos")
        return False            
    else:
        print("Valor inválido, por favor intentelo nuevamente")
        return False   
def obtenerCodTelefono(accion):
    """
    Funcionamiento: Solicita los datos con los que se trabajarán e imprime los resultados
    Entradas: accion (str) acción que se realizará posteriormente 
    Salidas: Continua con el procesamiento respectivo
    """
    frase=""
    print(f"\n_____________________________________________________________\nCifrado por código telefónico - ({accion})\n") 
    if accion == "codificar":
        frase = input(f"Por favor, ingrese la frase que desea {accion}: ").lower()
        if validarFrase(frase)==False:
            return obtenerCodTelefono(accion)
        print(procesarCodTel(frase))
        return menu()
    else:
        frase = input(f"Por favor, ingrese la frase que desea {accion}: ")
        if validarCodTel(frase)==False:
            return obtenerCodTelefono(accion)
        print(procesarDecodTel(frase))
        return menu()

# 8 - Cifrado binario
def procesarCodBinario(pfrase): # Proceso de Codificación
    """
    Funcionamiento: Codificar una frase con el método de Cifrado binario
    Entradas: pfrase (str) frase a trabajar
    Salidas: Resultado del proceso  
    """
    valorBinario = ["*", "00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111", "01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111", "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111", "11000", "11001" ]
    alfabeto = " abcdefghijklmnopqrstuvwxyz"    
    nuevaFrase = ' '.join((valorBinario[alfabeto.index(letra)]) for letra in pfrase)
    return f"Mensaje codificado: {nuevaFrase}"
def procesarDecodBinario(pfrase): # Proceso de Decodificación
    """
    Funcionamiento: Decodificar una frase con el método de 
    Entradas: pfrase (str) frase a trabajar
    Salidas: Resultado del proceso  
    """
    valorBinario = ["*", "00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111", "01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111", "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111", "11000", "11001" ]
    alfabeto = " abcdefghijklmnopqrstuvwxyz"    
    nuevaFrase = ''.join((alfabeto[valorBinario.index(dato)]) for dato in pfrase)
    return f"Mensaje decodificado: {nuevaFrase}"
def validarCodBinario(pValidar):
    """
    Funcionamiento: Validar las entradas para el ejercicio
    Entradas: pValidar (list) dato con el que se trabaja.
    Salidas: realimentar al usuario con la corrección de posibles errores o emitir el resultado correcto 
    """
    for dato in pValidar:
        if re.match("^[10]{5}$", dato):
            contador = 0 #Esto solo permite que se salga del ciclo y no tenga que avanzar por los otros elif
        elif dato == "*":
            contador = 0
        elif re.match("^[^10]+$", dato):   
            print("Debe ingresar solamente datos binarios o espacios (*)")
            return False            
        else:
            print("Valor inválido, por favor intentelo nuevamente")
            return False   
    return True
def obtenerCodBinario(accion):
    """
    Funcionamiento: Solicita los datos con los que se trabajarán e imprime los resultados
    Entradas: accion (str) acción que se realizará posteriormente 
    Salidas: Continua con el procesamiento respectivo
    """
    print(f"\n_____________________________________________________________\nCifrado binario - ({accion})\n") 
    if accion == "codificar":
        frase = input(f"Por favor, ingrese la frase que desea {accion}: ").lower()
        if validarFrase(frase)==False:
            return obtenerCodBinario(accion)
        print(procesarCodBinario(frase)) #<-- insertar parametros dentro de los parentesis
        return menu()    
    else:
        datos = input(f"Por favor, ingrese la frase que desea {accion}: ").lower()
        frase = datos.split(" ") # Aquí se dividen los datos de la frase en una lista, para facilitar su manipulación
        if validarCodBinario(frase)==False:
            return obtenerCodBinario(accion)
        print(procesarDecodBinario(frase))
        return menu()

# Funcionens de menú
def elegirAccion(ejercicio):
    """
    Funcionamiento: Solicita los datos con los que se trabajarán e imprime los resultados
    Entradas: ejercicio (str) nombre del ejercicio al que pertenece la acción, accion (str) acción que desea realizar
    Salidas: resultado del proceso
    """
    accion = input(f"___________________________\n¿Que acción desea realizar? - {ejercicio} \n1- Codificar     2- Decodificar?     0- Regresar al menú\n>>> ")
    if validarOpcion(accion, 2):
        if accion == "0":
            return 0
        elif accion == "1":
            return 1
        else:
            return 2
    else:
        return elegirAccion(ejercicio)        

def menu(): ### Menú principal
    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario. 
    Entradas: opcion (int) opcion del menú
    Salidas: Resultado según lo solicitado
    """
    print ("\n**************************")
    print ("*      Criptografía      *")
    print ("**************************")
    print ("1. Cifrado César ")
    print ("2. Cifrado por llave ")
    print ("3. Sustitución Vigenére ")
    print ("4. Sustitución XOR y llave ")
    print ("5. Palabra inversa ") 
    print ("6. Mensaje inverso ")
    print ("7. Cifrado telefónico ")
    print ("8. Cifrado binario ")   
    print ("0. Terminar")
    try:
        opcion = input("Seleccione una opción: ")
        if validarOpcion(opcion, 8)==False:  # Validación de las opciones
            return menu()
        elif opcion == "0":  # Finaliza el proceso
            return "\n---Ejecución finalizada---"
        else:   # Selecciona opciones del menú
            if opcion == "1":
                ejercicio = "Cifrado César"
                control = elegirAccion(ejercicio) # llama la variable para seleccionar si codifica o decodifica
                if control == 0:
                    return menu()
                elif control == 1: # Llama la variable respectiva, e indica el tipo de accion a realizar
                    return obtenerCodCesar("codificar")
                else:
                    return obtenerCodCesar("decodificar")
            elif opcion == "2": 
                ejercicio = "Cifrado por llave"
                control = elegirAccion(ejercicio)
                if control == 0:
                    return menu()
                elif control == 1:
                    return obtenerCodLlave("codificar")
                else:
                    return obtenerCodLlave("decodificar")
            elif opcion == "3":
                ejercicio = "Sustitución Vigenére"
                control = elegirAccion(ejercicio)
                if control == 0:
                    return menu()
                elif control == 1:
                    return obtenerCodVigenere("codificar")
                else:
                    return obtenerCodVigenere("decodificar")
            elif opcion == "4":
                ejercicio = "Sustitución XOR y llave"
                control = elegirAccion(ejercicio)
                if control == 0:
                    return menu()
                elif control == 1:
                    return obtenerCodXOR("codificar")
                else:
                    return obtenerCodXOR("decodificar")
            elif opcion == "5":
                ejercicio = "Palabra inversa"
                control = elegirAccion(ejercicio)
                if control == 0:
                    return menu()
                elif control == 1:
                    return obtenerCodPalabraInver("codificar")
                else:
                    return obtenerCodPalabraInver("decodificar")
            elif opcion == "6":
                ejercicio = "Mensaje inverso"
                control = elegirAccion(ejercicio)
                if control == 0:
                    return menu()
                elif control == 1:
                    return obtenerCodMInverso("codificar")
                else:
                    return obtenerCodMInverso("decodificar")
            elif opcion == "7":
                ejercicio = "Cifrado telefónico"
                control = elegirAccion(ejercicio)
                if control == 0:
                    return menu()
                elif control == 1:
                    return obtenerCodTelefono("codificar")
                else:
                    return obtenerCodTelefono("decodificar")
            else:
                ejercicio = "Cifrado binario"
                control = elegirAccion(ejercicio)
                if control == 0:
                    return menu()
                elif control == 1:
                    return obtenerCodBinario("codificar")
                else:
                    return obtenerCodBinario("decodificar")
    except:
        print("\n>>> Ocurrió un error, vuelva a intentarlo") # Atrapa y corrije en caso de recibir un error desconocido
        return menu()


# Programa Principal (PP)
print("\n--- Tarea Programada ---\n     Carlos Guzmán \n     Samuel Gárces\n________________________\n") # Encabezado
print(menu())
