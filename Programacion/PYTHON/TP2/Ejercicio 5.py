'''  5. Escriba un programa que permita cargar una lista de alumnos junto con su nota del 
parcial. Seleccione la estructura de datos que mejor se adapte al problema. Luego 
de ingresados los datos debe generar una lista donde figure si aprobaron o no (se 
aprueba con 40 o más). El listado a mostrar por pantalla debe ser como el siguiente 
(el resultado no se almacena, se calcula): 
ALUMNOS  PARCIAL  RESULTADO 
Smith, Juan      70   Aprobado 
Suárez, María      35   Desaprobado'''

listado = list()
cantidad_de_alumnos = int(input("ingrese la cantidad de alumnos que va a cargar:"))

for i in range(1,cantidad_de_alumnos + 1,1):
    nombre = input("ingrese el nombre del alumno:")
    parcial = int(input("ingrese la nota del parcial:"))
    if parcial >= 40:
        resultado = "Aprobado"
    else:
        resultado = "Desaprobado"
   
    alumno = {"nombre":nombre,"parcial":parcial,"resultado":resultado}
    listado.append(alumno)
    print(listado)


