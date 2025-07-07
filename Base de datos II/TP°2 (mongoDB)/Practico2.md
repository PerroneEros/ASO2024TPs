# TP2: MongoDB

## Ejercicio 1: CRUD básico

Este ejercicio permite aplicar operaciones fundamentales de MongoDB: inserción (`insertMany`), actualización (`updateOne`) y eliminación (`deleteOne`). Sirve para introducir la manipulación básica de documentos en una colección.

```js
use("empresa");

db.createCollection("empleados");

db.empleados.insertMany([
    {nombre:'Jorge', edad: 19, puesto: 'pasante'},
    {nombre:'Maria', edad: 43, puesto: 'Backend Developer'},
    {nombre:'Milo', edad: 27, puesto: 'Ingeniero en Sistemas'}
]);

db.empleados.updateOne(
    {nombre: 'Maria'},
    {$set: {edad: 44}}
);

db.empleados.deleteOne(
    {puesto: 'pasante'}
);
```

## Ejercicio 2: Búsquedas con operadores

Se utilizan operadores lógicos y relacionales para filtrar documentos según condiciones específicas, lo cual es clave en consultas dinámicas.

```js
use("empresa");

db.empleados.find({
    $and: [
        {edad: {$gt: 25}}, 
        {edad: {$lt: 40}}
    ] 
});
```

## Ejercicio 3: Uso de proyección

 Proyectar campos seleccionados permite optimizar las consultas devolviendo solo los datos necesarios, lo cual mejora el rendimiento y claridad de los resultados.

```js
use("empresa");

db.empleados.find(
    {}, 
    { _id: 0, nombre: 1, puesto: 1 }
);
```

## Ejercicio 4: Documentos embebidos

 El uso de documentos embebidos mejora la organización y modelado de datos relacionados, como direcciones dentro de un empleado, facilitando la consulta y actualización.

```js
use("empresa");

db.empleados.updateMany(
    {}, 
    {
        $set: {
            "direccion":{
                "calle": "calle777",
                "ciudad": "Bahia Blanca",
                "codigo_postal": 8000
            }
        }
    }
);
```

## Ejercicio 5: Agregación

Las operaciones de agregación como `$group` y `$sum` permiten realizar cálculos y resúmenes complejos directamente en la base de datos, útil para análisis de datos.

```js
use("empresa");

db.createCollection("ventas");

db.ventas.insertMany([
    { producto: "Tablet", cantidad: 2, precio_unitario: 800 },
    { producto: "Auriculares", cantidad: 4, precio_unitario: 60 },
    { producto: "Silla Gamer", cantidad: 1, precio_unitario: 300 },
    { producto: "Celular", cantidad: 3, precio_unitario: 90 },
    { producto: "Teclado", cantidad: 2, precio_unitario: 150 },
    { producto: "Tablet", cantidad: 1, precio_unitario: 800 },
    { producto: "Auriculares", cantidad: 2, precio_unitario: 60 },
    { producto: "Celular", cantidad: 1, precio_unitario: 90 },
    { producto: "Teclado", cantidad: 1, precio_unitario: 150 },
    { producto: "Silla Gamer", cantidad: 2, precio_unitario: 300 }
]);

db.ventas.aggregate([
    {
        $group: {
            _id: "$producto",
            total_ventas: { $sum: { $multiply: ["$cantidad", "$precio_unitario"] } }
        }
    }
]);
```

## Ejercicio 6: Índices

Los índices mejoran el rendimiento de las consultas, especialmente en búsquedas por múltiples campos como `nombre` y `apellido`, al acelerar el acceso a los datos.

```js
use("empresa");

db.createCollection("clientes");

db.clientes.insertMany([
    {nombre: 'Camila', apellido: 'Fernández'},
    {nombre: 'Lucas', apellido: 'Pereyra'},
    {nombre: 'Julieta', apellido: 'Martínez'},
    {nombre: 'Bruno', apellido: 'Giménez'},
    {nombre: 'Sofía', apellido: 'Acosta'},
    {nombre: 'Matías', apellido: 'Romero'}
]);

db.clientes.createIndex(
    {nombre: 1, apellido: 1}
);
```

## Ejercicio 7: Referencias

Este ejercicio muestra cómo modelar relaciones entre documentos usando referencias (`ObjectId`). Es ideal cuando se necesita mantener datos normalizados entre colecciones.

