document.addEventListener("DOMContentLoaded", () => {
    const btnModoOscuro = document.getElementById("modoOscuro");
    const body = document.body;

    btnModoOscuro.addEventListener("click", () => {
        body.classList.toggle("oscuro");

        // Guardar la preferencia en localStorage
        if (body.classList.contains("oscuro")) {
            localStorage.setItem("modo", "oscuro");
        } else {
            localStorage.setItem("modo", "claro");
        }
    });

    // Aplicar el modo oscuro si estaba activado
    if (localStorage.getItem("modo") === "oscuro") {
        body.classList.add("oscuro");
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const loginButton = document.querySelector("#login button");

    if (loginButton) {
        loginButton.addEventListener("click", function () {
            window.location.href = "./dashboard/dashboard.html"; 
        });
    }
});
