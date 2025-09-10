let contador = 0;

function actualizarContador() {
    document.getElementById('contador').textContent = contador;
}

function sumar() {
    contador++;
    actualizarContador();
}

function restar() {
    contador--;
    actualizarContador();
}

function reiniciar() {
    contador = 0;
    actualizarContador();
}