const express = require("express");
const cors = require("cors");
const app = express();
const PORT = 3000;

// Middlewares
app.use(cors());
app.use(express.json());

// Rutas
const personaRoutes = require("./routes/personaRoutes");
app.use("/personas", personaRoutes);

// Ruta de prueba
app.get("/", (req, res) => {
  res.send("¡El backend está funcionando! 🚀");
});


// Servidor
app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});