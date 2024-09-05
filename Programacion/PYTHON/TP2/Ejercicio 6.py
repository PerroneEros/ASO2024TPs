''' 6. Escriba un programa que permita leer de un archivo distancias.txt (cada renglón 
tiene una distancia válida) las distancias recorridas por el vehículo de una empresa, 
luego calcular cual es la distancia promedio, y mostrar por pantalla el promedio y 
todas las distancias mayores al promedio. 
Ej del contenido del archivo: 
150 
120 
50 
34 
250 
Salida: “La distancia promedio de los viajes es ... y los viajes con distancia mayor 
son: ... , ... , .... , .... “ '''

ruta = r"C:\Users\erosp\OneDrive\Escritorio\PYTHON\TP2.py\distacnias.txt"
archivo = open(ruta, "r")
contador = 0
distancia = 0
lista_distancia = list()

for linea in archivo:
    linea = int(linea.strip()) #convierte la linea en entero
    contador += 1
    distancia += linea
    lista_distancia.append(linea) 

archivo.close()

promedio = distancia / contador
lista_mayor_distancia = list()

for distancia in lista_distancia:
    if distancia > promedio:
        lista_mayor_distancia.append(distancia)
        
print(f"la distnacia promedio es: {promedio} y los viajes con distancia mayor son: {lista_mayor_distancia}")
