// Smooth scrolling when clicking on the "Shop Now" button
document.querySelector('.cta-button').addEventListener('click', function(event) {
    event.preventDefault();
    document.querySelector('#shop-now').scrollIntoView({
        behavior: 'smooth'
    });
});