export async function sendAuthorizationRequest(url,user) {
    let response = await fetch(url, {
        method: 'POST',
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify(user),
    });
    return await response.json();
}