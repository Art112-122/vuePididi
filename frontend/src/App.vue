<script>

console.log("Ширина окна: " + window.innerWidth);



export default {
  name: 'App',

}
</script>

<template>
    <meta charset="UTF-8">
    <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bulma@1.0.2/css/bulma.min.css"
    >
  <div>
    <router-view/>
  </div>

</template>



<style>
@import './assets/style.css';


</style>
