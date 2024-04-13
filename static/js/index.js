// ! DECLARE VARIABLES TO USE
let slides = document.getElementsByClassName('slides-img');
let pointsSlide = document.getElementsByClassName('point-slider');
let arrowsSlide = document.getElementsByClassName('arrow-slider');
let actualPoint = 0;
// ! SCROLL ALL SLIDES - WHEN CLICKED ADD ACTIVE CLASS AND REMOVE CLASS OF OTHERS SLIDES
function showSlide(){
    for(let i=0;i<slides.length;i++){
        // ! REMOVE ACTIVE CLASS
        slides[i].classList.remove('active');
    }
    // ! ADD ACTIVE CLASS
    slides[actualPoint].classList.add('active');

    for(let i=0;i<pointsSlide.length;i++){
        // ! REMOVE ACTIVE CLASS
        pointsSlide[i].classList.remove('active');
    }
    // ! ADD ACTIVE CLASS
    pointsSlide[actualPoint].classList.add('active');
}
// ! GO TO NEXT SLIDE
function nextSlide(){
    actualPoint++;
    if(actualPoint >= slides.length){
        actualPoint=0;
    }
    showSlide()
}
// ! GO TO PREVIOUS SLIDE
function previousSlide(){
    actualPoint--;
    if(actualPoint<0){
        actualPoint=slides.length-1;
    }
    showSlide()
}
// ! GO TO SELECTED SLIDE 
function goToSlide(point){
    actualPoint = point;
    showSlide()
}
// ! START FUNCTION NEXTSLIDE 
let interval = setInterval(nextSlide,8000);
// ! CHANGE SLIDE TO POINT SELECTED
for(let i=0;i<pointsSlide.length;i++){
    pointsSlide[i].addEventListener('click',function(){
        let point = parseInt(this.getAttribute('point-img'));
        goToSlide(point);
    });
}
// ! CHANGE SLIDE RIGHT OR LEFT
for (let i=0;i<arrowsSlide.length;i++){
    arrowsSlide[i].addEventListener('click',function(){
        let arrow = parseInt(this.getAttribute('arrow-img'));
        if(arrow==1){
            previousSlide();
        }else{
            nextSlide();
        }
    });
} 