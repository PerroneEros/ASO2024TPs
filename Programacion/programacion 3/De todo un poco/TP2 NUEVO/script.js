/*-----------------------EJERCICIO 1--------------------------------*/ 
const titulo = document.getElementById("tituloPrincial");
titulo.textContent = "titutlo cambiado";

const parrafos = document.getElementsByClassName("parrafo");
for(let i of parrafos){
    i.style.color = "blue";
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


