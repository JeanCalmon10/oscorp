// carousel.js

document.addEventListener('DOMContentLoaded', function () {
    const track = document.querySelector('.carousel-track');
    const items = document.querySelectorAll('.carousel-item');
    const prevButton = document.querySelector('.carousel-prev');
    const nextButton = document.querySelector('.carousel-next');
  
    let currentIndex = 0;
  
    function updateCarousel() {
      const newTransformValue = -currentIndex * 100 + '%';
      track.style.transform = 'translateX(' + newTransformValue + ')';
    }
  
    function prevSlide() {
      currentIndex = (currentIndex - 1 + items.length) % items.length;
      updateCarousel();
    }
  
    function nextSlide() {
      currentIndex = (currentIndex + 1) % items.length;
      updateCarousel();
    }
  
    prevButton.addEventListener('click', prevSlide);
    nextButton.addEventListener('click', nextSlide);
  });
  