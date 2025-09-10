import express from 'express';
import { body } from 'express-validator';
import { simularFinanciamiento } from '../controllers/financiamiento.controller.js';

const router = express.Router();

router.post(
  '/simular',
  [
    body('monto').isNumeric().withMessage('Monto inválido'),
    body('cuotas').isInt({ min: 1 }).withMessage('Cantidad de cuotas inválida'),
    body('tasa').isNumeric().withMessage('Tasa inválida')
  ],
  simularFinanciamiento
);

export default router;
