from ParticipantesYDisciplina import Participantes
from ParticipantesYDisciplina import Disciplina

class testerDiciplina:
    
    @staticmethod
    
    class test():
        # Creamos instancias de participantes y disciplinas
        p1 = Participantes("Juan", 25, "Argentina")
        p2 = Participantes("Maria", 22, "España")

        d1 = Disciplina("Carrera 100m", "Competencia de velocidad a 100 metros")
        d2 = Disciplina("Salto de longitud", "Competencia de salto lo más largo posible")

        # Inscribimos participantes en disciplinas
        p1.inscribirEnDisciplina(d1)  # Juan ha sido inscrito en la disciplina Carrera 100m.
        p1.inscribirEnDisciplina(d2)  # Juan ha sido inscrito en la disciplina Salto de longitud.
        p2.inscribirEnDisciplina(d1)  # Maria ha sido inscrita en la disciplina Carrera 100m.

        # Verificamos las disciplinas en las que está inscrito un participante
        print(p1.obtenerDisciplinas())  # ['Carrera 100m', 'Salto de longitud']
        print(p2.obtenerDisciplinas())  # ['Carrera 100m']

        # Verificamos los participantes en una disciplina
        print(d1.obtenerParticipantes())  # ['Juan', 'Maria']
        print(d2.obtenerParticipantes())  # ['Juan']
        
if __name__ == "__main__":
    testerDiciplina.test()          