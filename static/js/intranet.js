let menuMain = document.querySelectorAll('.menu-main-sub');
let subMenu = document.querySelectorAll('.submenu');

for(let i=0;i<menuMain.length;i++){
    menuMain[i].addEventListener('click',()=>{
        for(let j=0;j<subMenu.length;j++){
            if (j === i) {
                subMenu[j].classList.toggle('active');
            } else {
                subMenu[j].classList.remove('active');
            }
        }
    })
}