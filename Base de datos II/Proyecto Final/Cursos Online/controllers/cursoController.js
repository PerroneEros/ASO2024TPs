const Curso = require('../models/curso');

exports.getAll = async (req, res) => {
  const cursos = await Curso.find();
  res.json(cursos);
};

exports.getById = async (req, res) => {
  const curso = await Curso.findById(req.params.id);
  res.json(curso);
};

exports.create = async (req, res) => {
  const nuevoCurso = new Curso(req.body);
  await nuevoCurso.save();
  res.status(201).json(nuevoCurso);
};

exports.update = async (req, res) => {
  const curso = await Curso.findByIdAndUpdate(req.params.id, req.body, { new: true });
  res.json(curso);
};

exports.delete = async (req, res) => {
  await Curso.findByIdAndDelete(req.params.id);
  res.status(204).send();
};
