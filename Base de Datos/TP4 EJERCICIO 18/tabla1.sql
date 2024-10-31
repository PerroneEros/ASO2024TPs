CREATE TABLE Proyectos (
    ProyectoId INT PRIMARY KEY AUTO_INCREMENT,
    NombreProyecto VARCHAR(100) NOT NULL,
    FechaInicio DATE NOT NULL,
    FechaFin DATE,
    Estado VARCHAR(20) NOT NULL
);