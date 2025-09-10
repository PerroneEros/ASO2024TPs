# Consulta_Medic# 🏥 Proyecto: Clínica Salud+ - Gestión de Turnos Médicos

## 🔧 Tecnologías utilizadas

- Backend: **Node.js** + **Express**
- Motor de plantillas: **EJS**
- Autenticación: **JWT**
- Validación de datos: **Joi**
- Herramientas de testing de API: **Postman**
- Base de datos: **SQLite3**

# Estructuras de las Carpetas

```ruby
├───.vscode
└───src
    ├───config
    ├───controllers
    │   ├───API
    │   └───home
    ├───middlewares
    ├───models
    │   └───sqlite
    │       ├───config
    │       │   └───db
    │       └───entities
    ├───public
    ├───routes
    ├───schemas
    └───views
        ├───ejs
        └───pug
```

# Pruebas en Postman
Probamos las rutas principales con Postman para validar que el backend funcione correctamente:

- Crear pacientes
- Hacer login y obtener token
- Crear turnos (protegido con JWT)
- Consultar turnos por paciente
- Cancelar turnos

# Organización de las vistas

![Imagen de WhatsApp 2025-06-08 a las 19 56 54_3422273b](https://github.com/user-attachments/assets/41e87e84-26e0-4e37-a5fc-d13c549135e4)
![Imagen de WhatsApp 2025-06-08 a las 19 57 03_790b3b66](https://github.com/user-attachments/assets/453259f3-c603-45c4-ad0e-a89a3de5d1c8)
![Imagen de WhatsApp 2025-06-08 a las 19 57 09_8fef34b1](https://github.com/user-attachments/assets/8cf5f4cc-e489-4347-9592-d233f26be266)
![Imagen de WhatsApp 2025-07-01 a las 17 18 00_ee3b2b02](https://github.com/user-attachments/assets/33140e51-42e5-48c7-ac6b-15048962ddfd)
![Imagen de WhatsApp 2025-07-01 a las 17 19 03_ed78c060](https://github.com/user-attachments/assets/61f1fbf6-ef22-4831-8c8e-7f699fc458cb)
![Imagen de WhatsApp 2025-07-01 a las 17 21 14_fe2a2644](https://github.com/user-attachments/assets/38d5bf66-d568-41fc-9990-3cc703275cda)
![Imagen de WhatsApp 2025-07-01 a las 17 21 29_043bcc46](https://github.com/user-attachments/assets/41d2f524-2fa0-4496-9ceb-9de29dd3d98e)

----------------------------------
# ENDPOINTS

## Endpoint para **"Home"**

`GET /`
![HOME]

`GET /login`
![LOGIN]

`GET /register`
![REGISTER]

`GET /listaPacientes`
![LISTA PACIENTES]

`GET /turnos/vista`
![VISTA TURNOS]

`POST /register`
![REGISTRO PACIENTE (POST)]

`POST /login`
![LOGIN PACIENTE (POST)]

---

## Endpoint para **"Pacientes"**

`GET /api/v1/pacientes`  
*Requiere token*
![GET pacientes]

`GET /api/v1/pacientes/me`  
*Requiere token*
![GET perfil paciente]

`POST /api/v1/pacientes/login`  
*Valida con loginSchema*
![POST login paciente]

`POST /api/v1/pacientes`  
*Valida con registroSchema*
![POST crear paciente]

`PUT /api/v1/pacientes/:id`  
*Requiere token*
![PUT actualizar paciente]

`DELETE /api/v1/pacientes/:id`  
*Requiere token*
![DELETE paciente]

---

## Endpoint para **"Turnos"**

`GET /api/v1/turnos/:idPaciente`  
*Requiere token*
![GET turnos por paciente]

`POST /api/v1/turnos`  
*Requiere token*
![POST crear turno]

`DELETE /api/v1/turnos/:idTurno`  
*Requiere token*
![DELETE cancelar turno]


# INSTALACIÓN DEL PROYECTO

1. Lo primero seria clonar el repo

```js
git clone https://github.com/fashur12/Programaci-n-3-.git
```

2.Instalar

```ruby
node https://nodejs.org/es
```

3. Instalar sus dependencias

```ruby
npm install
npm install joi
npm i jasonwebtoken
npm install sqlite3
npm install dotenv
```

4. Iniciar el proyecto

```ruby
npm run dev
```

5. Extenciones opcionales (VsCode)

```ruby
-sqlite
-sqlite viewer
-express
-ejs
-nodejs
```
-----------------------------
## Intengrantes Del Grupo:

- Joaquin Benamo
- Fausto Desch
- Franco Devaux
- Eros Perrone
