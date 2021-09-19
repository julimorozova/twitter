export async function loadUserData() {
    let response = await fetch('/user', {
        method: 'GET',
        headers: {
            "content-type": "application/json"
        },
    });
    let responseJson = await response.json();

    return {
        firstName: 'Иван',
        lastName: 'Иванов',
        birthday: '1.07.1995'
    };

    /*return {
        firstName: responseJson.userFirstName,
        lastName: responseJson.userLastName,
        birthday: responseJson.userBirthday
    };*/
}