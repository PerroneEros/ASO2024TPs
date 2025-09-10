import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import { connectDB } from './config/database.js';

import vehiculosRoutes from './routes/vehiculos.routes.js';
import financiamientoRoutes from './routes/financiamiento.routes.js';
import testDriveRoutes from './routes/testdrive.routes.js';
import evaluacionRoutes from './routes/evaluacion.routes.js';
import chatbotRoutes from './routes/chatbot.routes.js';
import promocionRoutes from './routes/promociones.routes.js';
import healthRoutes from './routes/health.routes.js';
import reservaRoutes from './routes/reserva.routes.js';

dotenv.config();
const app = express();
const PORT = process.env.PORT || 5000;

// Middlewares
app.use(cors());
app.use(express.json());

// Carpeta estática para las imágenes subidas
app.use('/uploads', express.static('uploads'));

// Rutas de la API
app.use('/api/vehiculos', vehiculosRoutes);
app.use('/api/financiamiento', financiamientoRoutes);
app.use('/api/testdrive', testDriveRoutes);
app.use('/api/evaluacion', evaluacionRoutes);
app.use('/api/chatbot', chatbotRoutes);
app.use('/api/promociones', promocionRoutes);
app.use('/api/health', healthRoutes);
app.use('/api/reservas', reservaRoutes);

// Conexión a Mongo y arranque del servidor
connectDB().then(() => {
  console.log('🟢 Conectado a MongoDB');
  app.listen(PORT, () => {
    console.log(`Servidor backend corriendo en http://localhost:${PORT}`);
  });
});
