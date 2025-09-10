const pacientesModel = require('../../models/sqlite/paciente.model.js');
const turnosModel = require('../../models/sqlite/turnos.model.js');
const jwt = require('jsonwebtoken');
const config = require('../../config/config.js');

const home = async (req, res) => {
  res.render('index', {
    title: 'Mi aplicación Express',
    message: '¡Hola desde el servidor!',
    showFeatures: true,
    features: [
      'Descripción de la característica 1',
      'Descripción de la característica 2',
      'Descripción de la característica 3'
    ]
  });
};

// Vista de login
const mostrarLogin = (req, res) => {
  res.render('login');
};

// Vista de registro
const mostrarRegistro = (req, res) => {
  res.render('register');
};

// Vista de turnos vacía
const mostrarVistaTurnos = async (req, res) => {
  try {
    res.render('turnos', {
      turnos: [], 
      medicoNombre: "" 
    });
  } catch (error) {
    console.error('Error en mostrarVistaTurnos:', error);
    res.status(500).send("Error al cargar los turnos");
  }
};

// Registro de paciente
const registrarPaciente = async (req, res) => {
  try {
    await pacientesModel.create(req.body);
    res.redirect('/login');
  } catch (err) {
    console.error("Error al registrar:", err);
    res.status(400).render('register', { error: 'No se pudo registrar el usuario.' });
  }
};

// Login de paciente
const loginPaciente = async (req, res) => {
  const { email, password } = req.body;
  try {
    const user = await pacientesModel.findByEmail(email, password);
    if (!user) throw new Error("Usuario inválido");

    const token = jwt.sign(
      { id: user.id, email: user.email },
      config.secreteWord,
      { expiresIn: config.expiresIn }
    );

    res.json({ token, id: user.id, nombre: user.nombre });
  } catch (err) {
    res.status(401).json({ error: "Credenciales inválidas" });
  }
};

// Vista de lista de pacientes
const renderListaPacientes = async (req, res) => {
  try {
    const pacientes = await pacientesModel.getAll();
    res.render('listaPacientes', { pacientes });
  } catch (error) {
    res.status(500).send("Error al cargar los pacientes");
  }
};

module.exports = {
  home,
  mostrarLogin,
  mostrarRegistro,
  mostrarVistaTurnos,
  registrarPaciente,
  loginPaciente,
  renderListaPacientes
};
