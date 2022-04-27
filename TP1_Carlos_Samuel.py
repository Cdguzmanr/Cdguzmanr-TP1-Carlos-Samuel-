#######################################################
#Creado por: Carlos Guzmán, Samuel Garcés
#Fecha de creación: 4/4/2022 7:00 pm
#Última modificación: 27/4/2022 10:30 am 
#Versión de python: 3.10.2
#######################################################

# Importación de librerias
import re

# Validación general
def validarString(string): # Valida que solo se ingrese una palabra, con formato de valores alphabéticos 
    """
    Funcionamiento: Validar las entradas afabéticas
    Entradas: string (str) dato a trabajar
    Salidas: (Booleano) realimentar al usuario con la corrección de posibles errores o permitir el avance del proceso.
    """
    if re.match("^[a-zA-Z]+$", string):
        return True
    elif re.match("^[^a-zA-Z]+$", string):   
        print("Debe ingresar solamente valores alphabeticos")
        return False            
    else:
        print("Valor inválido, por favor intentelo nuevamente")
        return False   
def validarFrase(pValidar): # A diferencia de la anterior, esta validación admite espacios en blanco, permitiendo formar frases largas
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
def validarOpcion(opcion, tope): # Esta función permite validar las opciones en un menú de selección numérica
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
def validarNumero(pnum, numeroMinimo): # Permite validar unicamente valores numéricos mayores a un número definido, y con máximo infinito
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
def validarNumero2Digitos(pnum, numeroMinimo, numeroMaximo): # Permite validar valores numéricos mayores a un número definido, y con máximo definido
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

# 1 - Cifrado César
def procesarCodCesar(pfrase): # Proceso de Codificación
    """
    Funcionamiento: Codificar una frase con el método de Cifrado César
    Entradas: pfrase (string) frase a codificar
    Salidas: Resultado del proceso  
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz" # String con el Alfabeto a trabajar
    fraseCodificada, letraFrase= "",0
    while letraFrase < len(pfrase):
        if pfrase[letraFrase] == " ":
            fraseCodificada+= " "
            letraFrase+=1
        if (alfabeto.find(pfrase[letraFrase]) != -1):   # Si se encuentra el valor a trabajar dentro del string,
            fraseCodificada+= alfabeto[alfabeto.find(pfrase[letraFrase])+3] #  se procede a concatenar su valor respectivo
        letraFrase+=1
    return "Mensaje codificado: "+fraseCodificada.upper()
def procesarDecodCesar(pfrase): # Proceso de Decodificación
    """
    Funcionamiento: Decodificar una frase con el método de Cifrado César
    Entradas: pfrase (string) frase a decodificar
    Salidas: Resultado del proceso  
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    fraseCodificada, letraFrase, posicion= "",0,0
    while letraFrase < len(pfrase):
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
        if pfrase[letraFrase] == " ": # De encontrarse, añade el espacio y continúa con la siguiente letra
            fraseCodificada+= " "
            letraFrase+=1
        # Este es el procesamiento principal. 
        resultado = (alfabeto.index(pfrase[letraFrase])+1)+(alfabeto.index(pclave[letraClave])+1) # Suma el valor respectivo a las letras
        if resultado > 26:
            fraseCodificada += (alfabeto[resultado-27]) # Concatena la letra respectiva al valor de la suma anterior
        else:
            fraseCodificada+= (alfabeto[resultado-1])
        # Continúa el avance a traves de la frase y la clave.
        # Esta estructura lógica se repetira en multiples ajercicios a lo largo del código.
        letraClave+=1
        letraFrase+=1        
        if letraFrase == len(pfrase): # Si se ha completado el analisis de toda la frase, se cierra el ciclo
            break
        if letraClave == len(pclave): # Se reinicia el ciclo hasta que se cumpla el requisito anterior
            letraClave = 0
    return "Mensaje codificado: "+fraseCodificada   # Impresión del mensaje
