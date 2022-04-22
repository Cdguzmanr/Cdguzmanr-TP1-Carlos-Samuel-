#######################################################
#Creado por: Carlos Guzmán, Samuel Garcés
#Fecha de creación: 4/4/2022 7:00 pm
#Última modificación: 22/4/2022 7:55 am 
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
    print(f"\n_____________________________________________________________\nCifrado César - ({accion})") 
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
    print(f"\n_____________________________________________________________\nSustitución Vigenére - ({accion})") 
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
    print(f"\n_____________________________________________________________\nSustitución XOR y llave - ({accion})") 
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
    print(f"\n_____________________________________________________________\nMensaje inverso - ({accion})") 
    frase = input(f"Por favor, ingrese la frase que desea {accion}: ")
    if validarMInverso(frase)==False:
        return obtenerCodMInverso(accion)
    if accion == "codificar":
        print(procesarCodMInverso(frase, "codificado")) 
        return menu()
    else:
        print(procesarCodMInverso(frase, "decodificado"))
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
                return #obtenerCodPInversa("codificar")
            else:
                return #obtenerCodPInversa("decodificar")
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
                return #obtenerCodTelefonico("codificar")
            else:
                return #obtenerCodMTelefonico("decodificar")
        else:
            ejercicio = "Cifrado binario"
            control = elegirAccion(ejercicio)
            if control == 0:
                return menu()
            elif control == 1:
                return #obtenerCodBinario("codificar")
            else:
                return #obtenerCodBinario("decodificar")

# Programa Principal (PP)
print("\n--- Tarea Programada ---\n     Carlos Guzmán \n     Samuel Gárces\n________________________\n") # Encabezado
print(menu())