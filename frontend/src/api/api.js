import cookie from 'js-cookie';
import axios from "axios";


function httpGet(url, ...args) {
    axios.get(`${url}${args}`).then(response => {
        return response
    }).catch(error => {
        return JSON.stringify(error)
    })
}

function httpPost(url, data) {
    axios.post(url, data).then(response => {
        if (response <= 400) {
            return 'OK'
        } else {
            return response
        }
    }).catch(error => {
        return JSON.stringify(error)
    })
}

function createJWT(token) {
    cookie.set("token", token, {expires: 90});
}

function getCookie(key) {
    cookie.get(key);
}

export default {httpGet, httpPost, createJWT, getCookie};
