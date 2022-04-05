#######################################################
#Creado por: Carlos Guzmán
#Fecha de creación: 4/4/2022 7:00 pm
#Última modificación: 00/00/2022 00:00 am 
#Versión de python: 3.10.2
#######################################################











def menu(): ### Menú principal
    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario. 
    Entradas: opcion (int) opcion del menú
    Salidas: Resultado según lo solicitado
    """
    print ("**************************")
    print ("*      Cripografía       *")
    print ("**************************")
    print ("1. Cifrado César ")
    print ("2. Cifrado por llave ")
    print ("3. ustitución Vigenére ")
    print ("4. Sustitución XOR y llave ")
    print ("5. Palabra inversa ") 
    print ("6. Mensaje inverso ")
    print ("7. Cifrado telefónico ")
    print ("8. Cifrado binario ")   
    print ("0. Terminar")
    opcion = int (input ("Seleccione una opción: "))
    if opcion >=0 and opcion <=8: 
        if opcion == 1:
            return #obtenerParidad()
        elif opcion == 2:
            return #obtenerFibonacci()
        elif opcion == 3:
            return #obtenerPerfecto()
        elif opcion == 4:
            return #obtenerMCD()
        elif opcion == 5:
            return #obtenerMCM()
        elif opcion == 6:
            return #obtenerMCM()
        elif opcion == 7:
            return #obtenerMCM()
        elif opcion == 8:
            return #obtenerMCM()
        else:
            return ""
    else:
        print ("Opción inválida, indique un número según las opciones proporcionadas.")
    return menu()

# Programa Principal (PP)
print("\n--- Tarea Programada ---\n     Carlos Guzmán \n     Samuel Gárces\n________________________\n\n")
menu()