const Server = require('./server.js');
const {connectDB} = require('./models/sqlite/config/db.js');


connectDB()
const server = new Server("ejs");

server.listen();