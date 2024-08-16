texto = input("ingrese un texto:")
palabras = texto.split()
cantidad_de_palabras = len(palabras)

palabra_larga = ""
longitud_larga = 0

for palabra in palabras:
    if len(palabra) > longitud_larga:
        palabra_larga = palabra
        longitud_larga = len(palabra)

print(f"la palabra mas larga es {palabra_larga} y tiene {longitud_larga} letras")

