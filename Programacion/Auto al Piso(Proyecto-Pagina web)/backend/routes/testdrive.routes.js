import express from 'express';
import { body } from "express-validator";
import {
  agendarTestDrive,
  obtenerTestDrives
} from '../controllers/testdrive.controller.js';

const router = express.Router();

router.post(
  "/",
  [
    body("nombre").notEmpty().withMessage("El nombre es obligatorio"),
    body("email").isEmail().withMessage("Email inválido"),
    body("telefono").isLength({ min: 8 }).withMessage("Teléfono inválido"),
    body("fecha").notEmpty().withMessage("La fecha es obligatoria"),
    body("vehiculo").notEmpty().withMessage("Selecciona un vehículo"),
    body("sucursal").notEmpty().withMessage("Selecciona una sucursal")
  ],
  agendarTestDrive
);

router.get('/', obtenerTestDrives);

export default router;
