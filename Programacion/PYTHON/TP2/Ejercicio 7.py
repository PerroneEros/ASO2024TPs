'''7. Un almacén guarda los códigos, los nombres de los productos y sus precios, 
respectivamente, separados por punto y coma ( ; ) en el archivo productos.txt. Hacer 
un algoritmo y luego los procedimientos necesarios que permitan tomar los datos del 
archivo y buscar el precio de un artículo ingresado por teclado. Para probar el 
algoritmo crear un archivo “productos.txt” y cargarle datos al estilo: 
100;arroz;10 
102;fideos;5 
135;lentejas;8 
138;porotos;6 
140;sal gruesa;5 
201;aceite;20       (  etc...  ) 
'''
ruta = r"C:\Users\erosp\OneDrive\Escritorio\PYTHON\TP2.py\productos.txt"
archivo = open(ruta, "r")
lista_productos = list()

for linea in archivo:
    lista = linea.split(";")
    lista_productos.append({"codigo":int(lista[0]), "producto":lista[1],"precio":int(lista[2])})
    
producto_buscado = input("ingrese el nombre del producto que esta buscando:").lower()
precio_encontrado = None

for producto in lista_productos:
    if producto_buscado == producto["producto"].lower():
        precio_encontrado = producto["precio"]
    
if precio_encontrado is not None:
    print(f"El precio de {producto_buscado} es: {precio_encontrado}")
else:
    print(f"El producto '{producto_buscado}' no se encontró en la lista.")


archivo.close()