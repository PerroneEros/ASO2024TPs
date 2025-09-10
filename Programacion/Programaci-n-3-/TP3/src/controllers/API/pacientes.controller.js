const pacientesModel = require("../../models/sqlite/paciente.model.js");

class PacientesController {
  async list(req, res) {
    const pacientes = await pacientesModel.getAll();
    res.status(200).json(pacientes);
  }

  async create(req, res) {
    const data = req.body;
    const nuevo = await pacientesModel.create(data);
    res.status(201).json(nuevo);
  }

  async delete(req, res) {
    const eliminado = await pacientesModel.remove(req.params.id);
    if (!eliminado) {
      return res.status(404).json({ message: "Paciente no encontrado" });
    }
    res.status(200).json(eliminado);
  }

  async update(req, res) {
    const actualizado = await pacientesModel.update(req.params.id, req.body);
    if (!actualizado) {
      return res.status(404).json({ message: "Paciente no encontrado" });
    }
    res.status(200).json(actualizado);
  }

  async getPerfil(req, res) {
    try {
      const paciente = await pacientesModel.getByEmail(req.user.email);
      if (!paciente) {
        return res.status(404).json({ message: "Paciente no encontrado" });
      }
      res.status(200).json(paciente);
    } catch (error) {
      res.status(500).json({ message: "Error al obtener perfil", error: error.message });
    }
  }

}

module.exports = new PacientesController();