def procesarDecodLlave(pfrase, pclave): # Proceso de Decodificación
    """
    Funcionamiento: Decodificar una frase con el método de llave
    Entradas: pfrase (str) frase a trabajar, pclave (str) clave utilizada
    Salidas: Resultado del proceso  
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz" 
    fraseCodificada, letraClave, letraFrase = "", 0, 0
    while letraClave <= len(pclave)-1:
        if pfrase[letraFrase] == " ":
            fraseCodificada+= " "
            letraFrase+=1
        resultado = (alfabeto.index(pfrase[letraFrase])+1)-(alfabeto.index(pclave[letraClave])+1) # 
        if resultado > 26:
            fraseCodificada += (alfabeto[resultado-27])
        else:
            fraseCodificada+= (alfabeto[resultado-1])
        letraClave+=1
        letraFrase+=1            
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
    frase = input(f"Por favor, ingrese la frase que desea {accion}: ").lower() # En este y demás casos, se trabajan los datos con minúsculas, 
    if validarFrase(frase)==False:                                             # para evitar así inconsistencias a la hora de procesar los datos
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
def procesarCodVigenere(pfrase, pcifra):
    """
    Funcionamiento: Codificar una frase con el método de Sustitución Vigenére
    Entradas: pfrase (str) frase a trabajar, pcifra (str) clave numérica utilizada
    Salidas: Resultado del proceso
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz"  
    fraseCodificada, datoCifra, letraFrase = "", 0, 0
    while datoCifra < len(pcifra):
        if pfrase[letraFrase] == " ":
            fraseCodificada+= " "
            letraFrase+=1
        resultado = (alfabeto.index(pfrase[letraFrase])+1)+(int(pcifra[datoCifra]))
        letraFrase+=1
        datoCifra+=1
        if resultado > 26:
            fraseCodificada += (alfabeto[resultado-27])
        else:
            fraseCodificada+= (alfabeto[resultado-1])
        if letraFrase == len(pfrase): 
            break
        if datoCifra == 2:
            datoCifra = 0
    return "Mensaje codificado: "+fraseCodificada
