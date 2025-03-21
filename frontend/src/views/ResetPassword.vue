<script setup>

</script>

<template>
  <html lang="uk" class="purple-background">


  <div class="column is-one-third box" style="height: 102vh; border-bottom-left-radius: 0; border-top-left-radius: 0;">
    <div class="py-2"></div>
    <h1 class="title has-text-centered">Забули пароль?</h1>
    <h3 class="title is-3 has-text-centered">Ми надішлемо лист для перевірки</h3>
    <div class="py-3"></div>
    <label class="label title is-3 pt-4">Email</label>
    <input class="input" type="email" placeholder="mypost@gmail.com" name="email" style="font-size: 1.3rem !important; width: 90% !important;">
    <div class="pt-3 pb-1">
      <input class="button is-link " type="submit" value="Надіслати" id="submitButton">
    </div>
  </div>
  </html>
</template>

<style scoped>
@import '../assets/style.css';
</style>