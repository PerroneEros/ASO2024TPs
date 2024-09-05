'''8. El mismo almacén del punto anterior almacena los datos del stock de productos en 
el archivo stock.txt separados por punto y coma ( ; ) con el formato “codigo de 
producto; stock mínimo; stock real”. Escriba un programa, que a partir de 
información contenida en los archivos, genere otro archivo de texto, Compras.txt, 
conteniendo todos los productos cuyo stock se encuentra por debajo del mínimo. 
Utilizar el archivo productos.txt del punto anterior, y crear un archivo stock.txt y 
cargarle datos utilizando los códigos de los productos del archivo anterior. Ej: 
100;50;60 
102;50;20 
135;20;15 
138;20;20 
140;10;8 
201;20;30   '''

#abro ruta stock ,abro el archivo y lo leo
ruta_stock =  r"C:\Users\erosp\OneDrive\Escritorio\PYTHON\TP2.py\Stock.txt"
archivo_stock = open(ruta_stock,"r")

lista_stock = list()

for linea in archivo_stock:
    lista =linea.strip().split(";")
    if int(lista[2]) < int(lista[1]):
        lista_stock.append({"codigo de producto": int(lista[0]), "stock minimo":int(lista[1]),"stock real":int(lista[2])})

archivo_stock.close

ruta_productos = r"C:\Users\erosp\OneDrive\Escritorio\PYTHON\TP2.py\productos.txt"
archivo_productos = open(ruta_productos,"r")
ruta_compras = "compras.txt"
archivo_compras =open(ruta_compras,'w')

lista_productos = list()

for linea in archivo_productos:
    lista =linea.strip().split(";")
    for i in lista_stock:
        if int(i["codigo de producto"])== int(lista[0]):
            archivo_compras.write(f"{lista[0]} , {lista[1]}, {int(i["stock minimo"])- int(i["stock real"])}\n")
 
archivo_productos.close
archivo_compras.close