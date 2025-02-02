import {createRouter, createWebHashHistory} from 'vue-router'
import Main  from './views/Main.vue'
import Index from './views/Index.vue'

export default createRouter({
    history: createWebHashHistory(),
    mode: "history",
    routes: [
        {path: '/', component: Index},
        {path: '/user', component: Main},
    ]
})