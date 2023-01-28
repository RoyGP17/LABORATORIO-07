#Crear cadenas
x = "Cadenas en python"
print(x)
print(type(x))

x = 'Esto tambien es una cadena'
x = ''

x = "Esta es una comilla: \""
print(x)

#Mostrar saltos de linea
x = "\nLinea uno \nLinea dos"
print(x)

#Ocupar varias lineas se hace uso de la comilla triple (""")
print("""El siguiente texto
ocupa
varias 
lineas
de texto""")

#Formateo de cadenas
a = 5
print(type(a))
x = "El numero de la variable a es: " + str(a)
print(x)

#Concatenar haciendo uso del %
a = 5
x = "El numero de la variable a es: %i" % a

print(x)

#Concatenar dos o mas variables con el %
a = 5
x = "Los numeros son: %i y %i" % (4, a)
print(x)

#Concatenar con la funcion .format()
print()
x = "Los numero son {} y {} ".format(4, a)
print(x)

#Concatenar con la funcion .format() nombrando cada elemento
print()
x = "Los numero son {z} y {y} ".format(z=4, y=5)
print(x)

#Concatenar usando f-string
print()
z=4; y=7
x = f'Los numero son: {z} y {y}'
print(x)

#Operaciones usando f-string
print()
Z=4; Y=7
x = f'La suma de Z y Y es: {z + y}'
print(x)

#Uso de f-string en funciones
def fun():
    return(50)
s = f'El resultado de la funcion es: {fun()}'
print(s)

#EJEMPLOS:
s1 = "Cadena uno "
s2 = "Cadena dos"
print(s1 + " " + s2)

print(s1*3)
print()
print("Python" in "Python es un lenguaje de programacion")

#Metodos chr() y ord()
print(chr(65))
print(ord("A"))

#Funcion len()
print()
print(len("Tamaño de la cadena"))

#Idexae cadenas
print()
x = "La nueva verion de Python es: 3.20"
print(x[10])
print(x[-1])

#Crear subcadenas a partir de otras
print()
x = "La nueva verion de Python es: 3.20"
print(x[0:5])
print(x[0::3])
print(x[4:10:3])

#MÉTODOS:
#- El metodo capitalize()
x = "cadena"
print(x.capitalize())

#- El método lower()
x = "CADENA"
print(x.lower())

#- El método upper()
x = "cadena"
print(x.upper())

#- El método swapcase()
x = "cAdEnA"
print(x.swapcase())

#- El método count()
x = "python y la version 3.20"
print(x.count("on"))

#- El método isalnum()
x = "edem@gmail.com"
print(x.isalnum())

#- El método isalpha()
x = "asasdasdda"
print(x.isalpha())

#- El método strip()
x = "   cadenas limpias      "
print(x.strip())

#- El método zfill()
x = "123"
print(x.zfill(7))

#- El método join()
x = " y ".join(["uno", "dos", "tres"])
print(x)

#- El método split()
x = "java,python,ruby,C,C#"
print(x.split(","))
