#!/bin/bash

# Solicitar el primer número al usuario
echo "Ingrese el primer número:"
read num1

# Solicitar el segundo número al usuario
echo "Ingrese el segundo número:"
read num2

# Solicitar la operación al usuario
echo "Ingrese la operación que desea realizar (+, -, *, /):"
read operation

# Realizar la operación y mostrar el resultado
case $operation in
+)
result=$(echo "$num1 + $num2" | bc)
echo "El resultado de $num1 + $num2 es: $result"
;;
-)
result=$(echo "$num1 - $num2" | bc)
echo "El resultado de $num1 - $num2 es: $result"
;;
\*)
result=$(echo "$num1 * $num2" | bc)
echo "El resultado de $num1 * $num2 es: $result"
;;
/)
if [ "$num2" -eq 0 ]; then
echo "Error: División por cero no permitida."
else
result=$(echo "scale=2; $num1 / $num2" | bc)
echo "El resultado de $num1 / $num2 es: $result"
fi
;;
*)
echo "Operación no válida."
;;
esac

CULADORA.txt](https://github.com/user-attachments/files/15810685/CALCULADORA.txt)
image](https://github.com/PerroneEros/ASO2024TPs/assets/166446910/17c80f89-eb01-45d9-a141-66c3e371d3d3)
![image](https://github.com/PerroneEros/ASO2024TPs/assets/166446910/0ef48e25-b98e-407e-bc00-95dd07aca20d)
