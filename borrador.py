
def f7(list):
    variable = map(repr,list)
    return ''.join(ord(variable))

#print(f7([r'\x07',r'\x04',r'\x11',r'\x17',r'\x04',r'T',r'\x1f',r'\x01',r'\n',r'\x04',r'\x00',r'\x04',r'\x19',r'\x0e',r'\x17',r'\x04']))
####################################

def procesarCodXOR(pfrase, pclave): # Proceso de Codificación
    """
    Funcionamiento: Codificar una frase con el método de Sustitución XOR y llave
    Entradas: pfrase (str) frase a trabajar, pclave (str) clave utilizada
    Salidas: Resultado del proceso  
    """
    fraseCodificada, letraClave, letraFrase = "", 0, 0 # Definición de variables
    while letraClave < len(pclave):
        valor = chr(ord(pfrase[letraFrase])^ord(pclave[letraClave]))
        fraseCodificada+=valor
        letraClave+=1
        letraFrase+=1
        if letraFrase == len(pfrase):
            break
        if letraClave == len(pclave):
            letraClave = 0
    return f"Mensaje codificado: {repr(fraseCodificada)}"

valor = "\x07"
print(ord(valor))


#print(procesarCodXOR("tarea programada", "secreto"))
        
        # vXOR = "" # Reinicia el valor binario de la letra a trabajar
        # fraseBinario = bin(ord(pfrase[letraFrase])) # Definen los valores binarios de la respectiva letra
        # claveBinario = bin(ord(pclave[letraClave]))
        # # Proceso de codificación XOR de los valores binarios
        # for i in range(2, len(fraseBinario)):
        #     if fraseBinario[i] == claveBinario[i]:
        #         vXOR += "1"
        #     else:
        #         vXOR += "0"
        # Sigue avanzando por las palabras    


def generarASCII():
    print("\n\n\n")
    contador=1
    listaASCII=""
    for i in range(1, 257):
        print(f"Valor ASCII #{contador}: {repr(chr(i))}")
        vASCII = repr(chr(i))
        print(vASCII)
        listaASCII+=vASCII[1:-1]
        #print(repr(chr(i)))
        contador+=1
    print("\n\n\n")
    return listaASCII

#print(generarASCII())

listaASCII = "\x01 \x02 \x03 \x04 \x05 \x06 \x07 \x08 \t \n \x0b \x0c \r \x0e \x0f \x10 \x11 \x12 \x13 \x14 \x15 \x16 \x17 \x18 \x19 \x1a \x1b \x1c \x1d \x1e \x1f   ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \\ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~ \x7f \x80 \x81 \x82 \x83 \x84 \x85 \x86 \x87 \x88 \x89 \x8a \x8b \x8c \x8d \x8e \x8f \x90 \x91 \x92 \x93 \x94 \x95 \x96 \x97 \x98 \x99 \x9a \x9b \x9c \x9d \x9e \x9f \xa0 ¡ ¢ £ ¤ ¥ ¦ § ¨ © ª « ¬ \xad ® ¯ ° ± ² ³ ´ µ ¶ · ¸ ¹ º » ¼ ½ ¾ ¿ À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï Ð Ñ Ò Ó Ô Õ Ö × Ø Ù Ú Û Ü Ý Þ ß à á â ã ä å æ ç è é ê ë ì í î ï ð ñ ò ó ô õ ö ÷ ø ù ú û ü ý þ ÿ Ā"
listaASCII2 = "\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0¡¢£¤¥¦§¨©ª«¬\xad®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀ"

"""
listaASCII = "\x01 \x02 \x03 \x04 \x05 \x06 \x07 \x08 \t \n \x0b \x0c \r \x0e \x0f \x10 \x11 \x12 \x13 \x14 \x15 \x16 \x17 \x18 \x19 \x1a \x1b \x1c \x1d \x1e \x1f   ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \\ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~ \x7f \x80 \x81 \x82 \x83 \x84 \x85 \x86 \x87 \x88 \x89 \x8a \x8b \x8c \x8d \x8e \x8f \x90 \x91 \x92 \x93 \x94 \x95 \x96 \x97 \x98 \x99 \x9a \x9b \x9c \x9d \x9e \x9f \xa0 ¡ ¢ £ ¤ ¥ ¦ § ¨ © ª « ¬ \xad ® ¯ ° ± ² ³ ´ µ ¶ · ¸ ¹ º » ¼ ½ ¾ ¿ À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï Ð Ñ Ò Ó Ô Õ Ö × Ø Ù Ú Û Ü Ý Þ ß à á â ã ä å æ ç è é ê ë ì í î ï ð ñ ò ó ô õ ö ÷ ø ù ú û ü ý þ ÿ Ā"
"""
simbolos = r" !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
