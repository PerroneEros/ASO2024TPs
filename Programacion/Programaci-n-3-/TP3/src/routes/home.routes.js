const { Router } = require('express');
const {
  home,
  mostrarLogin,
  mostrarRegistro,
  mostrarVistaTurnos,
  registrarPaciente,
  loginPaciente,
  renderListaPacientes
} = require('../controllers/home/home.controller.js');

const rutaHome = Router();

rutaHome.get('/', home);
rutaHome.get('/login', mostrarLogin);
rutaHome.get('/register', mostrarRegistro);
rutaHome.get('/listaPacientes', renderListaPacientes);
rutaHome.get('/turnos/vista', mostrarVistaTurnos);
rutaHome.post('/register', registrarPaciente);
rutaHome.post('/login', loginPaciente);

module.exports = rutaHome;