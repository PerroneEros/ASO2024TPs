#!/bin/bash

# Solicita al usuario que ingrese un nombre
read -p "Ingrese un nombre: " nombre

# Solicita la API de agify.io y guarda la respuesta
respuesta=$(curl -s "https://api.agify.io/?name=$nombre")

# Extrae la edad probable del JSON, hay que instalar el comando jq 
edadProbable=$(echo "$respuesta" | jq -r '.age')

# Verifica si se puede determinar, por ejemplo al poner un numero da error
if [ "$edadProbable" = "null" ]; then
    echo "Error, no se pudo determinar la edad probable para el nombre \"$nombre\"."
else
    echo "La edad probable para el nombre \"$nombre\" es: $edadProbable"
fi
