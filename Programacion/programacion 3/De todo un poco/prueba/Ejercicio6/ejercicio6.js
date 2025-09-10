const inicio = document.getElementById("iniciar");
const pausa = document.getElementById("pausar");
const reinicio = document.getElementById("reiniciar");
const display = document.getElementById("display");

let timer = null;

let tiempo = 0;

function start() {
  timer = setInterval(function () {
    tiempo++;
    display.innerHTML = tiempo;
  }, 1000);
}

function pause() {
  clearInterval(timer);
}

function restart() {
  pause();
  tiempo = 0;
  display.innerHTML = tiempo;
}

inicio.addEventListener("click", start);
pausa.addEventListener("click", pause);
reinicio.addEventListener("click", restart);
