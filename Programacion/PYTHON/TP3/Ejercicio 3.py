'''3. Lee el contenido de un archivo de texto llamado "datos.txt" y crea una lista con todas 
las líneas del archivo, utilizando list comprehensions.'''

ruta = r"C:\Users\eros\Desktop\PYTHON\TP3\datos.txt"
archivo = open(ruta, "r")

lista_lineas_archivo =[lineas.strip() for lineas in archivo]

archivo.close()

print(lista_lineas_archivo)
