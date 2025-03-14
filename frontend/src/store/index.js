import {createStore} from 'vuex'
import store from '../store'

// Store is initialised here - in the real world you would make an API call.
export default createStore({
    state: {
        theme: "dark",
        isAuth: true,
    },
    getters: {
    },
    mutations: {
        setTheme: (theme) => {
            store.state.theme = theme
        },
        authSet: (bool) => {
            store.state.isAuth = bool
        }
    },
    actions: {

    },

    modules: {}
})