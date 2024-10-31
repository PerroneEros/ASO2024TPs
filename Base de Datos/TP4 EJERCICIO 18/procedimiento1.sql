DELIMITER //
CREATE PROCEDURE ActualizarStatusProyectos()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE ProyectoId INT;
    DECLARE FechaInicio DATE;
    DECLARE FechaFin DATE;
    DECLARE Estado VARCHAR(50);

    DECLARE Cursor1 CURSOR FOR 
        SELECT ProyectoId, FechaInicio, FechaFin, Estado FROM Proyectos;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    START TRANSACTION;
    OPEN Cursor1;

    FETCH Cursor1 INTO ProyectoId, FechaInicio, FechaFin, Estado;

    WHILE done = 0 DO
        IF FechaFin IS NOT NULL AND CURDATE() > FechaFin AND Estado != 'Completado' THEN
            UPDATE Proyectos SET Estado = 'Retrasado' WHERE ProyectoId = ProyectoId;
        ELSEIF FechaFin IS NOT NULL AND CURDATE() <= FechaFin AND Estado = 'Retrasado' THEN
            UPDATE Proyectos SET Estado = 'En Curso' WHERE ProyectoId = ProyectoId;
        END IF;

        FETCH Cursor1 INTO ProyectoId, FechaInicio, FechaFin, Estado;
    END WHILE;

    CLOSE Cursor1;
    COMMIT;
END//
DELIMITER ;

CALL ActualizarStatusProyectos();
SELECT * FROM Proyectos;