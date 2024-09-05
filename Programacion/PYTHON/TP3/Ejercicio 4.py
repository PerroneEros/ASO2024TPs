'''4. Dado un diccionario de palabras y sus definiciones, crea una lista que contenga sólo 
las palabras que comienzan con una letra específica (por ejemplo, "a") indicada por 
el usuario, utilizando list comprehensions. '''

diccionario = {
    'perro': 'animal',
    'torta': 'dulce',
    'biscochito':'salado',
    'mouse':'periferico',
    'remera':'prenda'
}

lista_con_la_misma_letra = []
letra =input("ingrese una letra:").lower()
lista_con_la_misma_letra = [palabra for palabra in diccionario if palabra[0] == letra ]

print(lista_con_la_misma_letra)