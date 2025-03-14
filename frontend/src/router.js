import {createRouter, createWebHistory } from 'vue-router'
import Main  from './views/Main.vue'
import Index from './views/Index.vue'
import Reg from './views/Regest.vue'
import Login from './views/Login.vue'
import Settings from "./views/Settings.vue";
import Transactions from './views/Transaction.vue'
import History from './views/CashHistory.vue'
import Reset from './views/ResetPassword.vue'
import store from './store'


const routes= [
        {path: '/', component: Index, name: "mainIndex"},
        {path: '/user', component: Main, name:"user"},
        {path: '/register', component: Reg, name:"register"},
        {path: '/login', component: Login, name:"login"},
        {path: '/settings', component: Settings, name:"settings"},
        {path: '/transaction', component: Transactions, name:"transaction"},
        {path: '/history', component: History, name:"history"},
        {path: '/resetPassword', component: Reset, name:"resetPassword"},
    ]




const router = createRouter({
    history: createWebHistory(),
    routes})


router.beforeEach((to, ) => {

    if (store.state.isAuth === false && to.path !== '/login' && to.path !== '/register' && to.path !== '/') {
        return {
            name: 'login'
        }
    }
})

export default router