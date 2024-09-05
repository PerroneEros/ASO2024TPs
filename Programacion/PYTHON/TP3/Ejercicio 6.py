'''6. Dado un diccionario de personas y sus edades, crea una lista que contenga solo los 
nombres de las personas cuya edad es mayor a una edad ingresada por el usuario, 
utilizando list comprehensions. '''

diccionario = {
    "Lautaro" : "30",  
    "Eros": "1",
    "Fausto": "14",
    "Andy": "98",
    "Juan": "17",
    "Joaquin": "28"  
}
lista_mayores =[]
edad = int(input("ingrese una edad:"))
lista_mayores = [nombre for nombre, valor_edad in diccionario.items() if int(valor_edad) > edad]
print(lista_mayores)