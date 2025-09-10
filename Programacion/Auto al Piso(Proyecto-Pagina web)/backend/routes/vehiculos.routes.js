import express from 'express';
import {
  obtenerVehiculos,
  crearVehiculo,
  obtenerVehiculoPorId,
  actualizarVehiculo,
  eliminarVehiculo
} from '../controllers/vehiculos.controller.js';

const router = express.Router();

router.get('/', obtenerVehiculos);
router.post('/', crearVehiculo);
router.get('/:id', obtenerVehiculoPorId);
router.put('/:id', actualizarVehiculo);
router.delete('/:id', eliminarVehiculo);

export default router;
