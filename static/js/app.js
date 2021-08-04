console.log('Start!');

const btn = document.querySelector('.form__btn input');
/*const userName = document.querySelector('.form__auto #username');
const userPassword = document.querySelector('.form__auto #password');*/

btn.addEventListener('click', async function (event)  {
    event.preventDefault();
    const userName = document.querySelector('.form__auto #username');
    const userPassword = document.querySelector('.form__auto #password');
    console.log(userName.value, userPassword.value);
    let response = await fetch("/login", {
        method: 'POST',
        headers: {
            "content-type": "application/json"
        },
        body: `{"username": "${userName.value}", "password": "${userPassword.value}"}`,
    });
    let response_json = await response.json();
    if (response_json.success) {
        console.log("ПОЛУЧИЛОСЬ")
    }
    /*userName.value = '';
    userPassword.value = '';*/

});

async function sendRequestAuthorization(userName, userPassword) {
    const url = '/login';
    const user = {
        name: userName,
        password: userPassword
    }
    try {
        let response = await fetch(url, {
            method: 'POST',
            body: JSON.stringify(user)
        });
        console.log(response);
        let json = response.status;
        console.log('Успех:', json);
    } catch (error) {
        console.error('Ошибка:', error);
    }

}