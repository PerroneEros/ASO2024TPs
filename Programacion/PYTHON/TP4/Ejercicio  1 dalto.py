class Estudiante:
    def __init__(self,Nombre,edad,grado):
        self.Nombre = Nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print("ESTUDIADO(NO ME JODAS GIL)") 

Nombre = input("ingrese su nombre:")
edad = int(input("ingrese su edad:"))
grado = int(input("ingrese su grado:"))


Estudiante1 = Estudiante(Nombre,edad,grado)
print(f"el nombre del estudiante es: {Estudiante1.Nombre}\nSu edad es:{Estudiante1.edad}\nEl grado es:{Estudiante1.grado}")

Estudiante1.estudiar()