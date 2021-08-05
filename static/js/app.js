console.log('Start!');

const btn = document.querySelector('.form__btn input');
const title = document.querySelector('.title');
const errorData = document.querySelector('.error_data');
const userName = document.querySelector('.form__auto #username');
const userPassword = document.querySelector('.form__auto #password');

btn.addEventListener('click',  async function (event) {
    event.preventDefault();

    if(validateDate(userName.value, userPassword.value)) {

       let response_json = await sendAuthorizationRequest();
        hrefPage(response_json);

        userName.value = '';
        userPassword.value = '';
    }
});

async function sendAuthorizationRequest() {
    let response = await fetch("/login", {
        method: 'POST',
        headers: {
            "content-type": "application/json"
        },
        body: `{"username": "${userName.value}", "password": "${userPassword.value}"}`,
    });
    return await response.json();
}

function isValidUser(success) {
    if (!success) {
        document.querySelector('#errorData').innerHTML = '*неверный логин или пароль';
        return false
    }
    return true;
}

function validateDate(name, password){
    if (name.length === 0 || password.length === 0){
        document.querySelector("#errorData").innerHTML="*заполните все поля ввода";
        return false;
    }
    //Проверим содержит ли значение введенное в поле email символы @ и .
    /*let at = name.indexOf("@");
    let dot = name.indexOf(".");
    //Если поле не содержит эти символы знач email введен не верно
    if (at < 1 || dot < 1 ) {
        document.querySelector("#errorData").innerHTML="*email введен не верно";
        return false;
    }*/
    return true;

}

function hrefPage(response_json) {
    console.log(response_json);
    if (isValidUser(response_json.success)) {
        console.log("ПОЛУЧИЛОСЬ");
        document.location.href = response_json.page;
    }
    return document.location.href;
}

