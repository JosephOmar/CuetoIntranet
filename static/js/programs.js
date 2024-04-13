// ! SLIDE AUTOMATIC IN PROGRAMS
// ! DECLARE VARIABLES TO USE
let slides = document.getElementsByClassName('about__slide-img');
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
}
// ! GO TO NEXT SLIDE
function nextSlide(){
    actualPoint++;
    if(actualPoint >= slides.length){
        actualPoint=0;
    }
    showSlide()
}
// ! START FUNCTION NEXTSLIDE 
let interval = setInterval(nextSlide,5000);

// ! CARROUSEL SYLLABUS PROGRAMS

let carrousel = document.querySelector('.syllabus-container');
let carrouselChildren = carrousel.children;
let buttonL = document.querySelector('.button1')
let buttonR = document.querySelector('.button2')
let actualPosition = 0
let indexPosition = 0

function moveLeft(){buttonL.addEventListener('click',()=>{
    indexPosition--;
    if(actualPosition==0){
        carrousel.prepend(carrousel.lastElementChild);
        actualPosition -= 100/6;
        carrousel.style.transform = `translateX(${actualPosition}%)`;
        carrousel.style.transition = `none`;
        setTimeout(()=>{
            actualPosition  += (100/6);
            carrousel.style.transform = `translateX(${actualPosition}%)`;
            carrousel.style.transition = `transform 0.5s linear`;
        },0);
    }else{
        actualPosition  += (100/6);
        if(actualPosition < 0.1 && actualPosition > 0){
            actualPosition = 0;
        }
        carrousel.style.transform = `translateX(${actualPosition}%)`;
        carrousel.style.transition = `transform 0.5s linear`;
    }
    if(indexPosition<0){
        indexPosition=0;
    }
    for(let i=0;i<carrouselChildren.length;i++){
        carrouselChildren[i].classList.remove('active');
    }
    carrouselChildren[indexPosition].classList.add('active');
})
}
function moveRight(){buttonR.addEventListener('click',()=>{
    indexPosition++;
    if(actualPosition== -50){
        carrousel.appendChild(carrousel.firstElementChild);
        actualPosition += 100/6;
        carrousel.style.transform = `translateX(${actualPosition}%)`;
        carrousel.style.transition = `none`;
        setTimeout(()=>{
        actualPosition  -= (100/6);
        carrousel.style.transform = `translateX(${actualPosition}%)`;
        carrousel.style.transition = `transform 0.5s linear`;
        },0);
    }else{
        actualPosition  -= (100/6);
        carrousel.style.transform = `translateX(${actualPosition}%)`;
        carrousel.style.transition = `transform 0.5s linear`;
    }
    if(indexPosition>3){
        indexPosition=3;
    }
    for(let i=0;i<carrouselChildren.length;i++){
        carrouselChildren[i].classList.remove('active');
    }
    carrouselChildren[indexPosition].classList.add('active');
})
}
function activeSelected(){
    for(let i=0;i<carrouselChildren.length;i++){
        carrouselChildren[i].addEventListener('click',()=>{
            buttonR.dispatchEvent(new Event('click'));
        });
    }
}
activeSelected();
moveLeft()
moveRight()

// ! *****INPUTS***** 

let inputsFather = document.querySelector('.form-container');
let inputsChildren = inputsFather.children;
let inputText = document.querySelectorAll('.form-input');

for(let i=0;i<inputsChildren.length;i++){
    inputsChildren[i].addEventListener('click',()=>{
        for(let j=0;j<inputsChildren.length;j++){
            let input = inputText[j]
            if(input && input.value.trim() == ''){
                inputsChildren[j].classList.remove('focus');
            }
        }
        inputsChildren[i].classList.add('focus');
    })
}