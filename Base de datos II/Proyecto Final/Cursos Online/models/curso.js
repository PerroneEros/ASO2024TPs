const mongoose = require('mongoose');

const leccionSchema = new mongoose.Schema({
  nombre: String
});

const moduloSchema = new mongoose.Schema({
  nombre: String,
  lecciones: [leccionSchema]
});

const cursoSchema = new mongoose.Schema({
  nombre: String,
  descripcion: String,
  instructor: String,
  duracionHoras: Number,
  precio: Number,
  modulos: [moduloSchema]
});

module.exports = mongoose.model('Curso', cursoSchema);
