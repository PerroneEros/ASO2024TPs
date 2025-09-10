const { DataTypes } = require('sequelize');
const { sequelize } = require('../sqlite/config/db.js');

const Turno = sequelize.define('Turno', {
  id: { type: DataTypes.INTEGER, autoIncrement: true, primaryKey: true },
  nombre: { type: DataTypes.STRING, allowNull: false },
  email: { type: DataTypes.STRING, allowNull: false },
  fecha: { type: DataTypes.STRING, allowNull: false },
  hora: { type: DataTypes.STRING, allowNull: false },
  pacienteId: { type: DataTypes.INTEGER, allowNull: false }
}, {
  timestamps: false
});
// Operaciones
const obtenerTurnosPorPaciente = async (idPaciente) => {
  return await Turno.findAll({ where: { pacienteId: idPaciente } });
};

const cancelarTurno = async (idTurno) => {
  const turno = await Turno.findByPk(idTurno);
  if (!turno) return null;
  await turno.destroy();
  return turno;
};

const crearTurno = async (pacienteId, nombre, email, fecha, hora) => {
  return await Turno.create({ pacienteId, nombre, email, fecha, hora });
};

module.exports = {
  Turno,
  obtenerTurnosPorPaciente,
  cancelarTurno,
  crearTurno
};
