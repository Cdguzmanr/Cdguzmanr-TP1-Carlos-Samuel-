def corregirError(string):
    if string == "":  # Valida en caso de no ingresar ningún valor       
        return "No puede ingresar un valor vacío"
    elif string.find(" ") != -1:    # Valida en caso de ingresar espacios en blanco entre los dígitos             
        return "No debe digitar espacios"

