funcionamiento = True
lista = list()
posicion = 0

while funcionamiento:
    elemento =int(input("ingrese un elemnto:"))
    if  elemento > 0:
        lista.insert(posicion,elemento)
        posicion += 1
    elif elemento == 0:
        funcionamiento = False
    else:
        print("ERROR numero negativo")

cantidad = len(lista)
contador = 0

for i in range(0,cantidad-1,1):
    if lista[i] < lista[i+1]:
        contador += 1    

if contador == cantidad-1:
    print("la lista esta ordenada")
else:
    print("la lista no esta ordenado") 