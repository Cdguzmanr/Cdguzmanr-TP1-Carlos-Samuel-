#print(chr(ord("\x07")^ord("s")))
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

def procesarCodTel(pfrase):
    """
    Funcionamiento: Codifica y decodifica una frase con el método de Palabra inversa
    Entradas: pfrase(string)
    Salidas: Resultado del proceso
    """
    resultado=""
    n2,n3,n4,n5,n6,n7,n8,n9 = ["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]
    for letra in pfrase:
        if letra in n2:
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
print(procesarCodTel("hola mundo"))