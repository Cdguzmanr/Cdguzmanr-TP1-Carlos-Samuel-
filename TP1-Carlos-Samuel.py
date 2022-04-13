#######################################################
#Creado por: Carlos Guzmán, Samuel Garcés
#Fecha de creación: 4/4/2022 7:00 pm
#Última modificación: 00/00/2022 00:00 am 
#Versión de python: 3.10.2
#######################################################

# Importación de librerias
import re

# Validación general
def corregirError(string):
    """
    Funcionamiento: Validar las entradas generales de los datos
    Entradas: string (str) dato a trabajar 
    Salidas: (Booleano) realimentar al usuario con la corrección de posibles errores o permitir el avance del proceso.
    """
    if string == "":  # Valida en caso de no ingresar ningún valor       
        return "No puede ingresar un valor vacío"
    elif string.find(" ") != -1:    # Valida en caso de ingresar espacios en blanco entre los dígitos             
        return "No debe digitar espacios"

def corregirString(string): # Valida que solo ingrese valores alphabéticos
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

def corregirOpcion(opcion, tope): 
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

def validarGeneral(pnum, numeroMinimo):
    """
    Funcionamiento: Validar las entradas numericas
    Entradas: pnum (str) número a trabajar, numeroMinimo (int) parametro que define el número minimo con el que desea trabajar
    Salidas: (Booleano) realimentar al usuario con la corrección de posibles errores o permitir el avance del proceso.
    """
    if pnum.find(" ") != -1:    # Valida en caso de ingresar espacios en blanco entre los dígitos             
        print ("No debe digitar espacios")
        return False
    elif pnum == "":    # Valida en caso de no ingresar ningún valor                                     
        print("Debe ingresar un valor numérico")
        return False
    try:
        pnum = int(pnum) #Aquí se transforma el número ingresado (str) a un valor entero (int) para su validación numérica
        if isinstance(pnum,int):
            if pnum > numeroMinimo: # Valida que sea mayor que el número mínimo solicitado
                return True
            else: 
                print("Debe ingresar un número mayor a "+str(numeroMinimo))
                return False
        else:
            print("El valor debe de ser un número entero")
            return False   
    except ValueError: # Valida en caso de que el número ingresado no sea un entero (int)
        print("El valor debe de ser un número entero")
        return False

    ### Definición de Funciones ###

# 2- Cifrado por llave
# En eso estoy <3 


# Funcionens de menú
def elegirAccion(ejercicio):
    """
    Funcionamiento: Solicita los datos con los que se trabajarán e imprime los resultados
    Entradas: ejercicio (str) nombre del ejercicio al que pertenece la acción, accion (str) acción que desea realizar
    Salidas: resultado del proceso
    """
    accion = input("___________________________\n¿Que acción desea realizar? - "+ejercicio+" \n1- Codificar     2- Decodificar?     0- Regresar al menú\n>>> ")
    if corregirOpcion(accion, 2):
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
    if corregirOpcion(opcion, 8)==False:  # Validación de las opciones
        return menu()
    elif opcion == "0":  # Finaliza el proceso
        return "\n---Ejecución finalizada---"
    else:   # Selecciona opciones del menú
        if opcion == "1":
            ejercicio = "Cifrado César"
            control = elegirAccion(ejercicio)
            if control == 0:
                return menu()
            elif control == 1:
                return "obtenerCodCesar()"
            else:
                return "obtenerDecodCesar()"
        elif opcion == "2": 
            ejercicio = "Cifrado por llave"
            control = elegirAccion(ejercicio)
            if control == 0:
                return menu()
            elif control == 1:
                return "obtenerCodLlave()"
            else:
                return "obtenerDecodLlave()"
        elif opcion == "3":
            ejercicio = "Sustitución Vigenére"
            control = elegirAccion(ejercicio)
            if control == 0:
                return menu()
            elif control == 1:
                return "obtenerCodVigenere()"
            else:
                return "obtenerDecodVigenere()"
        elif opcion == "4":
            ejercicio = "Sustitución XOR y llave"
            control = elegirAccion(ejercicio)
            if control == 0:
                return menu()
            elif control == 1:
                return "obtenerCodXOR()"
            else:
                return "obtenerDecodXOR()"
        elif opcion == "5":
            ejercicio = "Palabra inversa"
            control = elegirAccion(ejercicio)
            if control == 0:
                return menu()
            elif control == 1:
                return "obtenerCodPInversa()"
            else:
                return "obtenerDecodPInversa()"
        elif opcion == "6":
            ejercicio = "Mensaje inverso"
            control = elegirAccion(ejercicio)
            if control == 0:
                return menu()
            elif control == 1:
                return "obtenerCodMInverso()"
            else:
                return "obtenerDecodMInverso()"
        elif opcion == "7":
            ejercicio = "Cifrado telefónico"
            control = elegirAccion(ejercicio)
            if control == 0:
                return menu()
            elif control == 1:
                return "obtenerCodTelefonico()"
            else:
                return "obtenerDecodMTelefonico()"
        else:
            ejercicio = "Cifrado binario"
            control = elegirAccion(ejercicio)
            if control == 0:
                return menu()
            elif control == 1:
                return "obtenerCodBinario()"
            else:
                return "obtenerDecodBinario()"

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