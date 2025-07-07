MATCH (p:Proyecto)<-[:LIDERA]-(l:Empleado),(e:Empleado)-[:TRABAJA_EN]->(p)
RETURN p.nombre AS proyecto, l.nombre AS lider, collect(e.nombre) AS empleados;

MATCH (e:Empleado)-[a:TRABAJA_EN]->(p:Proyecto) 
RETURN p.nombre AS proyecto, sum(a.horas_semanales) AS total_horas;

MATCH (e:Empleado)-[:TRABAJA_EN]->(p:Proyecto)
WITH e, COUNT(p) AS cantidad_proyectos
WHERE cantidad_proyectos > 1
RETURN e.nombre AS empleado, cantidad_proyectos;

