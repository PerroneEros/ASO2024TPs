const express = require('express');
const dotenv = require('dotenv');
const morgan = require('morgan');
const path = require('path');

// Rutas
const rutaPacientes = require('./routes/pacientes.route.js');
const rutaTurnos = require('./routes/turnos.route.js');
const rutaHome = require('./routes/home.routes.js');

dotenv.config();

class Server {
  constructor(template = process.env.TEMPLATE || 'ejs') {
    this.app = express();
    this.port = process.env.PORT || 3000;

    this.middleware();
    this.engine(template);
    this.routes();
  }

  engine(template) {
    try {
      require.resolve(template);
      this.app.set('view engine', template);
      this.app.set('views', path.join(__dirname, 'views', template));
    } catch (error) {
      console.error('Error al configurar el motor de plantillas:', template);
    }
  }

  middleware() {
    this.app.use(express.urlencoded({ extended: true }));
    this.app.use(express.json());
    this.app.use(morgan('dev'));
    this.app.use(express.static(path.join(__dirname, 'public')));
  }

  routes() {
    this.app.use('/', rutaHome); // Solo vistas
    this.app.use('/api/v1/pacientes', rutaPacientes); // API pacientes
    this.app.use('/api/v1/turnos', rutaTurnos); // API turnos
  }

  listen() {
    this.app.listen(this.port, () => {
      console.log(`Servidor corriendo en http://localhost:${this.port}`);
    });
  }
}

module.exports = Server;
