function cambiarTexto() {
  const frases = ["hola", "chau", "hermano", "piola", "feliz"];
  const randomIndex = Math.floor(Math.random() * frases.length);
  document.getElementById("texto").textContent = frases[randomIndex];
}