```js
use("colegio");

db.createCollection("cursos");
db.createCollection("alumnos");

const curso1 = ObjectId();
const curso2 = ObjectId();
const curso3 = ObjectId();
const curso4 = ObjectId();

db.cursos.insertMany([
    {
        _id: curso1,
        nombre: "Matemática Discreta",
        profesor: "Lucía Martínez",
        clases: [
            { dia: "lunes", hora: "9am", aula: "101" },
            { dia: "miércoles", hora: "9am", aula: "101" }
        ]
    },
    {
        _id: curso2,
        nombre: "Algoritmos y Estructuras de Datos",
        profesor: "Carlos Gómez",
        clases: [
            { dia: "martes", hora: "11am", aula: "102" },
            { dia: "jueves", hora: "11am", aula: "102" }
        ]
    },
    {
        _id: curso3,
        nombre: "Sistemas Operativos",
        profesor: "Paula Torres",
        clases: [
            { dia: "miércoles", hora: "2pm", aula: "201" },
            { dia: "viernes", hora: "2pm", aula: "201" }
        ]
    },
    {
        _id: curso4,
        nombre: "Redes de Computadoras",
        profesor: "Esteban López",
        clases: [
            { dia: "lunes", hora: "4pm", aula: "202" },
            { dia: "miércoles", hora: "4pm", aula: "202" }
        ]
    }
]);

db.alumnos.insertMany([
    {
        _id: ObjectId(),
        nombre: "Agustina",
        apellido: "Morales",
        cursos: [
            { curso: curso1, estado: "cursando" },
            { curso: curso2, estado: "aprobada", nota: 8 },
            { curso: curso3, estado: "aprobada", nota: 9 },
            { curso: curso4, estado: "aprobada", nota: 10 }
        ]
    },
    {
        _id: ObjectId(),
        nombre: "Franco",
        apellido: "Vega",
        cursos: [
            { curso: curso1, estado: "cursando" },
            { curso: curso2, estado: "cursando" },
            { curso: curso4, estado: "aprobada", nota: 6 }
        ]
    },
    {
        _id: ObjectId(),
        nombre: "Valentina",
        apellido: "Ríos",
        cursos: [
            { curso: curso1, estado: "cursando" },
            { curso: curso2, estado: "cursando" },
            { curso: curso3, estado: "aprobada", nota: 7 },
            { curso: curso4, estado: "aprobada", nota: 8 }
        ]
    },
    {
        _id: ObjectId(),
        nombre: "Julián",
        apellido: "Álvarez",
        cursos: [
            { curso: curso1, estado: "cursando" },
            { curso: curso2, estado: "cursando" },
            { curso: curso3, estado: "aprobada", nota: 9 },
            { curso: curso4, estado: "aprobada", nota: 10 }
        ]
    }
]);
```

# Ejercicio 8: Uso de `$lookup`

Realiza una agregación donde se combinen los datos de alumnos y cursos usando `$lookup`.

Base de datos: `utn`

## Inserción de datos

```js
db.materias.insertMany([
  { aula: 704, materia: "base de datos" },
  { aula: 203, materia: "programacion 1" }
]);

db.alumnos.insertMany([
  { nombre: "juan", materia: "base de datos", legajo: 22336 },
  { nombre: "fulano", materia: "programacion 1", legajo: 22456 },
  { nombre: "Pedro", materia: "base de datos", legajo: 23435 }
]);
```

## Consulta con `$lookup`

```js
db.alumnos.aggregate([
  {
    $lookup: {
      from: "materias",
      localField: "materia",
      foreignField: "materia",
      as: "info_materia"
    }
  },
  { $unwind: "$info_materia" },
  {
    $project: {
      _id: 0,
      nombre: 1,
      legajo: 1,
      materia: 1,
      aula: "$info_materia.aula"
    }
  }
]);
```

## Visualización de datos

```js
db.alumnos.find();
```

---

# Ejercicio 9: Replicación y Sharding (Teórico)

## Ventajas de usar **Replica Set**

- **Alta disponibilidad**: Si el servidor principal falla, otro servidor puede reemplazarlo automáticamente.
- **Seguridad de datos**: Al tener múltiples copias de los datos, el riesgo de pérdida de información se reduce significativamente.
- **Lectura distribuida**: Se puede distribuir la carga de lectura entre las réplicas secundarias, reduciendo la presión sobre el servidor principal.

## Beneficios del **Sharding** en bases de datos de alto volumen

- **Escalabilidad horizontal**: Permite distribuir los datos entre varios servidores, facilitando el manejo de grandes volúmenes de información.
- **Mejor rendimiento**: Al tener menos datos por servidor, las consultas pueden ejecutarse más rápido.
- **Distribución de carga**: El trabajo se reparte entre varios nodos, aumentando la eficiencia general del sistema.

# Ejercicio 10: (seguridad y backups)

-Crear un usuario con permisos de lectura y escritura:

    Para crear un usuario con permisos de lectura/escritura en la base de datos, se puede usar el comando:
  ```js
    use empresa;  
    db.createUser({
    user: "lautaroAc",
    pwd: "12345678",        (datos de ej )
    roles: [
        { role: "readWrite", db: "empresa" }
    ]
    });
  ```
-Hacer un backup de la base de datos:

    - se usa la herramienta mongodump
```js
    mongodump --db empresa --out /ruta/a/backup 
```
    (aca se especifica la ruta donde se hace el volcado de la db)


-Restaurar la base de datos:
    -se usa la herramienta mongorestore
 ```js
    mongorestore --db empresa /ruta/a/backup/empresa
 ```
