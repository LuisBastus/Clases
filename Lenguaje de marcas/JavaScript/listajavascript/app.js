document.addEventListener("DOMContentLoaded", () => {
    const listaTareas = document.getElementById("listaTareas");
    const inputTarea = document.getElementById("nuevaTarea");
    const btnAgregar = document.getElementById("agregarBtn");
    const btnExportar = document.getElementById("exportarXML");
    const inputImportar = document.getElementById("importarXML");

    // Carga inicial de tareas desde LocalStorage
    cargarTareas();

    // Agregar una nueva tarea
    btnAgregar.addEventListener("click", () => {
        const texto = inputTarea.value.trim();
        if (texto !== "") {
            agregarTarea(texto, false);
            inputTarea.value = "";
            guardarTareas();
        }
    });

    // Marcar/Desmarcar tarea como completada o eliminar
    listaTareas.addEventListener("click", (e) => {
        if (e.target.tagName === "LI") {
            e.target.classList.toggle("completada");
            guardarTareas();
        } else if (e.target.tagName === "BUTTON") {
            e.target.parentElement.remove();
            guardarTareas();
        }
    });

    // Exportar tareas a XML
    btnExportar.addEventListener("click", () => {
        exportarXML();
    });

    // Importar tareas desde un archivo XML
    inputImportar.addEventListener("change", (e) => {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (event) => {
                importarXML(event.target.result);
            };
            reader.readAsText(file);
        }
    });

    // Función para agregar una tarea a la lista
    function agregarTarea(texto, completada) {
        const li = document.createElement("li");
        li.textContent = texto;
        if (completada) li.classList.add("completada");

        const btnEliminar = document.createElement("button");
        btnEliminar.textContent = "❌";
        li.appendChild(btnEliminar);

        listaTareas.appendChild(li);
    }

    // Función para guardar tareas en LocalStorage
    function guardarTareas() {
        const tareas = [];
        document.querySelectorAll("#listaTareas li").forEach((li) => {
            tareas.push({
                texto: li.childNodes[0].nodeValue,
                completada: li.classList.contains("completada")
            });
        });
        localStorage.setItem("tareas", JSON.stringify(tareas));
    }

    // Función para cargar tareas de LocalStorage
    function cargarTareas() {
        const tareasGuardadas = localStorage.getItem("tareas");
        if (tareasGuardadas) {
            JSON.parse(tareasGuardadas).forEach((tarea) => {
                agregarTarea(tarea.texto, tarea.completada);
            });
        }
    }

    // Función para exportar a XML
    function exportarXML() {
        let xmlString = "<?xml version='1.0' encoding='UTF-8'?><tasks>";
        document.querySelectorAll("#listaTareas li").forEach((li) => {
            xmlString += `<task completed="${li.classList.contains("completada")}">${li.childNodes[0].nodeValue}</task>`;
        });
        xmlString += "</tasks>";

        const blob = new Blob([xmlString], { type: "text/xml" });
        const a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = "tareas.xml";
        a.click();
    }

    // Función para importar desde XML
    function importarXML(xmlText) {
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(xmlText, "text/xml");
        const tareas = xmlDoc.getElementsByTagName("task");

        listaTareas.innerHTML = ""; // Borra la lista actual

        for (let i = 0; i < tareas.length; i++) {
            let texto = tareas[i].textContent;
            let completada = tareas[i].getAttribute("completed") === "true";
            agregarTarea(texto, completada);
        }

        guardarTareas();
    }
});
