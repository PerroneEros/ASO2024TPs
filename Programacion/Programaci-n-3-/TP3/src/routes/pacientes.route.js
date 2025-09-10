const { Router } = require('express');
const pacientesController = require('../controllers/API/pacientes.controller.js');
const autenticadorController = require('../controllers/API/autenticacion.controller.js');
const { verifyTokenMiddleware } = require('../middlewares/verifyToken.middleware.js');
const validar = require('../middlewares/joi.middleware.js');
const { loginSchema, registroSchema } = require('../schemas/pacientes.schema.js');

const rutaPacientes = Router();

rutaPacientes.get('/', verifyTokenMiddleware, pacientesController.list);
rutaPacientes.get('/me', verifyTokenMiddleware, pacientesController.getPerfil);
rutaPacientes.post('/login', validar(loginSchema), autenticadorController.login);
rutaPacientes.post('/', validar(registroSchema), pacientesController.create);
rutaPacientes.put('/:id', verifyTokenMiddleware, pacientesController.update);
rutaPacientes.delete('/:id', verifyTokenMiddleware, pacientesController.delete);

module.exports = rutaPacientes;