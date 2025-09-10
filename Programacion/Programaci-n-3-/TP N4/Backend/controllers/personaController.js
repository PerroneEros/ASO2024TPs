const personas = require("../models/personaModel");

const getPersonas = (req, res) => {
  res.json(personas);
};

module.exports = { getPersonas };
  