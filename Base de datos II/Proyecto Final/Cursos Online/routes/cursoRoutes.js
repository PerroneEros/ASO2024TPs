const express = require('express');
const router = express.Router();
const Curso = require('../models/curso');

//  Crear nuevo curso
router.post('/', async (req, res) => {
  try {
    const nuevoCurso = new Curso(req.body);
    await nuevoCurso.save();
    res.status(201).json(nuevoCurso);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

//  Obtener todos los cursos
router.get('/', async (req, res) => {
  try {
    const cursos = await Curso.find();
    res.json(cursos);
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener cursos' });
  }
});

//  Obtener un curso por ID
router.get('/:id', async (req, res) => {
  try {
    const curso = await Curso.findById(req.params.id);
    if (!curso) {
      return res.status(404).json({ error: 'Curso no encontrado' });
    }
    res.json(curso);
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener el curso' });
  }
});

//  Actualizar un curso por ID
router.put('/:id', async (req, res) => {
  try {
    const cursoActualizado = await Curso.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!cursoActualizado) {
      return res.status(404).json({ error: 'Curso no encontrado' });
    }
    res.json(cursoActualizado);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

//  Eliminar un curso por ID
router.delete('/:id', async (req, res) => {
  try {
    const cursoEliminado = await Curso.findByIdAndDelete(req.params.id);
    if (!cursoEliminado) {
      return res.status(404).json({ error: 'Curso no encontrado' });
    }
    res.json({ mensaje: 'Curso eliminado' });
  } catch (error) {
    res.status(500).json({ error: 'Error al eliminar el curso' });
  }
});

module.exports = router;
