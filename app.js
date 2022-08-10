// Lógica de los botones al ser clicados

const btn_cargar = document.getElementById("cargar");
const btn_limpiar = document.getElementById("reset");
const btn_desvelar = document.getElementById("desvelar");

btn_cargar.style.display = "none";

btn_cargar.addEventListener('click', event => {
    cargar();
});

btn_limpiar.addEventListener('click', event => {
    limpiar();
});

btn_desvelar.addEventListener('click', event => {
    desvelar();
});

// Pasamos a la carga de Pyodide para poder escribir las funciones de los botones en Python

let initPyodide = loadPyodide();  // Lo dejamos fuera para poder acceder al mismo entorno Python desde todas las funciones

async function inicializar(){
    let pyodide = await initPyodide;     // Hay que esperar a que se haya cargado.
    let response = await fetch("init.py");
    let init = await response.text();
    pyodide.runPython(init);
    btn_cargar.style.display = "block";  // Se muestra el botón tras haberse inicializado todo
}

inicializar(); // Sólo queremos que ejecute Pyodide una vez, pues tarda su tiempo

async function cargar() {
    let pyodide = await initPyodide;
    let response = await fetch("cargar.py");
    let funcs = await response.text();
    pyodide.runPython(funcs);
}

async function limpiar() {
    let pyodide = await initPyodide;
    let response = await fetch("limpiar.py");
    let funcs = await response.text();
    pyodide.runPython(funcs);
}

async function desvelar() {
    let pyodide = await initPyodide;
    let response = await fetch("desvelar.py");
    let funcs = await response.text();
    pyodide.runPython(funcs);
}

