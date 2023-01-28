def tam_digitos(n):
    subcadena_actual = ""
    subcadena_mas_larga = ""
    for i in n:
        if i.isdigit(): #isdigit() es para determinar si el caracter es un digito o no
            subcadena_actual += i
            if len(subcadena_actual) > len(subcadena_mas_larga):
                subcadena_mas_larga = subcadena_actual
        else:
            subcadena_actual = ""
    return len(subcadena_mas_larga)

print(tam_digitos("abc1234"))