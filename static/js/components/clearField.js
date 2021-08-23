import {variables} from "../variables/variables.js";

export function clearFieldAuto() {
    variables.userName.value = '';
    variables.userPassword.value = '';
}

export function clearFieldReg() {
    variables.userName.value = '';
    variables.userPassword.value = '';
    variables.userFirstName.value = '';
    variables.userLastName.value = '';
    variables.userRepeatPassword.value = '';
    variables.userBirthday.value = '';
}