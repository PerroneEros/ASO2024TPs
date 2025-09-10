const Joi = require('joi');

const loginSchema = Joi.object({
    email: Joi.string().email().required(),
    password: Joi.string().min(8).required()
});

const registroSchema = Joi.object({
    dni: Joi.string().required(),
    nombre: Joi.string().required(),
    apellido: Joi.string().required(),
    email: Joi.string().email().required(),
    password: Joi.string().required()
});

module.exports = {
    loginSchema,
    registroSchema
};
