MATCH (e:Estudiante)-[i:INSCRIPTO]->(c:Cursada)<-[:MATERIA_DE]-(m:Materia)
WHERE e.nombre = "Franco"
RETURN 
  m.nombre AS materia,
  c.anio AS año,
  c.cuatrimestre AS cuatrimestre,
  c.turno AS turno,
  i.nota_final AS nota;

MATCH (prer:Materia)-[:PRERREQUISITO_DE]->(:Materia {nombre: "Ingles 2"})
WHERE NOT EXISTS {
  MATCH (:Estudiante {nombre: "Eros"})-[r:INSCRIPTO]->(c:Cursada)<-[:MATERIA_DE]-(prer)
  WHERE r.nota_final >= 6
}
RETURN COUNT(prer) = 0 AS puede_inscribirse;

MATCH (e:Estudiante)-[i:INSCRIPTO]->(c:Cursada)
RETURN e.nombre AS estudiante, AVG(i.nota_final) AS promedio;

MATCH (e:Estudiante)-[i:INSCRIPTO]->(c:Cursada)<-[:MATERIA_DE]-(m:Materia)
WITH m.nombre AS materia, AVG(i.nota_final) AS promedio
WHERE promedio < 7
RETURN materia, promedio;
