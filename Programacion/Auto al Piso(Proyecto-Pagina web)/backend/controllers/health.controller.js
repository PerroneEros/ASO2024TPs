import mongoose from 'mongoose';

export const verificarEstadoMongo = (req, res) => {
  const estado = mongoose.connection.readyState;
  const estados = ['desconectado', 'conectado', 'conectando', 'desconectando'];

  res.json({
    mongo: estados[estado],
    timestamp: new Date().toISOString()
  });
};
