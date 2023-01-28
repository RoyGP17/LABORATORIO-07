def reemplazar_subcadena(cadena, vieja, nueva):
    nueva_cadena = ""
    i = 0
    while i < len(cadena):
        if cadena[i:i+len(vieja)] == vieja:
            nueva_cadena += nueva
            i += len(vieja)
        else:
            nueva_cadena += cadena[i]
            i += 1
    return nueva_cadena

cadena1 = "Brayam Gomez"
vieja1 = "Brayam"
nueva1 = "Roy"
print(reemplazar_subcadena(cadena1, vieja1, nueva1))

