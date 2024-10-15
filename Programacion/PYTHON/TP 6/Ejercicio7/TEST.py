from clasecuidador import Cuidador
from clasemascota  import Mascota

class testerCuidador:
    
    @staticmethod
    def test():
        # Creamos instancias de cuidador y mascotas
        cuidador1 = Cuidador("Juan Perez", "Calle Falsa 123", "5551234567")
        cuidador2 = Cuidador("Maria Lopez", "Avenida Siempre Viva 742", "5559876543")

        mascota1 = Mascota("Fido", "Perro", 1, "Color negro")
        mascota2 = Mascota("Michi", "Gato", 1, "Color verde")

        # Asignamos mascotas al cuidador
        cuidador1.agregarMascota(mascota1)  # Juan asigna a Fido
        cuidador1.agregarMascota(mascota2)  # Juan asigna a Michi
        cuidador2.agregarMascota(mascota2)  # Maria asigna a Michi

        # Verificamos el nombre, dirección y teléfono del cuidador
        print(cuidador1.obtenerNombre())  # Juan Perez
        print(cuidador1.obtenerDireccion())  # Calle Falsa 123
        print(cuidador1.obtenerTelefono())  # 5551234567

        print(cuidador2.obtenerNombre())  # Maria Lopez
        print(cuidador2.obtenerDireccion())  # Avenida Siempre Viva 742
        print(cuidador2.obtenerTelefono())  # 5559876543

        # Verificamos las mascotas asignadas al cuidador
        print(cuidador1.obtenerMascotas())  # ['Fido', 'Michi']
        print(cuidador2.obtenerMascotas())  # ['Michi']

        # Cambiamos los datos del cuidador
        cuidador1.establecerNombre("Carlos Ramirez")
        cuidador1.establecerDireccion("Boulevard Central 456")
        cuidador1.establecerTelefono("5551112233")

        # Verificamos que los cambios se reflejen correctamente
        print(cuidador1.obtenerNombre())  # Carlos Ramirez
        print(cuidador1.obtenerDireccion())  # Boulevard Central 456
        print(cuidador1.obtenerTelefono())  # 5551112233

if __name__ == "__main__":
    testerCuidador.test()