import {variables} from "./variables/variables.js";
import {clearFieldReg} from "./components/clearField.js";
import {sendAuthorizationRequest} from "./components/sendAuthorizationRequest.js";
import {hrefPage} from "./components/hrefPage.js";
import {isValidateFieldsValues} from "./components/isValidateFieldsValues.js";

console.log('Start!');

variables.btn.addEventListener('click',  async function (event) {
    event.preventDefault();

    const user = {
        userFirstName: variables.userFirstName.value,
        userLastName: variables.userLastName.value,
        userBirthday: variables.userBirthday.value,
        username: variables.userName.value,
        password: variables.userPassword.value,
        userRepeatPassword: variables.userRepeatPassword.value
    }

    if (isValidateFieldsValues(user)) {
        let response_json = await sendAuthorizationRequest('/reg',user);
        hrefPage(response_json);
        clearFieldReg();

    }
});