def procesarDecodVigenere(pfrase, pcifra):
    """
    Funcionamiento: Decodificar una frase con el método de Sustitución Vigenére
    Entradas: pfrase (str) frase a trabajar, pcifra (str) clave numérica utilizada
    Salidas: Resultado del proceso
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz"  # Variable utilizada para definir los valores de las letras
    fraseCodificada, datoCifra, letraFrase = "", 0, 0
    while datoCifra < len(pcifra):
        if pfrase[letraFrase] == " ":
            fraseCodificada+= " "
            letraFrase+=1
        resultado = (alfabeto.index(pfrase[letraFrase])+1)-(int(pcifra[datoCifra]))
        letraFrase+=1
        datoCifra+=1
        if resultado > 26:
            fraseCodificada += (alfabeto[resultado-27])
        else:
            fraseCodificada+= (alfabeto[resultado-1])
        if letraFrase == len(pfrase): # Esto permite finalizar el proceso una vez se termine de analizar toda la frace
            break
        if datoCifra == 2: # Esto permite reiniciar el ciclo cuando se avance a traves de toda la cifra
            datoCifra = 0
    return "Mensaje codificado: "+fraseCodificada
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
        print(procesarCodVigenere(frase, cifra)) 
        return menu()
    else:
        print(procesarDecodVigenere(frase, cifra))
        return menu()

# 4 - Sustitución XOR y llave
def procesarCodXOR(pfrase, pclave): # Proceso de Codificación
    """
    Funcionamiento: Codificar una frase con el método de Sustitución XOR y llave
    Entradas: pfrase (str) frase a trabajar, pclave (str) clave utilizada
    Salidas: Resultado del proceso 
    #__________________________________________________________________________#
    NOTA: Dado a los requisitos extraordinarios solicitados a través de Telegram, 
    se incluyó la función de solicitar la decodificación directamente desde aquí.
    Se deshabilitó la consulta de codificación o decodificación del menu principal.
    """
    fraseCodificada, letraClave, listaValores = "", 0, [] # Definición de variables
    for valor in pfrase:
        fraseCodificada+=''.join(chr(ord(valor)^ord(pclave[letraClave])))
        listaValores+=[chr(ord(valor)^ord(pclave[letraClave]))]
        letraClave+=1
        if letraClave == len(pclave): # Esto permite reiniciar el ciclo cuando se avance a traves de toda la clave
            letraClave = 0        
    print(f"Mensaje codificado: {repr(fraseCodificada)}")   
    if input("\n¿Desea decodificar este mensaje?\n1 -Sí    2 -No\n>>> ") == "1": print(procesarDecodXOR(listaValores, pclave))
    return menu()
def procesarDecodXOR(pfrase, pclave): # Proceso de Decodificación
    """
    Funcionamiento: Decodificar una frase con el método de Sustitución XOR y llave
    Entradas: pfrase (str) frase a trabajar, pclave (str) clave utilizada
    Salidas: Resultado del proceso  
    """
    print(f"\n_____________________________________________________________\nSustitución XOR y llave - (decodificar)\n")    
    print(f"Datos a trabajar: {pfrase}\nClave asignada: {pclave}") # Aquí se indican los valores con los que trabaja la decodificación, como se especifíca en la solicitud extraordinaria de Telegram
    fraseDecodificada, letraClave = "", 0 # Definición de variables
    for valor in pfrase:
        fraseDecodificada+=''.join(chr(ord(valor)^ord(pclave[letraClave])))
        letraClave+=1
        if letraClave >= len(pclave):
            letraClave = 0        
    return f"Mensaje decodificado: {fraseDecodificada}"
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
    print(procesarCodXOR(frase, clave))    
    return menu()
    
# 5 - Palabra inversa
def procesarCodPalabraInver(pfrase, accion):
    """
    Funcionamiento: Codifica y decodifica una frase con el método de Palabra inversa
    Entradas: pfrase (str) frase a trabajar
    Salidas: Resultado del proceso
    #_____________________________#
    Comentario adicional: Este método es muy sencillo, la codificación y decodificación utilizan el mismo proceso.
    Por lo tanto, unicamente se diferenció la impresión del resultado, utilizando el segundo parámetro (accion)        
    """
    palabra,inversa=[],""
    palabra = pfrase[::-1].split(" ")
    i=-1
    for n in range(len(palabra)):
        inversa+= palabra[i]
        inversa+=" "
        i-=1
    return f"Mensaje {accion}: {inversa}"
def obtenerCodPalabraInver(accion):
    """
    Funcionamiento: Solicita los datos con los que se trabajarán e imprime los resultados
    Entradas: accion (str) acción que se realizará posteriormente 
    Salidas: Continua con el procesamiento respectivo
    """
    frase=""
    print(f"\n_____________________________________________________________\nPalabra inversa - ({accion})\n") 
    frase = input(f"Por favor, ingrese la frase que desea {accion}: ")
    if validarFrase(frase)==False:
        return obtenerCodPalabraInver(accion)
    if accion == "codificar":
        print(procesarCodPalabraInver(frase, "codificado")) # El segundo parametro define la acción a realizar, esto para fines de impresión
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
    #_____________________________#
    Comentario adicional: Este método es muy sencillo, la codificación y decodificación utilizan el mismo proceso.
    Por lo tanto, unicamente se diferenció la impresión del resultado, utilizando el segundo parámetro (accion)    
    """
    return f"Mensaje {accion}: {pfrase[::-1]}" # El método [::-1] permite imprimir el valor de la función de atras hacia adelante, saltando en -1
