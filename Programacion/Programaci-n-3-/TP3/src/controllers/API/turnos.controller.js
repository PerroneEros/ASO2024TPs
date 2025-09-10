const turnosModel = require('../../models/sqlite/turnos.model.js');
const pacientesModel = require('../../models/sqlite/paciente.model.js');

class TurnosController {
  async obtenerTurnosPorPaciente(req, res) {
    try {
      const idPaciente = req.params.idPaciente;
      const turnos = await turnosModel.obtenerTurnosPorPaciente(idPaciente);
      if (!turnos || turnos.length === 0) {
        return res.status(404).json({ message: 'No se encontraron turnos' });
      }
      res.status(200).json(turnos);
    } catch (error) {
      res.status(500).json({ message: 'Error al obtener turnos', error: error.message });
    }
  }

  async cancelarTurno(req, res) {
    try {
      const idTurno = req.params.idTurno;
      const turnoCancelado = await turnosModel.cancelarTurno(idTurno);
      if (!turnoCancelado) {
        return res.status(404).json({ message: 'Turno no encontrado o ya cancelado' });
      }
      res.status(200).json({ message: 'Turno cancelado correctamente', turnoCancelado });
    } catch (error) {
      res.status(500).json({ message: 'Error al cancelar turno', error: error.message });
    }
  }

  async crearTurno(req, res) {
    try {
      console.log("Usuario autenticado:", req.user);
      console.log("Datos recibidos:", req.body);

      const { nombre, fecha, hora, email } = req.body;
      const idPaciente = req.user?.id;

      if (!idPaciente) {
        return res.status(401).json({ message: 'Token inválido o no contiene ID' });
      }

      if (!nombre || !fecha || !hora || !email) {
        return res.status(400).json({ message: 'Todos los campos son obligatorios' });
      }

      const nuevoTurno = await turnosModel.crearTurno(idPaciente, nombre, email, fecha, hora);
      console.log("Turno creado:", nuevoTurno);

      res.status(201).json({ message: 'Turno registrado correctamente', turno: nuevoTurno });
    } catch (error) {
      console.error("Error al crear turno:", error);
      res.status(500).json({ message: 'Error al crear turno', error: error.message });
    }
  }


  async mostrarVistaTurnos(req, res) {
    try {
      const paciente = await pacientesModel.getById(req.user.id);
      const medicoNombre = `${paciente.nombre} ${paciente.apellido}`;
      res.render('turnos', { medicoNombre });
    } catch (error) {
      res.status(500).send('Error al cargar turnos');
    }
  }
}

module.exports = new TurnosController();
