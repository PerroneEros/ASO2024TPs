'''9. Un profesor almacenó los datos de los alumnos de su materia en un archivo 
alumnos.txt. En cada línea guardó el número de legajo del alumno y sus tres notas 
finales (oral, escrito y trabajos prácticos). El archivo está ordenado por número de 
legajo.  
En otro archivo, ordenado alfabéticamente por apellido, guarda por línea, número de 
legajo, apellido y nombre de cada uno. 
En ambos archivos los datos están separados por punto y coma  ( ; )  . 
Desea escribir un programa para generar un archivo Promoción.txt con los apellidos 
y nombres de los alumnos que promocionan la materia, esto es, alumnos que el 
promedio de las tres notas supere los 7 puntos.  
El archivo debe quedar ordenado alfabéticamente'''

#inicio las rutas
ruta_alumnos = "alumnos.txt"
ruta_legajos = "legajo.txt"
ruta_promocion = "promocion.txt" 

#abro los archivos los primeros dos los leo y al otro lo creo y lo escribo 
archivo_alumnos = open(ruta_alumnos,"r")
archivo_legajos = open(ruta_legajos,"r")
archivo_promocion = open(ruta_promocion,"w")

lista_alumnos = list()

#en este for busco ver que alumno esta en condicion de promocionar
for linea in archivo_alumnos:
    lista_alumnos = linea.strip().split(";") #la funcion strip sirve para eliminar los espacios y la funcion splil te separa desde vos le indiques
    if ((int(lista_alumnos[1]) + int(lista_alumnos[2]) + int(lista_alumnos[3]))/3) >= 7:
        lista_alumnos.append({"numero de legajo":int(lista_alumnos[0]),"oral":int(lista_alumnos[1]),"escrito":int(lista_alumnos[2]),"trabajos practicos":int(lista_alumnos[3])})

archivo_alumnos.close()
lista_legajos = list()
lista_promocion =list()

for linea in archivo_legajos:
    lista_legajos = linea.strip().split(";")
    if int(lista_legajos[0]) == int(lista_alumnos[0]):
        lista_promocion.sort()#la funcion sort es para ordenar la lista alfabeticamente
        lista_promocion.write(f"apellido:{lista_legajos[1]}, nombre:{lista_legajos[2]}")
        

archivo_legajos.close()
archivo_promocion.close()