import TestDrive from '../models/TestDrive.js';
import { validationResult } from 'express-validator';

export const agendarTestDrive = async (req, res) => {
  const errores = validationResult(req);
  if (!errores.isEmpty()) {
    return res.status(400).json({ errores: errores.array() });
  }

  try {
    const nuevo = new TestDrive(req.body);
    const guardado = await nuevo.save();
    res.status(201).json(guardado);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

export const obtenerTestDrives = async (req, res) => {
  try {
    const testDrives = await TestDrive.find().sort({ fecha: -1 });
    res.json(testDrives);
  } catch (err) {
    res.status(500).json({ mensaje: 'Error al obtener datos', error: err.message });
  }
};
