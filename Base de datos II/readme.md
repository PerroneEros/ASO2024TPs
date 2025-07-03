# 🧠 Trabajo Práctico - Neo4j y Cypher: Sistema de Gestión de Proyectos
## Ejercicio 1
## Ejercicio 2
## Ejercicio 3
###  Creación de Usuarios

```cypher
// Crear 4 usuarios
CREATE (:Usuario {nombre: 'Alice'});
CREATE (:Usuario {nombre: 'Bob'});
CREATE (:Usuario {nombre: 'Clara'});
CREATE (:Usuario {nombre: 'David'});
```
![image](https://github.com/user-attachments/assets/ca2ad093-134a-470b-9d74-be7c3e6b4a7a)

---

###  Conexiones entre usuarios

```cypher
// Conexiones CONOCE entre usuarios
MATCH (a:Usuario {nombre: 'Alice'}), (b:Usuario {nombre: 'Bob'})
CREATE (a)-[:CONOCE]->(b), (b)-[:CONOCE]->(a);

MATCH (a:Usuario {nombre: 'Alice'}), (c:Usuario {nombre: 'Clara'})
CREATE (a)-[:CONOCE]->(c);

MATCH (c:Usuario {nombre: 'Clara'}), (d:Usuario {nombre: 'David'})
CREATE (c)-[:CONOCE]->(d), (d)-[:CONOCE]->(c);
```
![image](https://github.com/user-attachments/assets/71e66598-15d8-40af-8adf-bd9fc4382bd7)

---

###  Publicaciones

```cypher
// Cada post tiene contenido y fecha
MATCH (a:Usuario {nombre: 'Alice'})
CREATE (a)-[:PUBLICÓ]->(:Post {contenido: 'Primer post de Alice', fecha: '2024-01-01'});

MATCH (b:Usuario {nombre: 'Bob'})
CREATE (b)-[:PUBLICÓ]->(:Post {contenido: 'Hola desde Bob', fecha: '2024-01-10'});

MATCH (c:Usuario {nombre: 'Clara'})
CREATE (c)-[:PUBLICÓ]->(:Post {contenido: 'Clara comparte una novedad', fecha: '2024-02-01'});
```

<imagen>

---

### Habilidades y Endosos

```cypher
// Habilidades de usuarios
MATCH (a:Usuario {nombre: 'Alice'})
CREATE (a)-[:TIENE_HABILIDAD]->(:Habilidad {nombre: 'Python'}),
       (a)-[:TIENE_HABILIDAD]->(:Habilidad {nombre: 'SQL'});

MATCH (b:Usuario {nombre: 'Bob'})
CREATE (b)-[:TIENE_HABILIDAD]->(:Habilidad {nombre: 'Java'}),
       (b)-[:TIENE_HABILIDAD]->(:Habilidad {nombre: 'JavaScript'});

MATCH (c:Usuario {nombre: 'Clara'})
CREATE (c)-[:TIENE_HABILIDAD]->(:Habilidad {nombre: 'Python'}),
       (c)-[:TIENE_HABILIDAD]->(:Habilidad {nombre: 'React'});

MATCH (d:Usuario {nombre: 'David'})
CREATE (d)-[:TIENE_HABILIDAD]->(:Habilidad {nombre: 'SQL'}),
       (d)-[:TIENE_HABILIDAD]->(:Habilidad {nombre: 'Docker'});
```

 <imagen>

---

###  Endosos

```cypher
// Endosos entre usuarios
MATCH (b:Usuario {nombre: 'Bob'}), (h:Habilidad {nombre: 'Python'})
CREATE (b)-[:ENDOSÓ]->(h);

MATCH (a:Usuario {nombre: 'Alice'}), (h:Habilidad {nombre: 'Java'})
CREATE (a)-[:ENDOSÓ]->(h);

MATCH (d:Usuario {nombre: 'David'}), (h:Habilidad {nombre: 'React'})
CREATE (d)-[:ENDOSÓ]->(h);

MATCH (c:Usuario {nombre: 'Clara'}), (h:Habilidad {nombre: 'Docker'})
CREATE (c)-[:ENDOSÓ]->(h);
```

 <imagen>

---

##  Consultas

### 1. Usuarios con más conexiones

```cypher
// Cuenta la cantidad de relaciones CONOCE que tiene cada usuario
MATCH (u:Usuario)-[:CONOCE]->()
RETURN u.nombre, COUNT(*) AS conexiones
ORDER BY conexiones DESC;
```

 <imagen>

---

### 2. Top 2 usuarios con más publicaciones

```cypher
// Devuelve los 2 usuarios con más posts publicados
MATCH (u:Usuario)-[:PUBLICÓ]->(p:Post)
RETURN u.nombre, COUNT(p) AS cantidad_posts
ORDER BY cantidad_posts DESC
LIMIT 2;
```

 <imagen>

---

### 3. Habilidades más endosadas

```cypher
// Devuelve las habilidades que recibieron más ENDOSÓ
MATCH (:Usuario)-[:ENDOSÓ]->(h:Habilidad)
RETURN h.nombre, COUNT(*) AS cantidad_endosos
ORDER BY cantidad_endosos DESC;
```

 <imagen>

---

### 4. Habilidades que un usuario no ha endosado a nadie

```cypher
// Por ejemplo: habilidades que Alice aún no endosó a nadie
MATCH (h:Habilidad)
WHERE NOT EXISTS {
  MATCH (:Usuario {nombre: 'Alice'})-[:ENDOSÓ]->(h)
}
RETURN h.nombre;
```

 <imagen>

---
## Ejercicio 4

###  Creación de Estudiantes

```cypher
// Crear nodos de 3 estudiantes
CREATE (:Estudiante {nombre: 'Lucas', legajo: 101});
CREATE (:Estudiante {nombre: 'Martina', legajo: 102});
CREATE (:Estudiante {nombre: 'eros', legajo: 103});
```
![image](https://github.com/user-attachments/assets/51759603-b3e3-4f8b-9f1f-7bf1172291ab)

---

### Creación de Materias

```cypher
// Crear 3 materias
CREATE (:Materia {nombre: 'Matemática I'});
CREATE (:Materia {nombre: 'Matemática II'});
CREATE (:Materia {nombre: 'Programación'});
```
![image](https://github.com/user-attachments/assets/93b113f9-5b0b-41d1-8bdd-02d2616f4ecd)

---

###  Relación de Prerrequisito

```cypher
// Matemática I es prerrequisito de Matemática II
MATCH (m1:Materia {nombre: 'Matemática I'}), (m2:Materia {nombre: 'Matemática II'})
CREATE (m2)-[:PRERREQUISITO]->(m1);
```
![image](https://github.com/user-attachments/assets/db165c2c-2e28-4681-8678-ae5fc3596abd)

---

### Creación de Cursos

```cypher
// Crear 4 cursos dictados en el año 2024
CREATE (:Curso {codigo: 'C101', año: 2024});
CREATE (:Curso {codigo: 'C102', año: 2024});
CREATE (:Curso {codigo: 'C103', año: 2024});
CREATE (:Curso {codigo: 'C104', año: 2024});
```
![image](https://github.com/user-attachments/assets/064820e1-0189-4768-b27a-f70604e29ff2)

---

###  Relación Curso-Materia

```cypher
// Asignar materias a cada curso
MATCH (c:Curso {codigo: 'C101'}), (m:Materia {nombre: 'Matemática I'})
CREATE (c)-[:CORRESPONDE_A]->(m);

MATCH (c:Curso {codigo: 'C102'}), (m:Materia {nombre: 'Matemática II'})
CREATE (c)-[:CORRESPONDE_A]->(m);

MATCH (c:Curso {codigo: 'C103'}), (m:Materia {nombre: 'Programación'})
CREATE (c)-[:CORRESPONDE_A]->(m);

MATCH (c:Curso {codigo: 'C104'}), (m:Materia {nombre: 'Matemática I'})
CREATE (c)-[:CORRESPONDE_A]->(m);
```
![image](https://github.com/user-attachments/assets/11a48ff0-d3e0-466a-8e5d-23aa3ccf916f)

---

###  Inscripciones y Notas

```cypher
// Lucas se inscribe a Matemática I y Programación
MATCH (e:Estudiante {legajo: 101}), (c:Curso {codigo: 'C101'})
CREATE (e)-[:INSCRIPTO_EN {notaFinal: 8}]->(c);

MATCH (e:Estudiante {legajo: 101}), (c:Curso {codigo: 'C103'})
CREATE (e)-[:INSCRIPTO_EN {notaFinal: 9}]->(c);

// Martina a Matemática I y II
MATCH (e:Estudiante {legajo: 102}), (c:Curso {codigo: 'C101'})
CREATE (e)-[:INSCRIPTO_EN {notaFinal: 6}]->(c);

MATCH (e:Estudiante {legajo: 102}), (c:Curso {codigo: 'C102'})
CREATE (e)-[:INSCRIPTO_EN {notaFinal: 5}]->(c);

// eros solo Matemática I
MATCH (e:Estudiante {legajo: 103}), (c:Curso {codigo: 'C101'})
CREATE (e)-[:INSCRIPTO_EN {notaFinal: 7}]->(c);
```
 ![image](https://github.com/user-attachments/assets/aa879ef6-6386-4c0d-93b4-f4cd1940743a)

---
![image](https://github.com/user-attachments/assets/011e3c99-fc9f-4967-a7a2-4c044b2cca76)
![image](https://github.com/user-attachments/assets/c89775e0-01a9-4416-8b12-a20e309536be)

---
##  Consultas

### 1.Listar la transcripción académica de un estudiante.

```cypher
// Lista de materias, cursos y notas del estudiante 101 (Lucas)
MATCH (e:Estudiante {legajo: 101})- [i:INSCRIPTO_EN]->(c:Curso)-[:CORRESPONDE_A]->(m:Materia)
RETURN m.nombre AS materia, c.codigo AS curso, i.notaFinal AS nota;
```
![image](https://github.com/user-attachments/assets/72450111-df05-4ace-8166-35e253a07f55)

---

### 2.Verificar si un estudiante puede inscribirse en una materia (si aprobó los prerrequisitos).

```cypher
// Verifica si Lucas puede inscribirse a Matemática II (nota >= 6 en su prerrequisito)
MATCH (e:Estudiante {legajo: 101}),
      (m:Materia {nombre: 'Matemática II'})-[:PRERREQUISITO]->(prerre)
MATCH (e)-[:INSCRIPTO_EN]->(:Curso)-[:CORRESPONDE_A]->(prerre)
WHERE EXISTS {
  MATCH (e)-[ins:INSCRIPTO_EN]->(:Curso)-[:CORRESPONDE_A]->(prerre)
  WHERE ins.notaFinal >= 6
}
RETURN e.nombre AS estudiante, 'Puede inscribirse a Matemática II' AS estado;
```
![image](https://github.com/user-attachments/assets/b0f2cd8a-5ae1-4eaa-b897-0b9e1eb8787c)

---

### 3.Calcular el promedio de calificaciones por estudiante.

```cypher
// Promedio general de cada estudiante
MATCH (e:Estudiante)-[i:INSCRIPTO_EN]->(:Curso)
RETURN e.nombre, round(AVG(i.notaFinal),2) AS promedio;
```
![image](https://github.com/user-attachments/assets/02848244-56dd-4602-b522-4de1aebcb697)

---

### 4.Detectar materias con promedio inferior a 7.

```cypher
// Lista de materias cuyo promedio general de notas es menor a 7
MATCH (:Estudiante)-[i:INSCRIPTO_EN]->(c:Curso)-[:CORRESPONDE_A]->(m:Materia)
WITH m, avg(i.notaFinal) AS promedio
WHERE promedio < 7
RETURN m.nombre AS materia, round(promedio,2) AS promedio;
```
![image](https://github.com/user-attachments/assets/dde6d366-be9e-4591-bb52-60e0b8131f58)

