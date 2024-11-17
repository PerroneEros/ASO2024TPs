# Normalización de la Base de Datos: Juegos Olímpicos

Este documento describe la normalización de una base de datos sobre los Juegos Olímpicos, que incluye las dependencias funcionales (DFs), las claves candidatas, la justificación de la clave primaria y el proceso de normalización hasta la 3FN.

## Diagrama de Esquema de Tablas

![Diagrama de la Base de Datos](https://github.com/user-attachments/assets/57dcbf7c-4260-4eca-b094-79e98c51ac89)

Generado en dbdiagram.io, el diagrama muestra las tablas `Olimpiadas`, `Deportistas`, `Disciplinas` y `Juego` y sus relaciones.

## Dependencias Funcionales (DFs)

A continuación, se detallan las dependencias funcionales de cada tabla en el esquema:

- **Tabla Olimpiadas**
  - `id_olimpiada` → `año_olimpiada, pais_olimpiada`

- **Tabla Deportistas**
  - `id_deportista` → `nombre_deportista, pais_deportista`

- **Tabla Disciplinas**
  - `id_disciplina` → `nombre_disciplina, descripcion_disciplina`

- **Tabla Juego**
  - `(id_olimpiada, id_deportista, id_disciplina)` → `asistente`
  - `(id_olimpiada, id_deportista, id_disciplina)` → determina un único registro en `Juego`

## Claves Candidatas

Las claves candidatas para cada tabla son las siguientes:

- **Olimpiadas**: `id_olimpiada`
- **Deportistas**: `id_deportista`
- **Disciplinas**: `id_disciplina`
- **Juego**: La combinación `(id_olimpiada, id_deportista, id_disciplina)` es una clave candidata, ya que identifica de manera única cada participación de un deportista en una disciplina durante un juego olímpico.

## Elección Justificada de la Clave Primaria

- **Olimpiadas**: La clave primaria elegida es `id_olimpiada`, ya que identifica de manera única cada olimpiada.
- **Deportistas**: La clave primaria elegida es `id_deportista`, ya que cada deportista es único en la base de datos.
- **Disciplinas**: La clave primaria elegida es `id_disciplina`, ya que identifica de manera única cada disciplina.
- **Juego**: La clave primaria es la combinación `(id_olimpiada, id_deportista, id_disciplina)` porque identifica de manera única cada registro de participación de un deportista en una disciplina específica durante un juego olímpico.

## Normalización

A continuación, se detalla el proceso de normalización hasta la Tercera Forma Normal (3FN) y su cumplimiento:

### 1NF (Primera Forma Normal)  
- **Requisito:** Todos los atributos deben contener valores atómicos, sin conjuntos ni listas en las columnas.
- **Cumplimiento:** Cada campo almacena un valor único y atómico. Por ejemplo, `año_olimpiada`, `pais_olimpiada`, `nombre_deportista`, etc., todos son valores simples y únicos en cada columna.

### 2NF (Segunda Forma Normal)  
- **Requisito:** Debe estar en 1NF, y cada atributo no clave debe depender completamente de la clave primaria.
- **Cumplimiento:** La información se ha distribuido en tablas (`Olimpiadas`, `Deportistas`, `Disciplinas`, `Juego`) para asegurar que cada atributo depende completamente de la clave primaria de su tabla. Por ejemplo, en `Juego`, el campo `asistente` depende de la combinación de `id_olimpiada`, `id_deportista`, y `id_disciplina` (clave compuesta), cumpliendo con la dependencia completa.

### 3NF (Tercera Forma Normal)  
- **Requisito:** Debe estar en 2NF y no debe haber dependencias transitivas (un campo no clave no debe depender de otro campo no clave).
- **Cumplimiento:** No existen dependencias transitivas en el esquema. Cada campo no clave depende directamente de la clave primaria de su tabla. Por ejemplo, `pais_deportista` en la tabla `Deportistas` depende únicamente de la clave primaria `id_deportista`, y no de otro campo no clave.

### BCNF (Forma Normal de Boyce-Codd)  
- **Requisito:** Cada determinante debe ser una clave candidata (no debe haber dependencias que violen la estructura de la clave).
- **Cumplimiento:** Todas las dependencias funcionales en el esquema son válidas en función de las claves. Por ejemplo, en la tabla `Juego`, la combinación de `id_olimpiada`, `id_deportista`, y `id_disciplina` determina `asistente`, cumpliendo con la normalización en BCNF.

## Resumen  
Este esquema de base de datos cumple hasta la **3FN** y posiblemente **BCNF**, lo cual garantiza una estructura sin redundancias ni dependencias transitivas, proporcionando una organización de datos más eficiente y menos propensa a errores.
