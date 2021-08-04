/*
const menuItems = document.querySelectorAll('.menu_item');
const menu = document.querySelector('.menu_items');

menu.addEventListener('click', (event) => {
    console.log(event)
    const target = event.target.closest('.menu_item');
    console.log(target);
    if (target && target.classList.contains('menu_item')) {
        menuItems.forEach((item, i) => {
            if (target === item) {
                console.log(item)
                removeActiveClass();
                addActiveClass(i);
            }
        });
    }
});

function addActiveClass(i = 0) {
    menuItems[i].classList.add('active');
}

function removeActiveClass() {
    menuItems.forEach((item) => {
        item.classList.remove('active');
    });
}
*/


