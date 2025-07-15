const mongoose = require('mongoose');

const progresoSchema = new mongoose.Schema({
  leccionesCompletadas: [String],
  porcentajeAvance: Number,
  calificacionFinal: Number,
});

const matriculaSchema = new mongoose.Schema({
  estudianteId: mongoose.Schema.Types.ObjectId,
  cursoId: mongoose.Schema.Types.ObjectId,
  fechaMatricula: { type: Date, default: Date.now },
  progreso: progresoSchema,
  completado: Boolean
});

module.exports = mongoose.model('Matricula', matriculaSchema);
