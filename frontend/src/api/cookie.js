import cookie from "js-cookie";

function createJWT(token) {
    cookie.set("token", token, {expires: 90});
}

function getCookie(key) {
    cookie.get(key);
}

export {createJWT, getCookie};