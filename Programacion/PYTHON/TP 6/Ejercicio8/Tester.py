from claseEvento import Evento
from claseFecha import Fecha
from claseParticipante import Participante
from calseOrganizador import Organizador

class testerEvento:
    # Clase Tester
    @staticmethod
    def test():
        # Crear organizador
        organizador1 = Organizador("Juan Pérez", "juan.perez@example.com", "Logística")

        # Crear evento
        diaEvento = Fecha(1, 10, 2023)
        evento1 = Evento("Carrera 5K", diaEvento, "Carrera popular de 5 kilómetros")

        # Asignar organizador al evento
        evento1.asignarOrganizador(organizador1)

        # Crear participantes
        participante1 = Participante("Ana López", "ana.lopez@example.com", "123456789")
        participante2 = Participante("Carlos García", "carlos.garcia@example.com", "987654321")

        # Anotar participantes al evento
        evento1.anotarParticipante(participante1)
        evento1.anotarParticipante(participante2)

        # Mostrar detalles del evento
        print(f"Evento: {evento1.obtenerNombre()}")
        print(f"Fecha: {evento1.obtenerFecha()}")
        print(f"Descripción: {evento1.obtenerDescripcion()}")
        print(f"Organizador: {evento1.obtenerOrganizador().obtenerNombre()}")
        
        # Mostrar participantes
        print("Participantes inscritos:")
        participantes_nombres = evento1.obtenerParticipantesNombres()
        if participantes_nombres:
            for nombre in participantes_nombres:
                print(f"- {nombre}")
        else:
            print("No hay participantes inscritos.")
            

if __name__ == "__main__":
    testerEvento.test()