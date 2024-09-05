'''Escribir un procedimiento “reverso” que permita ingresar como parámetro una 
cadena, y devuelva la cadena invertida (“hola” se convierte en “aloh”). Escribir luego 
un programa que determine si una cadena de caracteres es un palíndromo (un 
palíndromo es un texto que se lee igual en sentido directo y en inverso, ej.: “radar”). 
Sugerencia: para evitar diferencias entre mayúsculas y minúsculas en las cadenas, 
utilice la función del tipo string .upper() ó .lower() en las cadenas, ya que Radar es 
distinto a radaR.'''

def reverso(cadena):
    invertida = cadena[::-1]
    return invertida

cadena = input("ingrese una palabra:").lower()     #el .lower te hace que la cadena pase a minuscula
print(f"la palabra es {cadena} invertida es {reverso(cadena)}")

if cadena == reverso(cadena):
    print("la cadena es un palindromo")
else:
    print("la cadena no es un palindromo")