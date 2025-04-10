# Para que no se vea error --- NO COPIAR
import re
def validarString(x): 
    return ""
def validarFrase(x): 
    return ""
def menu():
    return ""
#########################################

# X - Tipo de cifrado
def procesarCodXXX(PARAMETROS): # Proceso de Codificación
    """
    Funcionamiento: Codificar una frase con el método de --------------
    Entradas: ------ completar ------
    Salidas: Resultado del proceso  
    """
    # Insertar proceso de CODIFICACIÓN
    return "Mensaje codificado: "
def procesarDecodXXX(PARAMETROS): # Proceso de Decodificación
    """
    Funcionamiento: Decodificar una frase con el método de -------------
    Entradas: ------ (str) dato con el que se trabaja.
    Salidas: Resultado del proceso  
    """
    # Insertar proceso de DECODIFICACIÓN
    return "Mensaje decodificado: "
def validarCodXXX(pValidar):
    """
    Funcionamiento: Validar las entradas para el ejercicio
    Entradas: ---- (str) dato con el que se trabaja.
    Salidas: realimentar al usuario con la corrección de posibles errores o emitir el resultado correcto 
    """
    # Insertar tipo de validación / puede llamar alguna opción de validación anterior de ser necesaria
    if re.match("^[a-z ]+$", pValidar):
        return True
    elif re.match("^[^a-z ]+$", pValidar):   
        print("Debe ingresar solamente valores alphabeticos")
        return False            
    else:
        print("Valor inválido, por favor intentelo nuevamente")
        return False   
def obtenerCodXXX(accion):
    """
    Funcionamiento: Solicita los datos con los que se trabajarán e imprime los resultados
    Entradas: accion (str) acción que se realizará posteriormente 
    Salidas: Continua con el procesamiento respectivo
    """
    print(f"\n_____________________________________________________________\nXXX título del cifrado XXX - ({accion})") 
    frase = input(f"Por favor, ingrese la frase que desea {accion}: ").lower()
    if validarFrase(frase)==False:
        return obtenerCodXXX(accion)
    clave = input("Por favor, ingrese la clave: ").lower()
    if validarString(clave)==False:
        return obtenerCodXXX(accion)
    if accion == "codificar":
        print(procesarCodXXX(frase, clave)) #<-- insertar parametros dentro de los parentesis
        return menu()
    else:
        print(procesarDecodXXX(frase, clave))
        return menu()
