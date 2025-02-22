<script>
import state from "./store/index";
console.log("Ширина окна: " + window.innerWidth);
console.log(state.state.isAuth);


export default {
  name: 'App',
}
</script>

<template>
  <div>
  <router-view/>
  </div>
</template>



<style src="../style.css">

</style>
