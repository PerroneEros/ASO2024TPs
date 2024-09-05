'''3. Escriba un programa que permita cargar las notas de exámenes, primero debe 
permitir ingresar por teclado la cantidad de notas que desea cargar, y luego 
cargarlas en una lista, y posteriormente debe buscar la nota más alta, mostrarla, e 
indicar en qué índice del arreglo se encuentra. '''

cantidad_notas = int(input("ingrese la cantidad de notas que quiere cargar:"))
lista_notas = list()

#carga de lista
for i in range(cantidad_notas):
    notas = int(input("ingrese una nota:"))
    lista_notas.append(notas)

# Encontrar la nota más alta
nota_mas_alta = max(lista_notas)
indice_nota_mas_alta = lista_notas.index(nota_mas_alta)

# Mostrar resultados
print(f"La nota más alta es {nota_mas_alta} y se encuentra en el índice {indice_nota_mas_alta + 1}.")
