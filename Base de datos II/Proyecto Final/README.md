# Proyecto: "Cursos Online"
- Para el **proyecto final**, hicimos un sistema para manejar cursos online. Usando **Node.js**, **Express** y **MongoDB** (con Mongoose) para crear una **API RESTful** que te deja hacer de todo: desde registrar cursos y estudiantes, hasta matricularlos y luego revisar o actualizar la info. Podés usar Postman o cualquier cliente HTTP para interactuar con él


# Instalación

```ruby
git clone https://github.com/Juan-Pedro-Kessler/tup-basdat-2/jsjs.git
cd Cursos Online
```

### Instalar dependencias

```ruby
npm install
npm install express mongoose nodemon
```

### Configurar las variables de entorno en el archivo `.env`

```ruby
MONGO_URI=mongodb://localhost:27017/cursos_online
PORT=3000
```

### Iniciar el servidor

```ruby
npm run dev
```

# Estructuras de carpetas

```ruby
\---Proyecto Final
    |   README.md
    |   
    \---Cursos Online
        |   .env
        |   index.js
        |   package-lock.json
        |   package.json
        |   
        +---config
        |       db.js
        |       
        +---controllers
        |       cursoController.js
        |       matriculaController.js
        |       
        +---middlewares
        +---models
        |       curso.js
        |       estudiante.js
        |       matricula.js
        |       
        \---routes
                cursoRoutes.js
                estudianteRoutes.js
                matriculaRoutes.js
```

# Rutas disponibles

## Cursos (`/api/cursos`)

**POST** /

Crear un nuevo curso
- ![Imagen de WhatsApp 2025-07-15 a las 18 46 02_ac5a8b74](https://github.com/user-attachments/assets/2c51dfe7-357f-48bc-aefd-3e4fb4918261)

**GET** /

Obtener todos los cursos
- ![Imagen de WhatsApp 2025-07-15 a las 18 46 43_fb1d82c9](https://github.com/user-attachments/assets/a7f1de9b-733c-462f-9384-e11375fb0fae)

**GET** /:id

Obtener un curso por su ID
- ![Imagen de WhatsApp 2025-07-15 a las 18 47 06_5f3b9544](https://github.com/user-attachments/assets/f425cb3e-a03e-4a97-9502-a194144c39fa)

**PUT** /:id

Actualizar un curso por su ID
- ![Imagen de WhatsApp 2025-07-15 a las 18 48 15_98e75091](https://github.com/user-attachments/assets/47907b4f-62e4-4213-a668-cb13a3735a28)

**DELETE** /:id

Eliminar un curso por su ID
- ![Imagen de WhatsApp 2025-07-15 a las 18 49 04_ecf38cb3](https://github.com/user-attachments/assets/c149f9ff-c023-4c29-94fb-37b3e44310e6)


## Matrículas (`/api/matriculas`)

**POST** /

Crear un nuevo curso
- <img width="860" height="761" alt="image" src="https://github.com/user-attachments/assets/9bae41df-912f-430a-b933-b7318bed9cd9" />

**GET** /

Obtener todos los cursos
- ![Imagen de WhatsApp 2025-07-15 a las 18 44 22_0129fc98](https://github.com/user-attachments/assets/2e6ee60f-57f4-4dc4-996e-419c95c2ca37)

**GET** /:id

Obtener un curso por su ID
- <img width="749" height="696" alt="image" src="https://github.com/user-attachments/assets/1c598779-fb22-4bb2-9ee8-c6da7b1e1a02" />

**PUT** /:id

Actualizar un curso por su ID
- <img width="790" height="684" alt="image" src="https://github.com/user-attachments/assets/5d0ee6e4-c962-4518-b0cf-1a3ff3e0d893" />

**DELETE** /:id

Eliminar un curso por su ID
- ![Imagen de WhatsApp 2025-07-15 a las 18 44 46_de249cef](https://github.com/user-attachments/assets/68eb9e12-95a2-456d-abee-ab23032c1ae0)


## Estudiantes (``/api/estudiantes``)

**POST** /

Crear un nuevo estudiante
- ![Imagen de WhatsApp 2025-07-15 a las 18 52 20_16899a40](https://github.com/user-attachments/assets/2a9b1840-cc98-4455-82a5-2515ccc21921)

**GET** /

Obtener todos los estudiantes
- ![Imagen de WhatsApp 2025-07-15 a las 18 53 16_60886254](https://github.com/user-attachments/assets/403599a3-c8f8-462c-a1fa-215ffef6d087)


# Tecnologías utilizadas

```ruby
Node.js
Express
MongoDB (Mongoose)
Nodemon (desarrollo)
Postman (para pruebas en API)
```
--------------------------------
# Integrantes:
- Franco Devaux
- Juan Pedro Kessler
- Lautaro Acosta
- Eros Perrone
