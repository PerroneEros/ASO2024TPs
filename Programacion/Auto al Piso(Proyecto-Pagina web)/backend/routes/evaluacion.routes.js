import express from "express";
import { body } from "express-validator";
import { upload } from "../middlewares/upload.js";
import {
  crearEvaluacion,
  obtenerEvaluaciones
} from "../controllers/evaluacion.controller.js";

const router = express.Router();

router.post(
  "/",
  upload.array("fotos", 5),
  [
    body("patente").notEmpty().withMessage("La patente es obligatoria"),
    body("estado").notEmpty().withMessage("El estado es obligatorio"),
    body("kilometros").isNumeric().withMessage("Kilometraje inválido")
  ],
  crearEvaluacion
);

router.get("/", obtenerEvaluaciones);

export default router;
