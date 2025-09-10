import mongoose from "mongoose";

const promocionSchema = new mongoose.Schema({
  titulo: { type: String, required: true },
  descripcion: String,
  imagen: String,
  descuento: Number,
  vehiculo: {
    marca: String,
    modelo: String,
    anio: Number,
    precioOriginal: Number,
    precioConDescuento: Number
  },
  desde: Date,
  hasta: Date,
  creadoEn: { type: Date, default: Date.now }
});

export default mongoose.model("Promocion", promocionSchema);
