export function isValidateFieldsValues(user){
    for(let prop in user) {
        if (user[prop].length === 0) {
            document.querySelector("#errorData").innerHTML="*заполните все поля ввода";
            return false;
        }
    }
    if (user.userRepeatPassword !== undefined && (user.password !== user.userRepeatPassword)) {
        document.querySelector("#errorData").innerHTML= "*пароли не совпадают";
        return false
    }
    //Проверим содержит ли значение введенное в поле email символы @ и .
    let at = user.username.indexOf("@");
    let dot = user.username.indexOf(".");
    //Если поле не содержит эти символы знач email введен не верно
    if (at < 1 || dot < 1 ) {
        document.querySelector("#errorData").innerHTML="*email введен не верно";
        return false;
    }
    document.querySelector("#errorData").innerHTML= "";
    return true;
}