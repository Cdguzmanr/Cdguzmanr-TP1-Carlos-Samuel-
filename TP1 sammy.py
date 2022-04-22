#######################################################
#Creado por: Carlos Guzmán
#Fecha de creación: 4/4/2022 7:00 pm
#Última modificación: 00/00/2022 00:00 am 
#Versión de python: 3.10.2
#######################################################


#Importacion de Librerias
import re

#Validaciones
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
    
def corregirError(string):
    if string == "":  # Valida en caso de no ingresar ningún valor       
        return "No puede ingresar un valor vacío"
    elif string.find(" ") != -1:    # Valida en caso de ingresar espacios en blanco entre los dígitos             
        return "No debe digitar espacios"

#Funciones

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
    return "Mensaje codificado: "+fraseCodificada.lower()
    return "Mensaje decodificado: "
    
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

#Funcionens de menú
def elegirAccion(ejercicio):
    """
    Funcionamiento: Solicita los datos con los que se trabajarán e imprime los resultados
    Entradas: ejercicio (str) nombre del ejercicio al que pertenece la acción, accion (str) acción que desea realizar
    Salidas: resultado del proceso
    """
    accion = input(f"___________________________\n¿Que acción desea realizar? - {ejercicio} \n1- Codificar     2- Decodificar     0- Regresar al menú\n>>> ")
    if validarOpcion(accion, 2):
        if accion == "0":
            return 0
        elif accion == "1":
            return 1
        else:
            return 2
    else:
        return elegirAccion(ejercicio)        

### Menú principal
def menu(): 
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
            control = elegirAccion(ejercicio) #Llama la variable para seleccionar si codifica o decodifica
            if control == 0:
                return menu()
            elif control == 1: #Llama la variable respectiva, e indica el tipo de accion a realizar
                return obtenerCodCesar("codificar")
            else:
                return obtenerCodCesar("decodificar")
        elif opcion == "2": 
            return menu()
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
            return menu()
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
            return menu()
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
            return menu()

#Programa Principal (PP)
print("\n--- Tarea Programada ---\n     Carlos Guzmán \n     Samuel Gárces\n________________________\n")
print(menu())
