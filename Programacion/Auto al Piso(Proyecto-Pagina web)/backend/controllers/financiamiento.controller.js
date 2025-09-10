import { validationResult } from 'express-validator';

export const simularFinanciamiento = (req, res) => {
  const errores = validationResult(req);
  if (!errores.isEmpty()) {
    return res.status(400).json({ errores: errores.array() });
  }

  const { monto, cuotas, tasa } = req.body;

  if (!monto || !cuotas || tasa === undefined) {
    return res.status(400).json({ mensaje: 'Faltan parámetros' });
  }

  const tasaMensual = tasa / 100;
  const cuota = (monto * tasaMensual) / (1 - Math.pow(1 + tasaMensual, -cuotas));

  res.json({
    monto,
    cuotas,
    tasa,
    cuotaMensual: Math.round(cuota * 100) / 100,
    totalPagado: Math.round(cuota * cuotas * 100) / 100
  });
};
