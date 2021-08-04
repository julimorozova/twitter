console.log('Start!');

const btn = document.querySelector('.form__btn input');
const title = document.querySelector('.title');
const errorData = document.querySelector('.error_data');
const userName = document.querySelector('.form__auto #username');
const userPassword = document.querySelector('.form__auto #password');

btn.addEventListener('click',  async function (event) {
    event.preventDefault();

    const userName = document.querySelector('.form__auto #username');
    const userPassword = document.querySelector('.form__auto #password');

    let response = await fetch("/login", {
        method: 'POST',
        headers: {
            "content-type": "application/json"
        },
        body: `{"username": "${userName.value}", "password": "${userPassword.value}"}`,
    });
    let response_json = await response.json();
    console.log(response);
    console.log(response_json);
    isValidUser(response_json.success);
    if (response_json.success) {
        console.log("ПОЛУЧИЛОСЬ");
        document.location.href = response_json.page;

    }
    userName.value = '';
    userPassword.value = '';

});

function isValidUser(success) {
    let errorUser = `
        <p style="color: red;">Неверный логин или пароль</p>
    `
    if (!success) {
        errorData.innerHTML = errorUser;
    }
}

