// Carousel
const carouselInner = document.querySelector('.carousel-inner');

carouselInner.addEventListener('mouseenter', () => {
    carouselInner.style.animationPlayState = 'paused'; // Pausa la animación
});

carouselInner.addEventListener('mouseleave', () => {
    carouselInner.style.animationPlayState = 'running'; // Reanuda la animación
});