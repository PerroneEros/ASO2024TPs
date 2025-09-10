# 🚗 Auto al Piso

Simulador automotriz Full-Stack con reserva de test-drive, simulación de cuotas, catálogo de vehículos y promociones.  
Backend en Node.js/Express, frontend en React/Vite, MongoDB, todo orquestado con Docker y servido vía Nginx.

---

## 🔧 Tecnologías

### Backend  
- Express  
- Mongoose / MongoDB  
- Multer (subida de archivos)  

### Frontend  
- React v18+  
- Vite  
- CSS puro  

### Infraestructura  
- Docker & Docker Compose  
- Nginx (proxy inverso)  
- MongoDB  

---

## 📁 Estructura del Proyecto

```text
.
├── backend
│   ├── controllers
│   ├── models
│   ├── routes
│   ├── server.js
│   └── Dockerfile.dev
├── frontend
│   ├── public
│   ├── src
│   │   ├── components
│   │   └── App.jsx
│   ├── vite.config.js
│   ├── package.json
│   └── Dockerfile.dev
├── nginx
│   └── nginx.conf
├── docker-compose.yml
└── README.md
```

---

## 🚀 Puesta en Marcha

### 🧰 Requisitos Previos
- Docker ≥ 20.10  
- Docker Compose ≥ 1.29

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/auto-al-piso.git
cd auto-al-piso
```

### 2. Variables de entorno

Crear un archivo `.env` en la carpeta `backend`:

```ini
MONGO_URI=mongodb://mongo:27017/autosalpiso
PORT=5000
```

### 3. Levantar con Docker

```bash
docker-compose down -v
docker-compose up --build
```

- MongoDB → `mongodb://localhost:27017/autosalpiso`  
- Backend API → `http://localhost/api/...`  
- Frontend SPA → `http://localhost/`

---

## 📸 Capturas del Proyecto

### 🏠 Página principal

![Home](./capturas/galeria.jpeg)

---

### 📷 Galería de vehículos

![Galería](./capturas/galeria.jpeg)

---

### 📝 Evaluación de vehículos

![Evaluación 1](./capturas/evaluacion1.jpeg)  
![Evaluación 2](./capturas/evaluacion2.jpeg)

---

### 📊 Vista de evaluaciones

![Evaluaciones](./capturas/evaluaciones.jpeg)

---

### 💰 Simulador de financiación

![Simulador](./capturas/simulador.jpeg)

---

### 🔍 Comparador de vehículos

![Comparador](./capturas/comparar.jpeg)

---

### 🎉 Promociones activas

![Promociones](./capturas/promociones.jpeg)

---

### 📅 Reserva desde promociones

![Reserva desde promoción](./capturas/reserva_promociones.jpeg)

---

### 📆 Formulario de reserva

![Reserva 1](./capturas/reserva1.jpeg)  
![Reserva 2](./capturas/reserva2.jpeg)

---

### 📋 Vista de reservas

![Reservas](./capturas/reservas.jpeg)

---

### 🚘 Test Drive

![Test Drive 1](./capturas/testdrive1.jpeg)  
![Test Drive 2](./capturas/testdrive2.jpeg)

---

### 📞 Contacto y mapa

![Contacto 1](./capturas/contacto1.jpeg)  
![Contacto 2](./capturas/contacto2.jpeg)

---

### 💬 Chatbot flotante

![Chatbot](./capturas/chatbot.jpeg)

---

## 🧪 CRUD de Vehículos (Postman)

### ✅ POST

![POST](./capturas/POST.jpeg)

### ✅ GET

![GET](./capturas/GET.jpeg)

### ✅ PUT

![PUT](./capturas/PUT.jpeg)

### ✅ DELETE

![DELETE](./capturas/DEL.jpeg)

---

## 📜 Endpoints Principales

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET    | /api/vehiculos                     | Listar todos los vehículos |
| POST   | /api/vehiculos                     | Crear un nuevo vehículo |
| GET    | /api/testdrive                     | Listar turnos de test-drive |
| POST   | /api/testdrive                     | Agendar un test-drive |
| GET    | /api/evaluacion                    | Listar evaluaciones |
| POST   | /api/evaluacion                    | Crear evaluación con fotos (multipart) |
| POST   | /api/chatbot                       | Consultar asistente virtual |
| GET    | /api/promociones                   | Listar promociones |
| POST   | /api/promociones                   | Crear una promoción |
| POST   | /api/financiamiento/simular        | Simular plan de financiamiento |
| GET    | /api/reservas                      | Listar reservas |
| POST   | /api/reservas                      | Crear una reserva |

---

## 🌐 Rutas de Frontend

| Ruta              | Componente   | Descripción                        |
|-------------------|--------------|------------------------------------|
| `/`               | Home         | Página principal                   |
| `/galeria`        | Galería      | Listado de vehículos               |
| `/evaluaciones`   | Evaluaciones | Ver evaluaciones de autos          |
| `/reservas`       | Reservas     | Ver y crear reservas               |
| `/promociones`    | Promociones  | Listado de promociones             |
| `/contacto`       | Contacto     | Formulario de contacto             |
| `/simulador`      | Simulador    | Cálculo de cuotas                  |
| `/comparar`       | Comparador   | Comparación entre vehículos        |

---

## 🎯 Mejoras Futuras

- Autenticación y roles (admin/cliente)
- Paginación y filtros en listados
- Validación avanzada y notificaciones por email/WhatsApp
- Animaciones, transiciones y diseño responsivo
- Deploy a un entorno en la nube (AWS, DigitalOcean)

---

## 🤝 Contribuciones

1. Haz un **fork**
2. Crea una rama:
   ```bash
   git checkout -b feature/mi-mejora
   ```
3. Haz commit y push:
   ```bash
   git push origin feature/mi-mejora
   ```
4. Abre un **Pull Request**

---

📌 Proyecto con fines educativos — “**Auto al Piso**” 🚗
