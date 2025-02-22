<script>
export default {
  name: 'LoginName',
  data() {
    return {
      passType: false,
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
    <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bulma@1.0.2/css/bulma.min.css"
    >
    <link rel="stylesheet" href="../static/style.css">
  </head>
  <body class="purple-background">


  <div class="columns">
    <div class="column is-4">
    </div>

    <div class="column is-one-quarter">
      <div class="py-6"></div>
      <div class="card p-3">

        <h1 class="title has-text-centered">Вхід</h1>
        <label class="label title is-5 pt-4">Email</label>
        <input class="input" type="email" placeholder="mypost@gmail.com" name="email">
        <label class="label title is-5 pt-4">Пароль</label>
        <input class="input" placeholder="password123" name="password" :type="passType ? 'text' : 'password'">
        <label class="checkbox pl-2">
          <input type="checkbox" v-on:click="passType = !passType">
          Показати
        </label>

        <div class="pt-3 pb-1">
          <input class="button is-link" type="submit" value="Войти">
        </div>


      </div>

      <h4 style="text-align: center"><strong>Нема аккаунта? <a href="">Регістрація</a></strong><br/><strong>Чи <a href="">забули пароль? </a></strong></h4>

    </div>
  </div>


  <div class="py-6"></div>
  <div class="py-6"></div>
  <div class="py-6"></div>
  <div class="py-6"></div>
  <div class="py-3"></div>


  </body>
  </html>
</template>

<style scoped>

</style>