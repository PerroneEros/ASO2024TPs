const express = require('express');
const router = express.Router();
const controller = require('../controllers/matriculaController');

router.post('/', controller.crearMatricula);
router.get('/', controller.obtenerMatriculas);
router.get('/:id', controller.obtenerMatricula);
router.put('/:id', controller.actualizarMatricula);
router.delete('/:id', controller.eliminarMatricula);

module.exports = router;
