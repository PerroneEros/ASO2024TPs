import mongoose from 'mongoose';

const TestDriveSchema = new mongoose.Schema({
  nombre: { type: String, required: true },
  email: { type: String },
  telefono: { type: String },
  fecha: { type: Date, required: true },
  vehiculo: { type: String, required: true },
  sucursal: { type: String, required: true },
  creadoEn: { type: Date, default: Date.now }
});

export default mongoose.model('TestDrive', TestDriveSchema);
