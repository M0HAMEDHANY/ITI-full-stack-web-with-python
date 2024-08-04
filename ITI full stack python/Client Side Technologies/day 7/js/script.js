const images = ["../images/gojo-x-sukuna.jpg",
    "../images/solo-leveling.jpg",
    "../images/muzan.jpg",
    "../images/gyomei-himejima.jpg"]

let currentImageIndex = 0;
let slideshowInterval;

const slideshow = document.getElementById("slideshow");
const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const nextBtn = document.getElementById("nextBtn");
const backBtn = document.getElementById("backBtn");

function updateslideshow() { slideshow.src = images[currentImageIndex] }

backBtn.addEventListener('click', () => {
    currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
    updateslideshow();
});

nextBtn.addEventListener('click', () => {
    currentImageIndex = (currentImageIndex + 1) % images.length;
    updateslideshow();
});

startBtn.addEventListener('click', () => {
        slideshowInterval = setInterval(() => {
            currentImageIndex = (currentImageIndex + 1) % images.length;
            updateslideshow();
        }, 1000);
    
});

stopBtn.addEventListener("click", () => {
    clearInterval(slideshowInterval);
    slideshowInterval = null;
})
