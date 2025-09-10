import mongoose from "mongoose";

const simulacionSchema = new mongoose.Schema({
  nombre: String,
  email: String,
  telefono: String,
  montoEntrada: Number,
  cuotas: Number,
  vehiculo: String,
  resultadoCuota: Number,
  fecha: { type: Date, default: Date.now },
});

export default mongoose.model("Simulacion", simulacionSchema);
