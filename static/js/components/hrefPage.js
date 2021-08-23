import {isValidUser} from "/static/js/components/isValidUser.js";

export function hrefPage(response_json) {
    console.log(response_json);
    if (isValidUser(response_json)) {
        console.log("ПОЛУЧИЛОСЬ");
        document.location.href = response_json.page;
    }
    return document.location.href;
}