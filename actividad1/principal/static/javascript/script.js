const body = document.querySelector("body"),
    sidebar = body.querySelector(".sidebar"),
    toggle = body.querySelector(".toggle"),
    searchBtn = body.querySelector(".search-box"),
    modeSwitch = body.querySelector(".toggle-switch"),
    modeText = body.querySelector(".mode-text");


function aplicarTema() {
    const ismodoOscuro = localStorage.getItem('modoOscuro') === 'true';

    body.classList.toggle("oscuro", ismodoOscuro);

    if (ismodoOscuro) {
        modeText.innerText = "Modo Claro";
    } else {
        modeText.innerText = "Modo Oscuro";
    }
}

toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
});

modeSwitch.addEventListener("click", () => {
    body.classList.toggle("oscuro");

    const ismodoOscuro = body.classList.contains("oscuro");
    localStorage.setItem('modoOscuro', ismodoOscuro.toString());

    if (ismodoOscuro) {
        modeText.innerText = "Modo Claro";
    } else {
        modeText.innerText = "Modo Oscuro";
    }
});

aplicarTema();