const express = require('express');
const conectarDB = require('./config/db');
const app = express();

// Middlewares
app.use(express.json());

// Conexión a DB
conectarDB();

// Rutas
app.use('/api/matriculas', require('./routes/matriculaRoutes'));
app.use('/api/estudiantes', require('./routes/estudianteRoutes'));
app.use('/api/cursos', require('./routes/cursoRoutes'));

// Arrancar servidor
const PORT = 3000;
app.listen(PORT, () => console.log(`Servidor corriendo en puerto ${PORT}`));