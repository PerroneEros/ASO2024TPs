function cambiarColorFondo() {
    const colores = ['#ffadad', '#caffbf', '#9bf6ff', '#bdb2ff', '#ffd6a5'];
    const colorAleatorio = colores[Math.floor(Math.random() * colores.length)];
    document.body.style.backgroundColor = colorAleatorio;
}