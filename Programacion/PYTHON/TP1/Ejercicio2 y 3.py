ancho = float(input("Ingrese el ancho de la habitación (en metros): "))
alto = float(input("Ingrese el alto de la habitación (en metros): "))
largo = float(input("Ingrese el largo de la habitación (en metros): "))
manos = int(input("Ingrese el número de manos de pintura: "))

area_paredes = 2 * (ancho * alto) + 2 * (largo * alto)
area_puerta = 0.80 * 2
area_a_pintar = area_paredes - area_puerta
litros_necesarios = (area_a_pintar / 10) * manos

print(f"Se necesitan {litros_necesarios:.2f} litros de pintura para {manos} manos.")
