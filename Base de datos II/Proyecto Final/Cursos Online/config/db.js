const mongoose = require('mongoose');

const connectDB = async () => {
  try {
    await mongoose.connect('mongodb://localhost:27017/cursos', {
      useNewUrlParser: true,
      useUnifiedTopology: true
    });
    console.log('Conectado a MongoDB');
  } catch (err) {
    console.error(' Error al conectar a MongoDB', err);
    process.exit(1);
  }
};

module.exports = connectDB;
