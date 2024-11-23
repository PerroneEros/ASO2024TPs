-- Tabla Productos
CREATE TABLE Productos (
    ID_Producto INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100),
    Categoria VARCHAR(50),
    Precio DECIMAL(10 , 2 ),
    Stock INT
);

-- Tabla Clientes
CREATE TABLE Clientes (
    ID_Cliente INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100),
    Email VARCHAR(100),
    Direccion VARCHAR(200),
    Telefono VARCHAR(15)
);

-- Tabla Ordenes
CREATE TABLE Ordenes (
    ID_Orden INT AUTO_INCREMENT PRIMARY KEY,
    ID_Cliente INT,
    Fecha DATE,
    FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente)
);

-- Tabla Detalles_Orden
CREATE TABLE Detalles_Orden (
    ID_Detalle INT AUTO_INCREMENT PRIMARY KEY,
    ID_Orden INT,
    ID_Producto INT,
    Cantidad INT,
    FOREIGN KEY (ID_Orden) REFERENCES Ordenes(ID_Orden),
    FOREIGN KEY (ID_Producto) REFERENCES Productos(ID_Producto)
);