def obtenerCodMInverso(accion):                # O sea, se le da vuelta al valor
    """
    Funcionamiento: Solicita los datos con los que se trabajarán e imprime los resultados
    Entradas: accion (str) acción que se realizará posteriormente 
    Salidas: Continua con el procesamiento respectivo
    """
    print(f"\n_____________________________________________________________\nMensaje inverso - ({accion})\n") 
    frase = input(f"Por favor, ingrese la frase que desea {accion}: ") # En este caso, las mayusculas no influyen en el procesamiento de los datos
    if validarFrase(frase)==False:
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
    Entradas: pfrase (str) frase a trabajar
    Salidas: Resultado del proceso
    """
    resultado=""
    n2,n3,n4,n5,n6,n7,n8,n9 = ["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]
    for letra in pfrase:
        if letra in n2:  # Si la letra se encuentra en la lista referente al "botón telefónico", concatena su valor correspondiente
            resultado+=f"2{n2.index(letra)+1}" 
        elif letra in n3:
            resultado+=f"3{n3.index(letra)+1}"
        elif letra in n4:
            resultado+=f"4{n4.index(letra)+1}"
        elif letra in n5:
            resultado+=f"5{n5.index(letra)+1}"                        
        elif letra in n6:
            resultado+=f"6{n6.index(letra)+1}"             
        elif letra in n7:
            resultado+=f"7{n7.index(letra)+1}"
        elif letra in n8:
            resultado+=f"8{n8.index(letra)+1}"
        elif letra in n9:
            resultado+=f"9{n9.index(letra)+1}"         
        else:
            resultado+="*"
        resultado+=" "       
    return f"Mensaje codificado: {resultado}"
def procesarDecodTel(pfrase):
    """
    Funcionamiento: Codifica y decodifica una frase con el método de Palabra inversa
    Entradas: pfrase (str) frase a trabajar
    Salidas: Resultado del proceso
    """
    n2,n3,n4,n5,n6,n7,n8,n9 = ["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]
    nuevaFrase = ""
    for valor in pfrase:
        digito = valor[0]
        if digito == "*":
            nuevaFrase += ''.join(" ") 
        elif digito == "2":
            nuevaFrase += ''.join(n2[int(valor[1])-1]) # Añade a la frase el valor respectivo al numero que ingresó
        elif digito == "3": 
            nuevaFrase += ''.join(n3[int(valor[1])-1])  # Ejemplo: pfrase = 32
        elif digito == "4":                             # En este caso, ingresó el numero 3 de primero, por lo que se selecciona la lista n3
            nuevaFrase += ''.join(n4[int(valor[1])-1])  # y se integra a la nueva frase el valor numero 2, o sea, una "e".     
        elif digito == "5": 
            nuevaFrase += ''.join(n5[int(valor[1])-1])     
        elif digito == "6":
            nuevaFrase += ''.join(n6[int(valor[1])-1])
        elif digito == "7": 
            nuevaFrase += ''.join(n7[int(valor[1])-1])
        elif digito == "8": 
            nuevaFrase += ''.join(n8[int(valor[1])-1])     
        else: 
            nuevaFrase += ''.join(n9[int(valor[1])-1])               
    return f"Mensaje decodificado: {nuevaFrase}"
def validarDecodTel(pValidar):
    """
    Funcionamiento: Validar las entradas para el ejercicio
    Entradas: pValidar (str) dato con el que se trabaja.
    Salidas: Realimentar al usuario con la corrección de posibles errores o emitir el resultado correcto 
    """
    for digito in pValidar: # Se mueve a traves de la lista y valida sus valores
        if re.match("^[2-9]{1}[0-4]{1}$", digito): # Se asegura que cumpla el formato correcto
            valido = 0 # Esto solo permite que se salga del ciclo en caso de estar correcto, y continúe con el siguiente valor
        elif digito == "*":
            valido = 0
        elif re.match("^[^0-9* ]+$", digito):   
            print("Debe ingresar solamente valores numéricos, espacios o asteriscos")
            return False            
        else:
            print("Valor inválido, por favor intentelo nuevamente")
            return False   
    return True
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
        numeros = frase.split()        
        if validarDecodTel(numeros)==False:
            return obtenerCodTelefono(accion)
        print(procesarDecodTel(numeros))
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
                return obtenerCodXOR("codificar")
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
print("\n----  Tarea Programada  ---\n Carlos Guzmán: 2022437782\n Samuel Gárces: 2022437782\n___________________________\n") # Encabezado
print(menu())