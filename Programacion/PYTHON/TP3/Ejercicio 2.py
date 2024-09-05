'''2. Implemente una función que, dada una lista de nombres, devuelva una nueva lista 
que contenga solo los nombres que tengan una longitud mayor o igual a una 
cantidad de caracteres pasada por parámetro, utilizando list comprehensions.'''

lista_nombres = ['jose','thiago','andy','lautaro','sofia','luciano']

def longitud_nombres(parametro:int)->list:
    lista_nombres_con_mayor_cantidad_de_caracteres = [nombre for nombre in lista_nombres if len(nombre) >= parametro]
    return lista_nombres_con_mayor_cantidad_de_caracteres


parametro =int(input("ingrese una cantidad de caracteres:"))
print(f"los nombres que tienen mayor o igual cantidad de caracteres son:{longitud_nombres(parametro)}")