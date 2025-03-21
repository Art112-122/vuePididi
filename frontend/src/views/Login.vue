<script>
export default {
  name: 'LoginName',
  data() {
    return {
      passType: false,
      alertValue: ""
    }
  },
}
</script>

<template>
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>ПВББ Вход</title>

  </head>
  <body class="purple-background">


  <div class="columns">
    </div>

    <div class="column is-one-quarter box pr-5" style="border-bottom-left-radius: 0; border-top-left-radius: 0; height: 100.39vh;">
      <div class="py-6"></div>


        <h1 class="title has-text-centered">Вхід</h1>
        <label class="label title is-5 pt-4">Email</label>
        <input class="input" type="email" placeholder="mypost@gmail.com" name="email">
        <label class="label title is-5 pt-4">Пароль</label>
        <input class="input" placeholder="password123" name="password" :type="passType ? 'text' : 'password'">
        <label class="checkbox pl-2">
          <input type="checkbox" v-on:click="passType = !passType">
          Показати
        </label>
      <div v-if="alertValue" class="ml-5 icon-text my-1">
        <span class="icon">
          <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#EA3323"><path d="M480-280q17 0 28.5-11.5T520-320q0-17-11.5-28.5T480-360q-17 0-28.5 11.5T440-320q0 17 11.5 28.5T480-280Zm-40-160h80v-240h-80v240Zm40 360q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z"/></svg>
        </span>
        <span class="title">{{ alertValue }}</span>

      </div>
        <div class="pt-3 pb-1">
          <input class="button is-link" type="submit" value="Войти">
        </div>




      <h4 style="text-align: center"><strong>Нема аккаунта? <a href="/register">Регістрація</a></strong><br/><strong>Чи <a href="">забули пароль? </a></strong></h4>





    </div>






  </body>
  </html>
</template>

<style scoped>

</style>