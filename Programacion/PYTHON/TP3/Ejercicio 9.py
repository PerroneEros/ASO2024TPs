'''9. Dada una lista de números, crea dos listas separadas: una que contenga los 
números pares y otra que contenga los números impares utilizando list 
comprehensions.'''

lista_de_numeros = [1,2,3,4,5,6,7,8,9]
lista_pares = []
lista_impares = []

lista_pares =[numero for numero in lista_de_numeros if numero % 2 == 0]
lista_impares =[numero for numero in lista_de_numeros if numero % 2 != 0]

print(f"los pares son: {lista_pares} y los impares son: {lista_impares}")