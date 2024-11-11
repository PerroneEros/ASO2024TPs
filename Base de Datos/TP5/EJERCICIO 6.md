# Normalización de la Base de Datos

## 1NF (Primera Forma Normal)  
- **Requisito:** Todos los atributos deben contener valores atómicos (indivisibles), sin conjuntos ni listas en las columnas.
- **Cumplimiento:** En este esquema, cada campo almacena un valor único y atómico. Por ejemplo, `año_olimpiada`, `pais_olimpiada`, `nombre_deportista`, etc., todos son valores simples y únicos por columna.

## 2NF (Segunda Forma Normal)  
- **Requisito:** Debe estar en 1NF, y cada atributo no clave debe depender completamente de la clave primaria.
- **Cumplimiento:** La información se distribuye en tablas (`Olimpiadas`, `Deportistas`, `Disciplinas`, `Juego`) para asegurar que cada atributo depende completamente de la clave primaria de su tabla. Por ejemplo, en `Juego`, el campo `asistente` depende de la combinación de `año_olimpiada` y `nombre_deportista` (clave compuesta), cumpliendo así con la dependencia completa.

## 3NF (Tercera Forma Normal)  
- **Requisito:** Debe estar en 2NF y no debe haber dependencias transitivas (un campo no clave no debe depender de otro campo no clave).
- **Cumplimiento:** No existen dependencias transitivas en el esquema. Cada campo no clave depende directamente de la clave primaria de su tabla. Por ejemplo, `pais_deportista` en la tabla `Deportistas` depende únicamente de la clave primaria `nombre_deportista`, y no de otro campo no clave.

## BCNF (Forma Normal de Boyce-Codd)  
- **Requisito:** Cada determinante debe ser una clave candidata (no debe haber dependencias que violen la estructura de la clave).
- **Cumplimiento:** Todas las dependencias funcionales en el esquema son válidas en función de las claves. Por ejemplo, en la tabla `Juego`, la combinación de `año_olimpiada` y `nombre_deportista` determina `asistente`, cumpliendo con la normalización en BCNF.

## Resumen  
Este esquema de base de datos cumple hasta la **3NF** y posiblemente **BCNF**, lo cual garantiza una estructura sin redundancias ni dependencias transitivas, proporcionando una organización de datos más eficiente y menos propensa a errores.
