const { Paciente } = require('./entities/paciente.entity.js');

const create = async (data) => await Paciente.create(data);

const findByEmail = async (email, password) => {
  return await Paciente.findOne({ where: { email, password } });
};

const getByEmail = async (email) => {
  return await Paciente.findOne({ where: { email } });
};


const getAll = async () => await Paciente.findAll();

const getById = async (id) => await Paciente.findByPk(id);

const update = async (id, data) => {
  const paciente = await Paciente.findByPk(id);
  if (!paciente) return null;
  return await paciente.update(data);
};

const remove = async (id) => {
  const paciente = await Paciente.findByPk(id);
  if (!paciente) return null;
  await paciente.destroy();
  return paciente;
};

module.exports = {
  create,
  findByEmail,
  getAll,
  getById,
  getByEmail,
  update,
  remove
};

