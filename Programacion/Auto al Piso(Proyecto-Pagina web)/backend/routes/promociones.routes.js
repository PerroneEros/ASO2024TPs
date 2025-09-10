import express from "express";
import { body } from "express-validator";
import {
  crearPromocion,
  obtenerPromocionesActivas,
  obtenerTodasPromociones
} from "../controllers/promociones.controller.js";

const router = express.Router();

router.post(
  "/",
  [
    body("titulo").notEmpty().withMessage("El título es obligatorio"),
    body("vehiculo.precioOriginal").isNumeric().withMessage("Precio original inválido"),
    body("vehiculo.precioConDescuento").isNumeric().withMessage("Precio con descuento inválido"),
    body("desde").notEmpty().withMessage("Fecha de inicio requerida"),
    body("hasta").notEmpty().withMessage("Fecha de finalización requerida")
  ],
  crearPromocion
);

router.get("/", obtenerPromocionesActivas);
router.get("/todas", obtenerTodasPromociones);

export default router;
