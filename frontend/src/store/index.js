import {createStore} from 'vuex'
import store from '../store'

// Store is initialised here - in the real world you would make an API call.
export default createStore({
    state: {
        theme: false,
        isAuth: true,
    },
    getters: {
    },
    mutations: {
        setTheme () {
            store.state.theme =! store.state.theme
        },
        authSet (bool) {
            store.state.isAuth = bool
        }
    },
    actions: {

    },

    modules: {}
})