const burger = document.getElementById('burger');
const mainMobMenu = document.getElementById('mobile-menu');
const header = document.getElementById('header');
const mainLogo = document.getElementById('main-logo');
const body = document.getElementById('body');

header.addEventListener('click', function (event) {

    if (burger.contains(event.target)) {
        mainMobMenu.classList.toggle('visually-hidden_menu');
        burger.classList.toggle('active');
        header.classList.toggle('overlay_menu');
        mainLogo.classList.toggle('visually-hidden_logo');
        body.classList.toggle('overflow-hidden');
    } else if (header.classList.contains('overlay_menu')){
        if(!mainMobMenu.contains(event.target)) {
            mainMobMenu.classList.toggle('visually-hidden_menu');
            burger.classList.toggle('active');
            header.classList.toggle('overlay_menu');
            mainLogo.classList.toggle('visually-hidden_logo');
            body.classList.toggle('overflow-hidden');
        }
    }





})

