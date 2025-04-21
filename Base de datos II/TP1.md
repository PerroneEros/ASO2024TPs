# Trabajo Práctico: Fundamentos, Integridad y Concurrencia en Bases de Datos

## Ejercicio 1: Reglas de Integridad

### Descripción:

Se pide identificar posibles violaciones a la integridad referencial al eliminar un estudiante con cursos inscritos, y explicar mecanismos para evitarlo.

### Análisis:

Si eliminamos un estudiante que ya tiene matrículas (inscripciones) registradas, se rompe la integridad referencial, ya que quedaría una referencia a un estudiante que no existe.

### Ejemplo:

```sql
-- Supongamos que existen estas tablas:
CREATE TABLE Estudiantes (
  id INT PRIMARY KEY,
  nombre VARCHAR(50)
);

CREATE TABLE Matriculas (
  id INT PRIMARY KEY,
  id_estudiante INT,
  FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id)
);

-- Insertamos datos
INSERT INTO Estudiantes (id, nombre) VALUES (1, 'Ana');
INSERT INTO Matriculas (id, id_estudiante) VALUES (1, 1);

-- Si intentamos eliminar a Ana:
DELETE FROM Estudiantes WHERE id = 1;
-- Error: No se puede eliminar porque hay una referencia desde Matriculas
```

### Soluciones:

1. **ON DELETE CASCADE**: Elimina automáticamente las matrículas asociadas.
2. **ON DELETE SET NULL**: Establece el campo como NULL al eliminar el estudiante.
3. **RESTRICT (default)**: Impide eliminar si hay referencias.

---

## Ejercicio 2: Implementación de Restricciones

### Descripción:

Crear la tabla Matriculas con clave foránea y forzar un error de integridad al insertar datos inválidos.

### Script:

```sql
CREATE TABLE Estudiantes (
  id INT PRIMARY KEY,
  nombre VARCHAR(50)
);

CREATE TABLE Matriculas (
  id INT PRIMARY KEY,
  id_estudiante INT,
  FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id)
);

-- Insertar un estudiante válido
INSERT INTO Estudiantes (id, nombre) VALUES (1, 'Ana');

-- Insertar una matrícula válida
INSERT INTO Matriculas (id, id_estudiante) VALUES (1, 1);

-- Intentar insertar una matrícula inválida
INSERT INTO Matriculas (id, id_estudiante) VALUES (2, 99);
-- Error 1452: la clave foránea no encuentra coincidencia
```

---

## Ejercicio 3: Concurrencia

### Descripción:

Simular una situación donde dos usuarios intentan modificar el mismo saldo de una cuenta bancaria, analizando READ COMMITTED vs SERIALIZABLE.

### Ejemplo:

```sql
-- Tabla cuentas
CREATE TABLE Cuentas (
  id INT PRIMARY KEY,
  saldo DECIMAL(10,2)
);

INSERT INTO Cuentas (id, saldo) VALUES (1, 1000.00);
```

### Caso de Concurrencia:

- Usuario A lee el saldo (1000), suma 100 y guarda (saldo = 1100).
- Usuario B lee el mismo saldo original (1000), resta 200 y guarda (saldo = 800).

### Resultado:

Sin control: el último en escribir pisa el resultado anterior.

### Niveles de aislamiento:

- **READ COMMITTED**: puede haber perdidas de actualización.
- **SERIALIZABLE**: evita interferencias, asegura consistencia total.

---

## Ejercicio 4: Plan de Ejecución

### Descripción:

Comparar el rendimiento de una consulta con y sin índices usando EXPLAIN.

```sql
-- Tabla con muchos registros
CREATE TABLE Productos (
  id INT PRIMARY KEY,
  nombre VARCHAR(100),
  categoria VARCHAR(50)
);

-- Consulta sin índice:
EXPLAIN SELECT * FROM Productos WHERE categoria = 'Tecnología';

-- Crear índice
CREATE INDEX idx_categoria ON Productos(categoria);

-- Consulta con índice:
EXPLAIN SELECT * FROM Productos WHERE categoria = 'Tecnología';
```

### Resultado:

La segunda consulta debería tener mejor rendimiento (menos filas examinadas).

---

## Ejercicio 5: Creación de Índices

### Descripción:

Diseñar una consulta con filtros múltiples y crear diferentes índices para comparar.

```sql
-- Consulta:
SELECT * FROM Productos WHERE categoria = 'Tecnología' AND nombre LIKE 'L%';

-- Crear índices
CREATE INDEX idx_categoria ON Productos(categoria);
CREATE INDEX idx_nombre ON Productos(nombre);
CREATE INDEX idx_categoria_nombre ON Productos(categoria, nombre);
```

### Comparar:

Usar `EXPLAIN` para ver cuál índice mejora el plan de ejecución.

---

## Ejercicio 6: Vistas

### Descripción:

Crear una vista que resuma las ventas mensuales por producto y usarla para obtener los 5 productos más vendidos.

```sql
CREATE TABLE Ventas (
  id INT PRIMARY KEY,
  producto VARCHAR(50),
  cantidad INT,
  fecha DATE
);

CREATE VIEW VentasMensuales AS
SELECT producto, MONTH(fecha) AS mes, SUM(cantidad) AS total
FROM Ventas
GROUP BY producto, MONTH(fecha);

-- Top 5 productos
SELECT producto, SUM(total) AS total_anual
FROM VentasMensuales
GROUP BY producto
ORDER BY total_anual DESC
LIMIT 5;
```

---

## Ejercicio 7: Gestión de Permisos

### Descripción:

Crear un usuario analista con permisos limitados y probar su acceso.

```sql
-- Crear usuario
CREATE USER 'analista'@'localhost' IDENTIFIED BY 'clave123';

-- Dar permisos solo de lectura
GRANT SELECT ON universidad.* TO 'analista'@'localhost';

-- Probar inserción desde ese usuario (falla)
-- INSERT INTO Estudiantes VALUES (2, 'Juan');
-- Error: acceso denegado
```

---

## Ejercicio 8: Seguridad y Auditoría

### Descripción:

Usar triggers para auditar cambios en una tabla Clientes.

```sql
CREATE TABLE Clientes (
  id INT PRIMARY KEY,
  nombre VARCHAR(50)
);

CREATE TABLE Auditoria (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_cliente INT,
  accion VARCHAR(10),
  fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Trigger para INSERT
CREATE TRIGGER trg_insert_cliente
AFTER INSERT ON Clientes
FOR EACH ROW
INSERT INTO Auditoria (id_cliente, accion) VALUES (NEW.id, 'INSERT');

-- Trigger para UPDATE
CREATE TRIGGER trg_update_cliente
AFTER UPDATE ON Clientes
FOR EACH ROW
INSERT INTO Auditoria (id_cliente, accion) VALUES (NEW.id, 'UPDATE');
```

---

## Ejercicio 9: Backup y Restore

### Descripción:

Explicar cómo hacer un backup completo y restaurarlo.

### MySQL:

#### Backup:

```bash
mysqldump -u usuario -p basededatos > backup.sql
```

#### Restore:

```bash
mysql -u usuario -p basededatos < backup.sql
```

### Simulación de pérdida de datos:

```sql
DROP TABLE Clientes;
-- Restaurar usando el archivo backup.sql
```

---

#

