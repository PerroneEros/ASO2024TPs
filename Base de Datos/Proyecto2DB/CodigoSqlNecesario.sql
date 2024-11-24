-- Tabla Productos
CREATE TABLE Productos (
    ID_Producto INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Categoria VARCHAR(50) NOT NULL,
    Precio DECIMAL(10, 2) NOT NULL,
    Stock INT NOT NULL CHECK (Stock >= 0), -- No se permite stock negativo
    UNIQUE (Nombre) -- No debe haber dos productos con el mismo nombre
);

-- Tabla Clientes
CREATE TABLE Clientes (
    ID_Cliente INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE, -- Los correos electrónicos deben ser únicos
    Direccion VARCHAR(200) NOT NULL,
    Telefono VARCHAR(15) NOT NULL UNIQUE -- Los teléfonos deben ser únicos
);

-- Tabla Ordenes
CREATE TABLE Ordenes (
    ID_Orden INT AUTO_INCREMENT PRIMARY KEY,
    ID_Cliente INT NOT NULL,
    Fecha DATE NOT NULL,
    FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente) ON DELETE CASCADE
);

-- Tabla Detalles_Orden
CREATE TABLE Detalles_Orden (
    ID_Detalle INT AUTO_INCREMENT PRIMARY KEY,
    ID_Orden INT NOT NULL,
    ID_Producto INT NOT NULL,
    Cantidad INT NOT NULL CHECK (Cantidad > 0), -- La cantidad debe ser positiva
    FOREIGN KEY (ID_Orden) REFERENCES Ordenes(ID_Orden) ON DELETE CASCADE,
    FOREIGN KEY (ID_Producto) REFERENCES Productos(ID_Producto),
    UNIQUE (ID_Orden, ID_Producto) -- No se puede repetir el mismo producto en una orden
);


-- Insertar productos
INSERT INTO Productos (Nombre, Categoria, Precio, Stock) VALUES 
('Televisor', 'Electrónica', 400.00, 10),
('Lavadora', 'Electrodomésticos', 700.00, 5),
('Refrigerador', 'Electrodomésticos', 1200.00, 3),
('Microondas', 'Electrodomésticos', 200.00, 8),
('Laptop', 'Computadoras', 1500.00, 2);

-- Insertar clientes
INSERT INTO Clientes (Nombre, Email, Direccion, Telefono) VALUES 
('Juan Pérez', 'juan.perez@email.com', 'Calle Falsa 123', '123456789'),
('María Gómez', 'maria.gomez@email.com', 'Avenida Siempreviva 742', '987654321'),
('Pedro López', 'pedro.lopez@email.com', 'Calle Luna 56', '456123789');

-- Insertar órdenes
INSERT INTO Ordenes (ID_Cliente, Fecha) VALUES 
(1, '2024-11-20'),
(2, '2024-11-21'),
(3, '2024-11-22');

-- Insertar detalles de órdenes
INSERT INTO Detalles_Orden (ID_Orden, ID_Producto, Cantidad) VALUES 
(1, 1, 2), -- Juan Pérez compró 2 televisores
(1, 4, 1), -- Juan Pérez compró 1 microondas
(2, 2, 1), -- María Gómez compró 1 lavadora
(2, 3, 1), -- María Gómez compró 1 refrigerador
(3, 5, 1), -- Pedro López compró 1 laptop
(3, 4, 2); -- Pedro López compró 2 microondas

-- Algunas consultas triviales
#SELECT * FROM sistemadeventasenlinea.detalles_orden;
#SELECT * FROM sistemadeventasenlinea.clientes;
#SELECT * FROM sistemadeventasenlinea.productos;
#SELECT * FROM sistemadeventasenlinea.ordenes;
   
