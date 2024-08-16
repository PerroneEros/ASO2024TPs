oracion = input("ingrese una oracion:")
cantidad_de_caracteres_de_la_oracion = len(oracion)

#len sirve para contar la cantidad total de caracteres
print(f"la cantidad total de caracteres es de:{cantidad_de_caracteres_de_la_oracion}")

#.isalpha() verifica si una cadena tiene solo letras.
contador_letras = 0
for letra in oracion:
    if letra.isalpha():
        contador_letras += 1

print(f"La cantidad total de letras (consonantes y vocales, sin signos de puntuación) es de:{contador_letras}")

#.split() divide una cadena en una lista de palabras, separándolas por espacios u otro delimitador.
cantidad_de_palabras = len(oracion.split())
print(f"la cantidad de palabras separadas por uno o mas espacios es:{cantidad_de_palabras}")