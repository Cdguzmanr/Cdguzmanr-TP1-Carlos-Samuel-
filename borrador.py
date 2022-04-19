
# input
pfrase = "tarea"
pclave = "secreto"

# ASCII
fraseASCII = ord("t")
claveASCII = ord("s")

# binario
fraseBinario = bin(ord(pfrase[0])) # 0b1110100
claveBinario = bin(ord("s"))

# Proceso para 
vXOR = ""
for i in range(2, len(pfrase)):
    if fraseBinario[i] == claveBinario[i]:
        vXOR += "1"
    else:
        vXOR += "0"
print(int(vXOR, 2))


###########################################################################

# Input
pfrase = "tarea"
pclave = "secreto"

fraseCodificada, letraClave, letraFrase, vXOR = "", 0, 0, "" # Definición de variables
while letraClave <= len(pclave)-1:
    fraseBinario = bin(ord(pfrase[letraFrase])) # Definen los valores binarios de la respectiva letra
    claveBinario = bin(ord(pclave[letraClave]))
    # Proceso de codificación XOR de los valores binarios
    for i in range(2, len(pfrase)):
        if fraseBinario[i] == claveBinario[i]:
            vXOR += "1"
        else:
            vXOR += "0"
    fraseCodificada+=chr(int(vXOR, 2))    
    # Sigue avanzando por las palabras    
    letraClave+=1
    letraFrase+=1
    if letraFrase == len(pfrase):
        break
    if letraClave == len(pclave):
        letraClave = 0
print("Mensaje codificado: "+fraseCodificada)


#int("0b1110100", 2)

#print(fraseBinario)

# fraseBinario = bin(pfrase)
# print(fraseBinario)
# for i in range(9):
#     print(f"{i} --> {chr(i)}")









############# IMPORTANTE - DECODIFICAR ##############
# ord() es el contrario de chr()
