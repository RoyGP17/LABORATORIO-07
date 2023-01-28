def palindromo():
    entrada = input("Escriba una palabra palindroma: ").lower()
    n = entrada[::-1]
    if entrada == n:
        print(f"Palabra {entrada} es palíndroma")
    else:
        print(f"La palabra {entrada} no es palíndroma")

palindromo()