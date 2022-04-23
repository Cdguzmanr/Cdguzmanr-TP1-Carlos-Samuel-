

letra = "a"
#print(f"Letra; {letra}, valor binario; {format(ord(letra))}")

#f"Letra; {letra}, valor binario; {bin(letra)}"}

#_________________________________________________________________________________________________________#


string = "P Python"
binary_converted = ' '.join(format(ord(c), 'b') for c in string)

revertido = ' '.join(format(ord(c), 'b') for c in binary_converted)

#print("The Binary Representation is:", binary_converted)

abecedario = {"a": "00000", "b": "00001", "c": "00010", "d": "00011", "e": "00100", "f": "00101", "g": "00110", "h": "00111", "i": "01000", "j": "01001", "k": "01010", "l": "01011", "m": "01111", "n": "10011", "o": "10111", "l": "10000", "m": "10001", "n": "10011", "o": "10111"} 

letra = ""
valorBinario = ["*", "00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111", "01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111", "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111", "11000", "11001" ]
alfabeto = " abcdefghijklmnopqrstuvwxyz"
orden = valorBinario[alfabeto.index(letra)]

print(orden)