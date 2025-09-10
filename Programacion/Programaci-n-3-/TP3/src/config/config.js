const  dotenv = require('dotenv');
dotenv.config()
class Config {
    constructor(){
        //TODO: verificar que existean las constantes del .env       
        this.secreteWord= process.env.SECRETE_WORD;
        this.expiresIn = process.env.EXPIRES_IN;
    }
}
module.exports = new Config();