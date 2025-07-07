CREATE 

    // Estudiantes
    (est1:Estudiante {nombre: 'Franco'}),
    (est2:Estudiante {nombre: 'Eros'}),
    (est3:Estudiante {nombre: 'Laucha'}),

    // Materias
    (mat1:Materia {nombre: 'Ingles 1'}),
    (mat2:Materia {nombre: 'Matematica'}),
    (mat3:Materia {nombre: 'Ingles 2'}),

    // Cursos dictados
    (cursa1:Cursada {anio: 2025, cuatrimestre: 1, turno: 'Tarde'}),
    (cursa2:Cursada {anio: 2025, cuatrimestre: 1, turno: 'Mañana'}),
    (cursa3:Cursada {anio: 2025, cuatrimestre: 2, turno: 'Mañana'}),
    (cursa4:Cursada {anio: 2025, cuatrimestre: 2, turno: 'Tarde'}),

    // Asociación de las materias con los cursos
    (mat1)-[:MATERIA_DE]->(cursa1),
    (mat1)-[:MATERIA_DE]->(cursa2),
    (mat2)-[:MATERIA_DE]->(cursa3),
    (mat3)-[:MATERIA_DE]->(cursa4),

    (mat1)-[:PRERREQUISITO_DE]->(mat3), // El Pererrequisito, se necesita Ingles 1 para cursar Ingles 2

    // Inscripciones-Calificaciones
    (est1)-[:INSCRIPTO {nota_final: 8}]->(cursa1),  // franco Ingles 1 Tarde
    (est1)-[:INSCRIPTO {nota_final: 5}]->(cursa3),  // franco Matematica
    (est2)-[:INSCRIPTO {nota_final: 7}]->(cursa2),  // eros Ingles 1 Mañana
    (est2)-[:INSCRIPTO {nota_final: 6}]->(cursa4),  // eros Ingles 2
    (est3)-[:INSCRIPTO {nota_final: 4}]->(cursa1),  // laucha Ingles 1 Tarde
    (est3)-[:INSCRIPTO {nota_final: 9}]->(cursa3)   // laucha Matematica
;

