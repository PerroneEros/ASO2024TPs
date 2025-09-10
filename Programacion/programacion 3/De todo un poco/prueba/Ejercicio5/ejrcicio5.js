function ValidarFormulario(event) {
  event.preventDefault();

  const nombre = document.getElementById("nombre").value.trim();
  const edad = document.getElementById("edad").value.trim();
  const email = document.getElementById("email").value.trim();
  const mensaje = document.getElementById("MensajeError");

  if (nombre === "" || edad === "" || email === "") {
    mensaje.textContent = "Por favor, completa todos los campos.";
  } else {
    mensaje.textContent = "";
    alert("Formulario enviado con éxito");
  }
}
