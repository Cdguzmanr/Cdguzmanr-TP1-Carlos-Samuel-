#######################################################
#Creado por: Carlos Guzmán, Samuel Garcés
#Fecha de creación: 4/4/2022 7:00 pm
#Última modificación: 18/4/2022 7:10 am 
#Versión de python: 3.10.2
#######################################################

#Ya lo logre :) ntp Carlos

# Importación de librerias
import re

# Funciones de validación general   <-- Serán utilizadas repetidamente a lo largo del código
def validarString(string): # Valida que solo ingrese valores alphabéticos
    """
    Funcionamiento: Validar las entradas afabéticas
    Entradas: string (str) dato a trabajar
    Salidas: (Booleano) realimentar al usuario con la corrección de posibles errores o permitir el avance del proceso.
    """
    if re.match("^[a-z]+$", string): # Valida el ingreso solo de palabras en letras minúsculas
        return True   
    elif re.match("^[^a-z]+$", string):   
        print("Debe ingresar solamente valores alphabeticos")
        return False       
    elif string.count(" ")!=0:
        print("No debe digitar espacios")    
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
    if re.match("^[a-z ]+$", pValidar): # Dado que se valida ua frase, se permite el ingreso solo de letras (minúsculas) y espacios
        return True
    elif re.match("^[A-Z]+$", pValidar):   
        print("Debe ingresar solamente letras minúsculas")
        return False      
    elif re.match("^[^a-zA-Z ]+$", pValidar):   
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

    ### Definición de Funciones ###

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

# 4 - Sustitución XOR y llave
def procesarCodXOR(pfrase, pclave): # Proceso de Codificación
    """
    Funcionamiento: Codificar una frase con el método de Sustitución XOR y llave
    Entradas: pfrase (str) frase a trabajar, pclave (str) clave utilizada
    Salidas: Resultado del proceso  
    """
    fraseCodificada, letraClave, letraFrase = "", 0, 0 # Definición de variables
    while letraClave < len(pclave):
        valor = chr(ord(pfrase[letraFrase])^ord(pclave[letraClave])) # se define el caracter, del valor ordenado del XOR entre las letras en curso
        fraseCodificada+=valor
        letraClave+=1
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
def validarDecodXOR(pValidar):
    """
    Funcionamiento: Validar las entradas para el ejercicio
    Entradas: ---- (str) dato con el que se trabaja.
    Salidas: realimentar al usuario con la corrección de posibles errores o emitir el resultado correcto 
    """
    if pValidar!="":
        return True     
    if  re.match("^[A-Z]+$", pValidar):   
        print("Debe ingresar solamente valores alphabeticos")
        return False       
    else:
        print("No puede dejar espacios en blanco")
        return False   
def obtenerCodXOR(accion):
    """
    Funcionamiento: Solicita los datos con los que se trabajarán e imprime los resultados
    Entradas: accion (str) acción que se realizará posteriormente 
    Salidas: Continua con el procesamiento respectivo
    """
    print(f"\n_____________________________________________________________\nSustitución XOR y llave - ({accion})") 
    if accion == "codificar":
        frase = input(f"Por favor, ingrese la frase que desea {accion}: ").lower()
        if validarFrase(frase)==False:
            return obtenerCodXOR(accion)
        clave = input("Por favor, ingrese la clave: ").lower()
        if validarString(clave)==False:
            return obtenerCodXOR(accion)        
        print(procesarCodXOR(frase, clave))
        return menu()
    else:
        frase = input(f"Por favor, ingrese la frase que desea {accion}: ")
        if validarDecodXOR(frase)==False:
            return obtenerCodXOR(accion)
        clave = input("Por favor, ingrese la clave: ").lower()
        if validarString(clave)==False:
            return obtenerCodXOR(accion)        
        print(procesarDecodXOR(frase, clave))
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
                return #obtenerCodCesar("codificar")
            else:
                return #obtenerCodCesar("decodificar")
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
                return #obtenerCodVigenere("codificar")
            else:
                return #obtenerDecodVigenere("decodificar")
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
                return #obtenerCodMInverso("codificar")
            else:
                return #obtenerCodMInverso("decodificar")
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
print("\n--- Tarea Programada ---\n     Carlos Guzmán \n     Samuel Gárces\n________________________\n")
print(menu())
# print(menu())
# print(menu())
# print(menu())
# print(menu())
# print(menu())
# print(menu())
# print(menu())
# print(menu())