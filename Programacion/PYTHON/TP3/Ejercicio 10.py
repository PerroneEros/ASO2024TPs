'''10. Dada una lista de diccionarios que contienen información de estudiantes de una 
materia (nombre_apellido, legajo, nota_parcial1, nota_parcial2, nota_final) , 
utilizando list comprehensions:

a. Crea una lista que contenga los nombres de todos los estudiantes. Salida 
ejemplo: nombres: ['Pepe', 'María', 'Pedro', 'Ana'] 

b. Crea una lista que contenga los nombres de todos los estudiantes que han 
obtenido una calificación superior a 70 en todos los exámenes 

c. Crea una lista que contenga los nombres de todos los estudiantes que han 
obtenido una calificación inferior a 60 en al menos un examen. '''

estudiantes = [
    {
        "nombre_apellido": "Pepe García",
        "legajo": 123,
        "nota_parcial1": 75,
        "nota_parcial2": 80,
        "nota_parcial3": 70,
        "nota_final": 85
    },
    {
        "nombre_apellido": "María López",
        "legajo": 124,
        "nota_parcial1": 60,
        "nota_parcial2": 90,
        "nota_parcial3": 50,
        "nota_final": 65
    },
    {
        "nombre_apellido": "Pedro Díaz",
        "legajo": 125,
        "nota_parcial1": 90,
        "nota_parcial2": 85,
        "nota_parcial3": 95,
        "nota_final": 90
    },
    {
        "nombre_apellido": "Ana Pérez",
        "legajo": 126,
        "nota_parcial1": 55,
        "nota_parcial2": 65,
        "nota_parcial3": 58,
        "nota_final": 60
    }
]
lista_de_nombres = [estudiante["nombre_apellido"] for estudiante in estudiantes]
print(f"los nombres de los estudiantes son:{lista_de_nombres}")
#se usa el all para que se cumpla en todas
lista_de_nombres_con_nota_mayor_a_70 = [estudiante["nombre_apellido"] for estudiante in estudiantes if all(nota > 70 for nota in [estudiante["nota_parcial1"],estudiante["nota_parcial2"],estudiante["nota_parcial3"],estudiante["nota_final"]])]
print(f"los estudiantes con notas mayores a 70 en todos los parciales son: {lista_de_nombres_con_nota_mayor_a_70}")
#se usa el any para que en cualquier caso que pase 
lista_de_nombres_con_alguna_nota_menor_a_60 = [estudiante["nombre_apellido"] for estudiante in estudiantes if any(nota < 60 for nota in [estudiante["nota_parcial1"],estudiante["nota_parcial2"],estudiante["nota_parcial3"],estudiante["nota_final"]])]
print(f"los estudiantes con alguna nota menor a 60 son: {lista_de_nombres_con_alguna_nota_menor_a_60}")