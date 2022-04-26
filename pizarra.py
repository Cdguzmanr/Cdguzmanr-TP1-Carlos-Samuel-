#print(chr(ord("\x07")^ord("s")))

valor = "'T'"
#print(valor[1:-1])


def procesarDecodXOR(pfrase, pclave): # Proceso de Decodificación
    """
    Funcionamiento: Decodificar una frase con el método de Sustitución XOR y llave
    Entradas: pfrase (str) frase a trabajar, pclave (str) clave utilizada
    Salidas: Resultado del proceso  
    """
    fraseDecodificada, letraClave = "", 0 # Definición de variables
    for valor in pfrase:
        fraseDecodificada+=''.join(chr(ord(valor)^ord(pclave[letraClave])))
        letraClave+=1
        if letraClave >= len(pclave):
            letraClave = 0        
    return f"Mensaje decodificado: {fraseDecodificada}"
#print(procesarDecodXOR(['\x07', '\x04', '\x11', '\x17', '\x04', 'T', '\x1f', '\x01', '\n', '\x04', '\x00', '\x04', '\x19', '\x0e', '\x17', '\x04'], "secreto"))

def procesarDecodXOR2(pfrase, pclave): # Proceso de Codificación
    """
    Funcionamiento: Codificar una frase con el método de Sustitución XOR y llave
    Entradas: pfrase (str) frase a trabajar, pclave (str) clave utilizada
    Salidas: Resultado del proceso  
    """
    print(pfrase)
    fraseDecodificada, letraClave = "", 0 # Definición de variables
    for datos in pfrase:
        valor = datos[1:-1]
        print(valor)
        fraseDecodificada+=''.join(chr(ord(valor)^ord(pclave[letraClave])))
        letraClave+=1
        if letraClave >= len(pclave):
            letraClave = 0        
    return f"Mensaje decodificado: {fraseDecodificada}" 


#___________________________________________
def procesarDecodXOR(pfrase, pclave): # Proceso de Decodificación
    """
    Funcionamiento: Decodificar una frase con el método de Sustitución XOR y llave
    Entradas: pfrase (str) frase a trabajar, pclave (str) clave utilizada
    Salidas: Resultado del proceso  
    """
    fraseDecodificada, letraClave = "", 0 # Definición de variables
    for valor in pfrase:
        #print(repr(valor))
        fraseDecodificada+=''.join(chr(ord(valor)^ord(pclave[letraClave])))
        letraClave+=1
        if letraClave >= len(pclave):
            letraClave = 0        
    return f"Mensaje decodificado: {fraseDecodificada}"
#print(procesarDecodXOR(['\x07', '\x04', '\x11', '\x17', '\x04', 'T', '\x1f', '\x01', '\n', '\x04', '\x00', '\x04', '\x19', '\x0e', '\x17', '\x04'], "secreto"))

def procesarCodXOR(pfrase, pclave): # Proceso de Codificación
    """
    Funcionamiento: Codificar una frase con el método de Sustitución XOR y llave
    Entradas: pfrase (str) frase a trabajar, pclave (str) clave utilizada
    Salidas: Resultado del proceso  
    """
    fraseCodificada, letraClave, listaValores = "", 0, [] # Definición de variables
    for valor in pfrase:
        fraseCodificada+=''.join(chr(ord(valor)^ord(pclave[letraClave])))
        listaValores+=[chr(ord(valor)^ord(pclave[letraClave]))]
        letraClave+=1
        if letraClave == len(pclave):
            letraClave = 0        
    print(f"Mensaje decodificado: {repr(fraseCodificada)}")
    print(repr(listaValores))
    if input("¿Desea decodificar este mensaje?\n1 -Sí    2 -No\n>>> ") == "1": return print(procesarDecodXOR(listaValores, pclave))
    return ""
        
print(procesarCodXOR("tarea programada", "secreto"))