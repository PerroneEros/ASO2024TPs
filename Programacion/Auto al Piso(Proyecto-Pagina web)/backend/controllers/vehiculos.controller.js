import Vehiculo from '../models/Vehiculo.js';

export const obtenerVehiculos = async (req, res) => {
  try {
    const filtros = req.query;
    const query = {};

    if (filtros.marca) query.marca = filtros.marca;
    if (filtros.modelo) query.modelo = filtros.modelo;
    if (filtros.tipo) query.tipo = filtros.tipo;
    if (filtros.transmision) query.transmision = filtros.transmision;
    if (filtros.combustible) query.combustible = filtros.combustible;
    if (filtros.precioMin || filtros.precioMax) {
      query.precio = {};
      if (filtros.precioMin) query.precio.$gte = Number(filtros.precioMin);
      if (filtros.precioMax) query.precio.$lte = Number(filtros.precioMax);
    }

    const vehiculos = await Vehiculo.find(query);
    res.json(vehiculos);
  } catch (err) {
    res.status(500).json({ mensaje: 'Error al obtener vehículos', error: err });
  }
};

export const crearVehiculo = async (req, res) => {
  try {
    const nuevoVehiculo = new Vehiculo(req.body);
    const guardado = await nuevoVehiculo.save();
    res.status(201).json(guardado);
  } catch (err) {
    res.status(400).json({ mensaje: 'Error al guardar vehículo', error: err });
  }
};

export const obtenerVehiculoPorId = async (req, res) => {
  try {
    const vehiculo = await Vehiculo.findById(req.params.id);
    if (!vehiculo) return res.status(404).json({ mensaje: 'Vehículo no encontrado' });
    res.json(vehiculo);
  } catch (err) {
    res.status(500).json({ mensaje: 'Error al obtener vehículo', error: err });
  }
};

export const actualizarVehiculo = async (req, res) => {
  try {
    const actualizado = await Vehiculo.findByIdAndUpdate(req.params.id, req.body, { new: true });
    res.json(actualizado);
  } catch (err) {
    res.status(400).json({ mensaje: 'Error al actualizar vehículo', error: err });
  }
};

export const eliminarVehiculo = async (req, res) => {
  try {
    await Vehiculo.findByIdAndDelete(req.params.id);
    res.json({ mensaje: 'Vehículo eliminado' });
  } catch (err) {
    res.status(500).json({ mensaje: 'Error al eliminar vehículo', error: err });
  }
};
