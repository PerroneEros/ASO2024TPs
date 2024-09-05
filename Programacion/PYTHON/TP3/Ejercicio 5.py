'''5. Dado un rango de números, crea una lista que contenga todos los números primos 
dentro de ese rango utilizando list comprehensions.'''

def es_primo(numero):
    contador = 0
    for i in range(1,numero + 1):
        if numero % i == 0:
            contador += 1    
    if contador == 2:
        return True
    else:
        return False

lista_de_numeros_primos = []
rango_minimo =int(input("ingrese el rango minimo:"))
rango_maximo =int(input("ingrese el rango maximo:"))

lista_de_numeros_primos = [numero for numero in range(rango_minimo,rango_maximo + 1,1) if es_primo(numero)]
print(lista_de_numeros_primos)