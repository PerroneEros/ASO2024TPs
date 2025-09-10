import Promocion from '../models/Promocion.js';
import { validationResult } from 'express-validator';

export const crearPromocion = async (req, res) => {
  const errores = validationResult(req);
  if (!errores.isEmpty()) {
    return res.status(400).json({ errores: errores.array() });
  }

  try {
    const promo = new Promocion(req.body);
    const guardada = await promo.save();
    res.status(201).json(guardada);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

export const obtenerPromocionesActivas = async (req, res) => {
  try {
    const hoy = new Date();
    const promociones = await Promocion.find({
      desde: { $lte: hoy },
      hasta: { $gte: hoy }
    });
    res.json(promociones);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

export const obtenerTodasPromociones = async (req, res) => {
  try {
    const promos = await Promocion.find().sort({ creadoEn: -1 });
    res.json(promos);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};
