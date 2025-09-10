import Reserva from '../models/Reserva.js';
import { validationResult } from 'express-validator';

export const crearReserva = async (req, res) => {
  const errores = validationResult(req);
  if (!errores.isEmpty()) {
    return res.status(400).json({ errores: errores.array() });
  }

  try {
    const reserva = new Reserva(req.body);
    const guardada = await reserva.save();
    res.status(201).json(guardada);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

export const obtenerReservas = async (req, res) => {
  try {
    const reservas = await Reserva.find().sort({ creadoEn: -1 });
    res.json(reservas);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};
