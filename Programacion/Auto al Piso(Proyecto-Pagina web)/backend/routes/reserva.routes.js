import express from 'express';
import { body } from 'express-validator';
import { crearReserva, obtenerReservas } from '../controllers/reserva.controller.js';

const router = express.Router();

router.get('/', obtenerReservas);

router.post(
  '/',
  [
    body('nombre').notEmpty().withMessage('El nombre es obligatorio'),
    body('email').isEmail().withMessage('Email inválido'),
    body('modelo').notEmpty().withMessage('El modelo es obligatorio')
  ],
  crearReserva
);

export default router;
