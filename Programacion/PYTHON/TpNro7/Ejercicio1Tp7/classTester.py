from classPolizaInmueble import PolizaInmueble
from classPolizaInmuebleEscolar import PolizaInmuebleEscolar
from classAseguradora import Aseguradora

class Tester:

    @staticmethod
    def probar_poliza_inmueble():
        # Crear una instancia de PolizaInmueble
        poliza = PolizaInmueble(1001, 5000.0, 3000.0, 2000.0)
        print(f"Probando PolizaInmueble: {poliza.toString()}")
        print(f"Costo de la póliza: {poliza.costoPoliza()}")

    @staticmethod
    def probar_poliza_inmueble_escolar():
        # Crear una instancia de PolizaInmuebleEscolar
        poliza_escolar = PolizaInmuebleEscolar(2002, 6000.0, 4000.0, 3000.0, 
                                               cantPersonas=50, 
                                               montoEquipamiento=10000.0, 
                                               montoMobiliario=8000.0, 
                                               montoPersona=500.0)
        print(f"Probando PolizaInmuebleEscolar: {poliza_escolar.toString()}")
        print(f"Costo de la póliza escolar: {poliza_escolar.costoPoliza()}")

    @staticmethod
    def probar_aseguradora():
        # Crear una instancia de Aseguradora
        aseguradora = Aseguradora()

        # Crear pólizas para añadir a la aseguradora
        poliza1 = PolizaInmueble(1001, 5000.0, 3000.0, 2000.0)
        poliza2 = PolizaInmuebleEscolar(2002, 6000.0, 4000.0, 3000.0, 
                                        cantPersonas=50, 
                                        montoEquipamiento=10000.0, 
                                        montoMobiliario=8000.0, 
                                        montoPersona=500.0)
        
        # Insertar pólizas en la aseguradora
        aseguradora.insertar(poliza1)
        aseguradora.insertar(poliza2)
        print(f"Polizas en aseguradora tras inserciones: {[p.toString() for p in aseguradora._Aseguradora__seguros]}")

        # Eliminar una póliza
        aseguradora.eliminar(poliza1)
        print(f"Polizas en aseguradora tras eliminar poliza1: {[p.toString() for p in aseguradora._Aseguradora__seguros]}")

if __name__ == "__main__":
    Tester.probar_poliza_inmueble()
    print("\n")
    Tester.probar_poliza_inmueble_escolar()
    print("\n")
    Tester.probar_aseguradora()
