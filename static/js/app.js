console.log('Start!');

const btn = document.querySelector('.form__btn input');
const userName = document.querySelector('.form__auto #username');
const userPassword = document.querySelector('.form__auto #password');
btn.addEventListener('click', (event) => {
    console.log('event');
    event.preventDefault();

    console.log(sendRequestAuthorization(userName.value, userPassword.value))
    userName.value = '';
    userPassword.value = '';

});

async function sendRequestAuthorization(userName, userPassword) {
    const url = 'http://127.0.0.1:8000/login';

    const user = {
        name: userName,
        password: userPassword
    }
    let response = await fetch(url, {
        method: 'POST',

        body: JSON.stringify(user)
    });
    let result = await response.json();
    return result;
}