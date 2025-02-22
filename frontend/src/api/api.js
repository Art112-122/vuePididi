import axios from 'axios';
import cookie from 'js-cookie';


function axios_get(path) {
    axios.get(path)
}

function cookie_get(key) {
    return cookie.get(key);
}

function cookie_set(key, data) {
    cookie.set(key, data, { expires: 30 })
}


export default {
    axios_get
}

export const cookies = {
    cookie_get,
    cookie_set,
}