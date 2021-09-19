export function isValidUser(response_json) {
    if (!response_json.success && response_json.message === "I don't know you") {
        document.querySelector('#errorData').innerHTML = '*неверный логин или пароль';
        return false
    }
    if (!response_json.success && response_json.message === "This username is busy") {
        document.querySelector('#errorData').innerHTML = '*логин занят';
        return false
    }
    return true;
}
