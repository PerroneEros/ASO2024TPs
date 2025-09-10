import Evaluacion from '../models/Evaluacion.js';
import { validationResult } from 'express-validator';

export const crearEvaluacion = async (req, res) => {
  const errores = validationResult(req);
  if (!errores.isEmpty()) {
    return res.status(400).json({ errores: errores.array() });
  }

  try {
    const fotos = req.files?.map(file => file.filename) || [];
    const evaluacion = new Evaluacion({
      ...req.body,
      fotos
    });

    const guardada = await evaluacion.save();
    res.status(201).json(guardada);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

export const obtenerEvaluaciones = async (req, res) => {
  try {
    const datos = await Evaluacion.find().sort({ creadoEn: -1 });
    res.json(datos);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};
