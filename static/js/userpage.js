import {loadUserData} from "/static/js/components/loadUserData.js";


const btnCreatePost = document .querySelector('.btn_create_post');
const postArea = document.querySelector('.user_post');
const inputPostText = document.querySelector('.input_post');
const userName = document.querySelectorAll('.js-user_name');
const userBirthday = document.querySelector('.js-user_birthday');

btnCreatePost.addEventListener('click', (event) => {
    event.preventDefault();
    let textPost =  inputPostText.value;
    console.log(textPost.length)
    if (textPost.length !== 0) {
        postArea.style.display = 'block';
        let post =  `
        <div class="post">${textPost}</div>
    `;
        postArea.insertAdjacentHTML("afterbegin", post);
        inputPostText.value = '';
    }
});

loadUserData().then(user => {
    console.log(user);
    userName.forEach(username => {
        username.innerHTML = `${user.firstName} ${user.lastName}`
    });
    userBirthday.innerHTML = user.birthday;
});


