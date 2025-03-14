<script>

console.log("Ширина окна: " + window.innerWidth);



export default {
  name: 'App',

}
</script>

<template>
  <html lang="en">
  <header>
    <meta charset="UTF-8">
    <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bulma@1.0.2/css/bulma.min.css"
    >
  </header>
  <body>
  <div>
    <router-view/>
  </div>
  </body>
  </html>

</template>



<style>
@import './assets/style.css';


</style>
