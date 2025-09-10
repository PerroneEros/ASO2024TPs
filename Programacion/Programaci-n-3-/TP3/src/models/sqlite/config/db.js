const { Sequelize } = require('sequelize');
const path = require('path');

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db', 'clinica.sqlite'),
  logging: false
});

const connectDB = async () => {
  try {
    await sequelize.sync();
    console.log('Base de datos sincronizada.');
  } catch (error) {
    console.error('Error conectando a la base de datos:', error);
  }
};

module.exports = { sequelize, connectDB };