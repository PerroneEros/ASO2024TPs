import express from 'express';
import { verificarEstadoMongo } from '../controllers/health.controller.js';

const router = express.Router();

router.get('/', verificarEstadoMongo);

export default router;
