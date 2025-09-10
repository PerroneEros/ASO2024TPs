/*-----------------------EJERCICIO 1--------------------------------*/ 
const titulo = document.getElementById("tituloPrincial");
titulo.textContent = "titutlo cambiado";

const parrafos = document.getElementsByClassName("parrafo");
for(let i of parrafos){
    i.style.color = "purple";
}
/* es lo mismo hacer cualquiera de los dos
for (let i = 0; i < parrafos.length; i++) {
    parrafos[i].style.color = "blue";
}
*/
const items = document.querySelectorAll("li");
for (let i = 0; i < items.length; i++) {
    items[i].textContent = items[i].textContent + " (item " + (i + 1) + ")";
}

/*-----------------------EJERCICIO 2--------------------------------*/ 
//referencias a elementos html
const input = document.getElementById("inputTarea");
const boton = document.getElementById("btnAgregar");
const lista = document.getElementById("listaTareas");

//boton para agregar
boton.addEventListener("click", function() {
    //texto guarda lo que escribe el usuario
    var texto = input.value;
    //si no esta vacio
    if (texto !== "") {

    //creo una lista
    var li = document.createElement("li");
    //el texto del usuario
    li.textContent = texto + " ";

    //se crea el boton para eliminar
    var btnEliminar = document.createElement("button");
    btnEliminar.textContent = "Eliminar";
    //le da la funcion al boton eliminar
    btnEliminar.onclick = function() {
        lista.removeChild(li);
    };
    //mete el boton adentro del item
    li.appendChild(btnEliminar);
    //agrega los itmens a la lista
    lista.appendChild(li);
    
    //"limpia los valores"
    input.value = "";
    }
});

/*-----------------------EJERCICIO 3--------------------------------*/
// Referencias a los botones
const botonResaltar = document.getElementById("botonResaltar");
const botonOcultar = document.getElementById("botonOcultar");

// Obtener todos los párrafos con clase 'parrafo'
const parrafos_3 = document.querySelectorAll(".parrafo");


// addEventListener es una función en JavaScript para hacer que los elementos HTML respondan a eventos, como cliks, teclas, etc.

// Botón para resaltar (agrega la clase .resaltado)
botonResaltar.addEventListener("click", () => {
    console.log("Botón Resaltar clickeado!"); // Para q pueda verlo en cosnola si funcionaba 
    parrafos_3.forEach(p => { // forEach ejecuta un callback para cada elemento del array
        p.classList.add("resaltado"); // agregamos la clase resaltado a todos los parrafos
    });
});

// Botón para ocultar (activar/desactivar la clase .oculto)
botonOcultar.addEventListener("click", () => {
    parrafos_3.forEach(p => { 
        p.classList.toggle("oculto"); // quitamos la clase oculto a todos los parrafos
    });
});

//------------Punto4----------------
if(texto !== ""){
    var li = document.createElement("li");
    li.textContent = texto + " ";

    li.addEventListener("click",function() {
        li.classList.toggle("completado");
    });

    var btnEliminar = document.createElement("button");
    btnEliminar.textContent= "Eliminar";
    btnEliminar.onclick =  function(){
        lista.removeChild(li)

    };

    li.appendChild(btnEliminar);
    lista.appendChild(li);
    input.value = "";
}
//---------FINAL-----