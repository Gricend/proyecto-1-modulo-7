const body = document.querySelector("body"),
    sidebar = body.querySelector(".sidebar"),
    toggle = body.querySelector(".toggle"),
    searchBtn = body.querySelector(".search-box"),
    modeSwitch = body.querySelector(".toggle-switch"),
    modeText = body.querySelector(".mode-text");


function applyTheme() {
    const isDarkMode = localStorage.getItem('darkMode') === 'true';

    body.classList.toggle("dark", isDarkMode);

    if (isDarkMode) {
        modeText.innerText = "Modo Claro";
    } else {
        modeText.innerText = "Modo Oscuro";
    }
}

toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
});

searchBtn.addEventListener("click", () => {
    sidebar.classList.remove("close");
});

modeSwitch.addEventListener("click", () => {
    body.classList.toggle("dark");

    const isDarkMode = body.classList.contains("dark");
    localStorage.setItem('darkMode', isDarkMode.toString());

    if (isDarkMode) {
        modeText.innerText = "Modo Claro";
    } else {
        modeText.innerText = "Modo Oscuro";
    }
});


applyTheme();

const popover = new bootstrap.Popover('.popover-dismiss', {
    trigger: 'focus'
})
