def div_cadena():
    cadena = input("Escriba una cadena que contenga (,) en lugar de espacio: ")
    if "," in cadena:
        print(cadena.split(","))
    else:
        print(cadena)

div_cadena()