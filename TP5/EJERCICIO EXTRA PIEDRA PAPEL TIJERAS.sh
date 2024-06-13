#!/bin/bash

# Función para elección aleatoria de la computadora
generar_eleccion_computadora() {
opciones=("Piedra" "Papel" "Tijera")
eleccion_computadora=${opciones[$RANDOM % ${#opciones[@]}]}
}

# Función para ver quien gana
determinar_ganador() {
if [ "$eleccion_usuario" == "$eleccion_computadora" ]; then
echo "Empate!"
elif [ "$eleccion_usuario" == "Piedra" ]; then
if [ "$eleccion_computadora" == "Tijera" ]; then
echo "Ganaste!"
else
echo "Perdiste!"
fi
elif [ "$eleccion_usuario" == "Papel" ]; then
if [ "$eleccion_computadora" == "Piedra" ]; then
echo "Ganaste!"
else
echo "Perdiste!"
fi
elif [ "$eleccion_usuario" == "Tijera" ]; then
if [ "$eleccion_computadora" == "Papel" ]; then
echo "Ganaste!"
else
echo "Perdiste!"
fi
else
echo "Opción inválida! Por favor elige Piedra, Papel o Tijera."
fi
}

# eleccion usuario
echo "Elige Piedra, Papel o Tijera:"
read eleccion_usuario

# eleccion de la computadora
generar_eleccion_computadora

# Muestro las elecciones
echo "Tú elegiste: $eleccion_usuario"
echo "La computadora eligió: $eleccion_computadora"

# muestro ganador
determinar_ganador
