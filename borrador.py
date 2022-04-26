# 3 - Vigenére
def procesarCodVigenere(pfrase, pcifra):
    """
    Funcionamiento: Codificar una frase con el método de Sustitución Vigenére
    Entradas: pfrase(string)
    Salidas: Resultado del proceso
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz"  # Variable utilizada para definir los valores de las letras
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
        if datoCifra == len(pcifra):
            datoCifra = 0
    return "Mensaje codificado: "+fraseCodificada
def procesarDecodVigenere(pfrase, pcifra):
    """
    Funcionamiento: Decodificar una frase con el método de Sustitución Vigenére
    Entradas: pfrase(string)
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
        if letraFrase == len(pfrase):
            break
        if datoCifra == len(pcifra):
            datoCifra = 0
    return "Mensaje codificado: "+fraseCodificada
#print(procesarCodVigenere("tarea programada", "23"))
print(procesarDecodVigenere("vdthc striucpcgc", "23"))

#______________________________________________#
def procesarCodLlave(pfrase, pcifra): # Proceso de Codificación
    """
    Funcionamiento: Codificar una frase con el método de llave
    Entradas: pfrase (str) frase a trabajar, pclave (str) clave utilizada
    Salidas: Resultado del proceso  
    """

    alfabeto = "abcdefghijklmnopqrstuvwxyz"  # Variable utilizada para definir los valores de las letras
    fraseCodificada, datoCifra, letraFrase = "", 0, 0
    while datoCifra < len(pcifra):
        if pfrase[letraFrase] == " ":
            fraseCodificada+= " "
            letraFrase+=1
        resultado = (alfabeto.index(pfrase[letraFrase])+1)+(pcifra[datoCifra])
        letraFrase+=1
        datoCifra+=1
        if resultado > 26:
            fraseCodificada += (alfabeto[resultado-27])
        else:
            fraseCodificada+= (alfabeto[resultado-1])
        if letraFrase == len(pfrase):
            break
        if datoCifra == len(pcifra):
            datoCifra = 0
    return "Mensaje codificado: "+fraseCodificada