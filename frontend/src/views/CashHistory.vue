<script>
export default {
  name: 'CashHistory',
  data () {
    return {
      object1: [{cost: 1,}, {cost: 2}],
    }
  },
  created() {

  }
}
</script>

<template>
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Settings</title>
  </head>
  <body>
  <div v-for="i in object1" :key="i">
    {{i["cost"]}}
  </div>



  </body>
  </html>
</template>

<style scoped>

</style>