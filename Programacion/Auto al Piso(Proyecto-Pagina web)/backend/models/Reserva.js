import mongoose from 'mongoose';

const reservaSchema = new mongoose.Schema({
  nombre: { type: String, required: true },
  email: { type: String, required: true },
  telefono: String,
  modelo: { type: String, required: true },
  fechaReserva: Date,
  comentarios: String,
  creadoEn: { type: Date, default: Date.now }
});

export default mongoose.model('Reserva', reservaSchema);
