function validarFormulario(event) {
    event.preventDefault();
    const nombre = document.getElementById('nombre').value.trim();
    const email = document.getElementById('email').value.trim();
    const mensaje = document.getElementById('mensajeError');

    if (nombre === '' || email === '') {
        mensaje.textContent = 'Por favor, completa todos los campos.';
    } else {
        mensaje.textContent = '';
        alert('Formulario enviado con éxito');
    }
}