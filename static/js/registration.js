console.log('Start!');

const btn = document.querySelector('.form__btn input');
const userFirstName = document.querySelector('#firstname');
const userLastName = document.querySelector('#lastname');
const userEmail = document.querySelector('#useremail');
const userPassword = document.querySelector('#password');
const userRepeatPassword = document.querySelector('#repeatpassword');
const userBirthday = document.querySelector('#userBirthday');

btn.addEventListener('click',  async function (event) {
    event.preventDefault();
    const user = {
        userFirstName: userFirstName.value,
        userLastName: userLastName.value,
        userBirthday: userBirthday.value,
        userEmail: userEmail.value,
        userPassword: userPassword.value,
        userRepeatPassword: userRepeatPassword.value
    }
    if (validate(user)) {
        let response = await fetch("/login", {
            method: 'POST',
            headers: {
                "content-type": "application/json"
            },
            body: `
            {
                "userFirstName": "${userFirstName.value}",
                "userLastName": "${userLastName.value}",
                "userBirthday": "${userBirthday.value}",
                "username": "${userEmail.value}", 
                "password": "${userPassword.value}"
              }
            `,
        });
        let response_json = await response.json();
        console.log(response);
        console.log(response_json);
        if (response_json.success) {
            console.log("ПОЛУЧИЛОСЬ");
            document.location.href = response_json.page;
        }

        userEmail.value = '';
        userPassword.value = '';
        userFirstName.value = '';
        userLastName.value = '';
        userRepeatPassword.value = '';
        userBirthday.value = '';
    }
});

function validate(user){
    if (user.userFirstName.length === 0 || user.userLastName.length === 0 || user.userEmail.length === 0 || user.userPassword.length === 0
        || user.userRepeatPassword.length === 0 || user.userBirthday.length === 0){
        document.querySelector("#errorData").innerHTML= "*заполните все поля ввода";
        return false;
    }
    if (user.userPassword !== user.userRepeatPassword) {
        document.querySelector("#errorData").innerHTML= "*пароли не совпадают";
        return false
    }
    //Проверим содержит ли значение введенное в поле email символы @ и .
    /*let at = user.userEmail.indexOf("@");
    let dot = user.userEmail.indexOf(".");
    //Если поле не содержит эти символы знач email введен не верно
    if (at<1 || dot <1){
        document.querySelector("#errorData").innerHTML="*email введен не верно";
        return false;
    }*/
    document.querySelector("#errorData").innerHTML= "";
    return true;
}



