const jwt = require('jsonwebtoken');
const config = require('../../config/config.js');
const pacientesModel = require('../../models/sqlite/paciente.model.js');

class AutenticadorController {
    async login(req, res) {
        try {
            const { email, password } = req.body;
            const user = await pacientesModel.findByEmail(email, password);
            if (!user) {
                return res.status(401).json({ message: "Credenciales inválidas" });
            }

            const token = jwt.sign({ id: user.id, email: user.email }, config.secreteWord, { expiresIn: config.expiresIn });

            res.status(200).json({ token });
        } catch (error) {
            res.status(500).json({ message: "Error en el login", error: error.message });
        }
    }
}

module.exports = new AutenticadorController();
