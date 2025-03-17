<script>
import "js-cookie"

import api from "@/api/api"

export default {
  name: 'App',
  data() {
    return {
      usernameValue: "",
      emailValue: "",
      classAlert: false,
      classAlert2: false,
      alertValue: "",
      alertValue2: "",
      passType: false,
      passValue: "",
      passValue2: "",
    }
  },
  methods: {
    postButton() {
      api.httpPost("http://127.0.0.1:7070/singup/", {username: this.usernameValue, email: this.emailValue, password: this.passValue})
    },
    passManager() {
      if (this.passValue === null) {
        this.alertValue = "Заповніть це поле"
      } else if (this.passValue.length <= 5) {
        this.alertValue = "Пароль закороткий!"
      } else if (this.passValue.length >= 12) {
        this.alertValue = "Пароль завеликий!"
      } else {
        this.alertValue = ''
      }
      this.classAlert = this.alertValue !== "";
    },
    passSecondManager() {
      if (this.passValue !== this.passValue2) {
        this.alertValue2 = "Паролі не співпадають"
        this.classAlert2 = true
        this.classAlert = true
      }

      else {
        this.alertValue2 = ''
        this.classAlert2 = false
        this.classAlert = this.alertValue !== "";
      }
    },
    passSubmit() {
      this.passSecondManager()
      this.passManager()
    }
  }
}
</script>

<template>
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>ПВББ Регистрация</title>
    <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bulma@1.0.2/css/bulma.min.css"
    >


  </head>
  <body class="purple-background">


  <div class="columns">


    <div class="column is-one-quarter box pr-5"
         style="border-bottom-left-radius: 0; border-top-left-radius: 0; height: 102vh;">
      <div class="py-6"></div>


      <h1 class="title has-text-centered">Реєстрація</h1>
      <label class="ml-3 label title is-5">Никнейм</label>
      <input v-model="username" class="ml-3 input" type="text" placeholder="ПІБ" name="username" required>
      <label class="ml-3 label title is-5 pt-4">Email</label>
      <input v-model="email" class="ml-3 input" type="email" placeholder="mypost@gmail.com" name="email" required>
      <label class="ml-3 label title is-5 pt-4">Пароль<h6 style="font-family: cursive; font-size: 0.9rem">Від 6 до 11 символів</h6></label>
      <input :class="classAlert ? 'is-danger' : ''" v-model="passValue" class="ml-3 input" placeholder="password123" required
             name="password" :type="passType ? 'text' : 'password'">
      <div :class="classAlert ? 'anim' : ''" v-if="alertValue" class="ml-5 icon-text my-1">
        <span class="icon">
          <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#bd5656"><path d="M480-280q17 0 28.5-11.5T520-320q0-17-11.5-28.5T480-360q-17 0-28.5 11.5T440-320q0 17 11.5 28.5T480-280Zm-40-160h80v-240h-80v240Zm40 360q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z"/></svg>
        </span>
        <span class="title is-5" style="color: #bd5656">{{ alertValue }}</span>

      </div>
      <label class="ml-3 label title is-5 pt-4">Повторення пароля</label>
      <input :class="classAlert2 ? 'is-danger' : ''" v-model="passValue2" class="ml-3 input" placeholder="password123"
             name="passwordcheck" :type="passType ? 'text' : 'password'" required>
      <div :class="classAlert2 ? 'anim' : ''" v-if="alertValue2" class="ml-5 icon-text my-1">
        <span class="icon">
          <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#bd5656"><path d="M480-280q17 0 28.5-11.5T520-320q0-17-11.5-28.5T480-360q-17 0-28.5 11.5T440-320q0 17 11.5 28.5T480-280Zm-40-160h80v-240h-80v240Zm40 360q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z"/></svg>
        </span>
        <span class="title is-5" style="color: #bd5656">{{ alertValue2 }}</span>

      </div>

      <label class="checkbox ml-3 pl-2">
        <input type="checkbox" v-on:click="passType =! passType">
        Показати
      </label>

      <div class="ml-5 pt-3 pb-1">
        <button v-on:click="passSubmit" class="button is-link" type="submit">Увійти</button>
      </div>





      <h4 style="text-align: center"><strong>Вже є акаунт? <a href="/login">Вхід</a></strong></h4>

    </div>

  </div>


  </body>
  </html>
</template>

<style>


.anim {
  animation: heartBeat 1s !important;
}




</style>