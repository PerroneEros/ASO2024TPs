
// -----------------------EJERCICIO 5--------------------------------

// Crear referencias a los elementos del formulario
const form = document.createElement("form");
form.id = "formularioValidacion";
form.innerHTML = `
    <h2>Formulario de Validación</h2>
    <label for="nombre">Nombre:</label>
    <input type="text" id="nombre"><br>
    <span class="error" id="errorNombre"></span><br>

    <label for="email">Email:</label>
    <input type="email" id="email"><br>
    <span class="error" id="errorEmail"></span><br>

    <label for="edad">Edad:</label>
    <input type="number" id="edad"><br>
    <span class="error" id="errorEdad"></span><br>

    <button type="submit">Enviar</button>
`;

document.body.appendChild(form);

const errorNombre = document.getElementById("errorNombre");
const errorEmail = document.getElementById("errorEmail");
const errorEdad = document.getElementById("errorEdad");

form.addEventListener("submit", function (e) {
    e.preventDefault();

    const nombre = document.getElementById("nombre").value.trim();
    const email = document.getElementById("email").value.trim();
    const edad = parseInt(document.getElementById("edad").value);

    errorNombre.textContent = "";
    errorEmail.textContent = "";
    errorEdad.textContent = "";

    let valido = true;

    if (!nombre) {
        errorNombre.textContent = "El nombre es obligatorio.";
        valido = false;
    }

    if (!email || !/^\S+@\S+\.\S+$/.test(email)) {
        errorEmail.textContent = "El email no es válido.";
        valido = false;
    }

    if (!edad || isNaN(edad) || edad <= 18) {
        errorEdad.textContent = "Debe tener más de 18 años.";
        valido = false;
    }

    if (valido) {
        alert("Formulario enviado correctamente.");
        form.reset();
    }
});
