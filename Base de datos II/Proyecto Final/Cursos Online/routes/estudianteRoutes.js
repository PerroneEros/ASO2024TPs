const express = require('express');
const router = express.Router();
const Estudiante = require('../models/estudiante');

router.post('/', async (req, res) => {
  try {
    const nuevoEstudiante = new Estudiante(req.body);
    await nuevoEstudiante.save();
    res.status(201).json(nuevoEstudiante);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

router.get('/', async (req, res) => {
  const estudiantes = await Estudiante.find();
  res.json(estudiantes);
});

module.exports = router;
