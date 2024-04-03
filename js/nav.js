
/*
const navToggle = document.querySelector(".nav-toggle");
const navMenuLinks = document.querySelector(".nav-links");

navToggle.addEventListener("click", () => {
    navMenuLinks.classList.toggle("nav-links_visible");

    if (navMenuLinks.classList.contains("nav-links_visible")) {
        navToggle.setAttribute("aria-label", "Cerrar menu");
    } else {
        navToggle.setAttribute("aria-label", "Abrir menu");
    }
}) */

/*
var hamburger = document.getElementById('Hamburger');
var menu = document.getElementById('Menu');

hamburger.addEventListener('click', function(){
    menu.classList.toggle('open');
}) */

const toggleBtn = document.querySelector('.toggle_btn');
const toggleBtnIcon = document.querySelector('.toggle_btn i');
const dropDownMenu = document.querySelector('.dropdown_menu');

toggleBtn.onclick = function() {
    dropDownMenu.classList.toggle('open');
    const isOpen = dropDownMenu.classList.contains('open');

    toggleBtnIcon.classList = isOpen
    ? 'fa-solid fa-xmark'
    : 'fa-solid fa-bars'
}