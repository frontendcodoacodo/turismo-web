
const navToggle = document.querySelector(".nav-toggle");
const navMenuLinks = document.querySelector(".nav-links");

navToggle.addEventListener("click", () => {
    navMenuLinks.classList.toggle("nav-links_visible");

    if (navMenuLinks.classList.contains("nav-links_visible")) {
        navToggle.setAttribute("aria-label", "Cerrar menu");
    } else {
        navToggle.setAttribute("aria-label", "Abrir menu");
    }
}) 