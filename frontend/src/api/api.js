import Axios from 'axios';
import cookie from 'js-cookie';
import axios from "axios";




function httpGet(url) {
    axios.get(url).then(response => {return response}).catch(error => {return "!*#$!"})
}


function createJWT(token) {
    cookie.set("token", token);
}

