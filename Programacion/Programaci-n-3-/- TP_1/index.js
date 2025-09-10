const toggle = document.getElementById('toggleDark');
const body = document.body;

toggle.addEventListener('click', function () {
    body.classList.toggle('dark-mode');

    if (body.classList.contains('dark-mode')) {
        localStorage.setItem('theme', 'dark');
        toggle.classList.replace('bi-brightness-high-fill', 'bi-moon-fill'); // Cambia a luna
        body.style.background = 'black';
        body.style.color = 'white';
    } else {
        localStorage.setItem('theme', 'light');
        toggle.classList.replace('bi-moon-fill', 'bi-brightness-high-fill'); // Cambia a sol
        body.style.background = 'white';
        body.style.color = 'black';
    }

    body.style.transition = '2s'; // Mantiene la animación
});

// Mantener el modo oscuro y el ícono al recargar la página
if (localStorage.getItem('theme') === 'dark') {
    body.classList.add('dark-mode');
    toggle.classList.replace('bi-brightness-high-fill', 'bi-moon-fill');
    body.style.background = 'black';
    body.style.color = 'white';
}

$(document).ready(function(){
    $('.ir-arriba').click(function(){
      $('html, body').animate({ scrollTop: 0 }, 1000);
    });

    $(window).scroll(function(){
      if ($(this).scrollTop() > 0) {
        $('.ir-arriba').fadeIn(600);
      } else {
        $('.ir-arriba').fadeOut(600);
      }
    });
});
