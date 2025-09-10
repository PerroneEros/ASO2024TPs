import mongoose from 'mongoose';

const EvaluacionSchema = new mongoose.Schema({
  nombre: { type: String },
  email: { type: String },
  telefono: { type: String },
  patente: { type: String, required: true },
  marca: { type: String },
  modelo: { type: String },
  anio: { type: Number },
  kilometros: { type: Number },
  estado: { type: String },
  fotos: [{ type: String }],
  creadoEn: { type: Date, default: Date.now }
});

export default mongoose.model('Evaluacion', EvaluacionSchema);
