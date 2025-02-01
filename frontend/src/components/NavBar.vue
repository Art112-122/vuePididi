<script>
export default {
  props: {
    name: {
      type: String,
      required: false,
    },
    username: {
      type: String,
      required: false,
    },
    methods: {
      reposition(ids, values) {
        let data = document.getElementById("var");
        let arrayIds = ids;
        let arrayValues = values;
        switch (data) {
          case '0':
            for (let i = 0; i < arrayIds.length; i++) {
              document.getElementById(arrayIds[i]).hidden = false;
              document.getElementById(arrayIds[i]).left = arrayValues[i];
            }
            data.innerText = '1';
            break;
          case '1':
            for (let i = 0; i < arrayIds.length; i++) {
              document.getElementById(arrayIds[i]).left = arrayValues[i];

              let hiddenn= document.getElementById(arrayIds[i]).hidden = true;

              setTimeout(hiddenn, 700);

            }
            data.innerText = '0';
            break;
        }
      }
    }
  }
};
</script>

<template>
  <div id="var" hidden>0</div>
  <svg class="rounded-figure" v-on:click="methods.reposition([], [])" xmlns="http://www.w3.org/2000/svg" height="34px" viewBox="0 -960 960 960" width="34px" fill="#8C1AF6"><path d="M120-240v-80h720v80H120Zm0-200v-80h720v80H120Zm0-200v-80h720v80H120Z"/></svg>
</template>

<style>

.rounded-figure {
  position: fixed;
  padding: 5px;
  top: 1rem;
  left: 2rem;
  border-radius: 50%;
  transition-duration: 0.7s;
}

.rounded-figure:hover {
  background-color: rgba(0, 0, 0, 0.09) !important;
}
</style>