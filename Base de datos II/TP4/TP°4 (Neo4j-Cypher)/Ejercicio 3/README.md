# Sistema de Cursos y Calificaciones

#### Requerimientos

En este otro ejercicio el `modelado` debe tener:
- Tres estudiantes
- Tres materias con una que tenga algun **prerrequistos**
- Cuatro cursos ditactdos
- Que tenga inscripcciones y calificaciones

## Capturas `Neo4j` 

Vemos que nos devuelve los **nodos** que creamos en el **modelado** 

![image](https://github.com/user-attachments/assets/86bf38ee-c718-4477-99b0-bccb3db9c5c0)

Ahora vemos sus **realciones** 

![image](https://github.com/user-attachments/assets/827ac5e4-1453-4a45-b239-e3e93441db49)


### Consultas

- Listar la transcripción académica de un estudiante :
  
  ![image](https://github.com/user-attachments/assets/b74145fd-eaf6-447b-b074-da22dd672cd6)

- Verificar si un estudiante puede inscribirse en una materia (si aprobó los prerrequisitos) :

  - **Franco** da `True` porque **si aprobo Ingles 1** con un `Ocho`
  ![image](https://github.com/user-attachments/assets/415835ab-72ef-446e-8112-391a343f976f)

  - **Laucha** da `False` porque **no aprobo Ingles 1** ya que se sacos un ``Cuatro``
  ![image](https://github.com/user-attachments/assets/5515b6c2-29ab-4d31-990c-4639ca587c51)

- Calcular el promedio de calificaciones por estudiante :

  ![image](https://github.com/user-attachments/assets/44c573b6-f4c4-41d8-b8b3-199810646ff1)

- Detectar materias con promedio inferior a 7 :

  ![image](https://github.com/user-attachments/assets/82424f32-bf59-4c3b-a91c-60075cbb4245)



