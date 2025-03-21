
import axios from "axios";


function httpGetWithArgs(url, ...args) {
    axios.get(`${url}${args}`).then(response => {
        return response.data
    }).catch(() => {
        return "error"
    })

}

function httpGet(url) {
    axios.get(url).then(response => {
        return response
    }).catch(() => {
        return "error"
    })

}

function formPost(url, loader, data) {
    axios.post(url, data).then(response => {
        if (response.status <= 400) {
            return 'OK'
        } else {
            return response.data['error_message']
        }
    }).catch(() => {return 'error'}).finally(function loading() {loader = false})
}



export {httpGet, formPost, httpGetWithArgs};
