def frecuencia_caracter(string):
    diccionario = {}
    for i in string:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    return diccionario

print(frecuencia_caracter("Roy Brayam Gomez Prado"))