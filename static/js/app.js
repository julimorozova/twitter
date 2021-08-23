import {sendAuthorizationRequest} from "/static/js/components/sendAuthorizationRequest.js";
import {isValidateFieldsValues} from "/static/js/components/isValidateFieldsValues.js";
import {hrefPage} from "/static/js/components/hrefPage.js";
import {variables} from "./variables/variables.js";
import {clearFieldAuto} from "./components/clearField.js";

console.log('Start!');

variables.btn.addEventListener('click',  async function (event) {

    event.preventDefault();
    const user = {
        username: variables.userName.value,
        password: variables.userPassword.value
    }

    if(isValidateFieldsValues(user)) {
       let response_json = await sendAuthorizationRequest('/login',user);
        hrefPage(response_json);

        clearFieldAuto();
    }
});

