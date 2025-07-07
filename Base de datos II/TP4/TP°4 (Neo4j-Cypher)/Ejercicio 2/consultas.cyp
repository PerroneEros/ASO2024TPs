MATCH (u1:Usuario)-[c:CONOCE]->(u2:Usuario) RETURN u1.nombre AS usuario, 
COUNT(c) AS cantidad_conexiones ORDER BY cantidad_conexiones DESC;

MATCH (u:Usuario)-[:POSTEA]->(p:Post) RETURN u.nombre AS usuario, 
COUNT(p) AS cantidad_posts ORDER BY cantidad_posts DESC LIMIT 2;

MATCH (:Usuario)-[e:ENDOSA]->(h:Habilidad) RETURN h.nombre AS habilidad, 
COUNT(e) AS cantidad_endosadas ORDER BY cantidad_endosadas DESC;

MATCH (h:Habilidad) WHERE NOT (:Usuario {nombre: "JuanDev"})-[:ENDOSA]->(h) 
RETURN h.nombre AS habilidades_no_endosadas;
