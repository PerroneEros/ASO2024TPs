'''4. Escriba un programa que permita ingresar un número, se debe validar que 
realmente se haya ingresado un número, y crear una lista para almacenar por 
separado los dígitos del número. Luego recorrer la lista y mostrar el índice que 
contiene el dígito mayor'''
ingreso = True
#control de datos
while ingreso:
    try:
        numero = int(input("ingrese un numero: "))
        print(f"ingreso bien el numero: {numero}")
        ingreso = False
    except ValueError:
        print("error debe ingresar un numero")
#crear una lista
lista_digitos = list()

aux = numero
while aux > 0:
    digito = aux % 10
    aux //= 10                  #DIVISION ENTERA //  Y DIVISION NORMAL /
    lista_digitos.append(digito) #.APPEND ES PARA AGREGAR UN ELEMENTO A LA LISTA 

lista_digitos.reverse()          #.REVERSE ES PARA DAR VUELTA UNA LISTA
digito_mas_alto = max(lista_digitos) #MAX ES PARA QUE TE DE EL NUMERO MAS ALTO DE UNA LISTA 
indice_digito_mas_alto = lista_digitos.index(digito_mas_alto) #INDEX TE MUESTRA EL INDICE DE LA LISTA

print(f"el digito mas alto es {digito_mas_alto } y el indice es {indice_digito_mas_alto + 1}")