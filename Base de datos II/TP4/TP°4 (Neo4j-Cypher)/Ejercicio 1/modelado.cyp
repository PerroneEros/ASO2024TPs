CREATE  
    // Empleados
    (jorge:Empleado {nombre: "Jorge"}),
    (ariel:Empleado {nombre: "Ariel"}),
    (carlos:Empleado {nombre: "Carlos"}),

    // Departamentos
    (biologia:Departamento {nombre: "Biologia"}),
    (agronomia:Departamento {nombre: "Agronomia"}),
    (ingenieria:Departamento {nombre: "Ingenieria"}),

    // Proyectos
    (proyectoX:Proyecto {nombre: "Proyecto X"}),
    (proyectoZ:Proyecto {nombre: "Proyecto Z"}),

    // Relaciones 
    (jorge)-[:PERTENECE_A]->(biologia),
    (ariel)-[:PERTENECE_A]->(agronomia),
    (carlos)-[:PERTENECE_A]->(ingenieria),

    // Asignaciones 
    (jorge)-[:TRABAJA_EN {horas_semanales: 30}]->(proyectoX),
    (ariel)-[:TRABAJA_EN {horas_semanales: 40}]->(proyectoZ),
    (carlos)-[:TRABAJA_EN {horas_semanales: 45}]->(proyectoX),
    (carlos)-[:TRABAJA_EN {horas_semanales: 25}]->(proyectoZ),
    
    // Líderes
    (jorge)-[:LIDERA]->(proyectoX),
    (ariel)-[:LIDERA]->(proyectoZ);
;
