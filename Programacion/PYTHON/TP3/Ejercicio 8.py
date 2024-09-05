'''8. Dada una lista con elementos duplicados, crea una nueva lista que contenga solo los 
elementos únicos utilizando list comprehensions.'''
 
lista_duplicados = [2,3,2,5,6,5,6,7,7,8,8,9,9]
lista_sin_duplicados = []
[lista_sin_duplicados.append(numero) for numero in lista_duplicados if numero not in lista_sin_duplicados]
print(lista_sin_duplicados)