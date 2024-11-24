# Normalización de la Base de Datos: Sistema de Ventas en Línea  

Este documento ha sido elaborado por el grupo compuesto por:

- **Andy García**  
- **Fausto Desch**  
- **Eros Perrone**  
- **Juan Blas Natalini**  

En él se describe el diseño y normalización de la base de datos para el **Sistema de Ventas en Línea**, incluyendo dependencias funcionales, claves candidatas, la justificación de las claves primarias y el cumplimiento hasta la **Tercera Forma Normal (3FN)**.
  

## Diagrama de Esquema de Tablas  

 ![Diagrama](https://github.com/user-attachments/assets/405d5ac7-d811-4f83-8f91-8f571bd78266)


Generado en dbdiagram.io, el diagrama muestra las tablas `Productos`, `Clientes`, `Ordenes` y `Detalles_Orden` y sus relaciones.  

---

## Dependencias Funcionales (DFs)  

### **1. Tabla `Productos`**  
- `ID_Producto` → `Nombre, Categoria, Precio, Stock`  

### **2. Tabla `Clientes`**  
- `ID_Cliente` → `Nombre, Email, Direccion, Telefono`  

### **3. Tabla `Ordenes`**  
- `ID_Orden` → `ID_Cliente, Fecha`  

### **4. Tabla `Detalles_Orden`**  
- `(ID_Orden, ID_Producto)` → `Cantidad`  

---

## Claves Candidatas  

### **1. Tabla `Productos`**  
- Clave candidata: `ID_Producto`  

### **2. Tabla `Clientes`**  
- Clave candidata: `ID_Cliente`  

### **3. Tabla `Ordenes`**  
- Clave candidata: `ID_Orden`  

### **4. Tabla `Detalles_Orden`**  
- Clave candidata: La combinación `(ID_Orden, ID_Producto)`  

---

## Elección Justificada de la Clave Primaria  

### **1. Tabla `Productos`**  
La clave primaria elegida es `ID_Producto` porque identifica de manera única cada producto.  

### **2. Tabla `Clientes`**  
La clave primaria elegida es `ID_Cliente` porque identifica de manera única cada cliente.  

### **3. Tabla `Ordenes`**  
La clave primaria elegida es `ID_Orden` porque identifica de manera única cada orden.  

### **4. Tabla `Detalles_Orden`**  
La clave primaria elegida es la combinación `(ID_Orden, ID_Producto)` porque identifica de manera única cada línea de detalle en una orden.  

---

## Normalización  

### **1NF (Primera Forma Normal)**  
- **Requisito:** Todos los atributos deben contener valores atómicos y únicos en cada celda.  
- **Cumplimiento:** Cada columna contiene valores atómicos. Por ejemplo, `Nombre` en `Productos` es un solo texto, no una lista o conjunto.  

### **2NF (Segunda Forma Normal)**  
- **Requisito:** Estar en 1NF y que todos los atributos no clave dependan completamente de la clave primaria.  
- **Cumplimiento:**  
  - En `Productos`, todos los atributos dependen únicamente de `ID_Producto`.  
  - En `Clientes`, todos los atributos dependen de `ID_Cliente`.  
  - En `Ordenes`, `ID_Cliente` y `Fecha` dependen de `ID_Orden`.  
  - En `Detalles_Orden`, `Cantidad` depende completamente de `(ID_Orden, ID_Producto)`.  

### **3NF (Tercera Forma Normal)**  
- **Requisito:** Estar en 2NF y no tener dependencias transitivas.  
- **Cumplimiento:**  
  - No existen dependencias transitivas en ninguna tabla.  
  - Por ejemplo, en `Productos`, `Precio` depende directamente de `ID_Producto`, y no de otro atributo como `Categoria`.  

---
## Código DBML  

El siguiente código en formato DBML describe las tablas y relaciones de la base de datos:  

```dbml
Table Productos {
    ID_Producto INT [pk, increment, not null]
    Nombre VARCHAR(100) [not null, unique]
    Categoria VARCHAR(50) [not null]
    Precio DECIMAL(10, 2) [not null]
    Stock INT [not null]
}

Table Clientes {
    ID_Cliente INT [pk, increment, not null]
    Nombre VARCHAR(100) [not null]
    Email VARCHAR(100) [not null, unique]
    Direccion VARCHAR(200) [not null]
    Telefono VARCHAR(15) [not null, unique]
}

Table Ordenes {
    ID_Orden INT [pk, increment, not null]
    ID_Cliente INT [not null, ref: > Clientes.ID_Cliente]
    Fecha DATE [not null]
}

Table Detalles_Orden {
    ID_Detalle INT [pk, increment, not null]
    ID_Orden INT [not null, ref: > Ordenes.ID_Orden]
    ID_Producto INT [not null, ref: > Productos.ID_Producto]
    Cantidad INT [not null, note: 'Cantidad debe ser mayor a 0']

    Indexes {
        (ID_Orden, ID_Producto) [unique]
    }
}
```
---
## Resumen  

Este diseño cumple con los criterios de normalización hasta la **Tercera Forma Normal (3FN)**, garantizando:  
1. **Reducción de redundancias:** Cada dato se almacena una sola vez.  
2. **Facilidad de mantenimiento:** Las modificaciones son más simples y menos propensas a errores.  
3. **Integridad referencial:** Las relaciones entre tablas están claramente definidas con claves foráneas.  

Este esquema es óptimo para gestionar eficientemente los datos del sistema de ventas en línea.  
