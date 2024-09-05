'''1. Implemente una función que, dada una lista de números, devuelva una nueva lista 
que contenga el cuadrado de cada número utilizando list comprehensions.'''

lista_numeros_original = [1,2,3,5,7,8,11]

def cuadrado_de_un_numero(lista_numeros_original):
    lista_nueva = [elemento ** 2 for elemento in lista_numeros_original]
    return lista_nueva

lista_nueva = cuadrado_de_un_numero(lista_numeros_original)
print(lista_nueva)




