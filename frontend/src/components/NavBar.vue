<script>
export default {
  data() {
    return {
      position: false,
      tooltipMenu: false,
      tooltipAnalytics: false,
    }
  }

};
</script>

<template>

  <div class="navbarComp">
    <svg class="rounded-figure" style="z-index: 2" v-on:click="position=!position"
         xmlns="http://www.w3.org/2000/svg" height="34px" viewBox="0 -960 960 960" width="34px" fill="#8C1AF6">
      <path d="M120-240v-80h720v80H120Zm0-200v-80h720v80H120Zm0-200v-80h720v80H120Z"/>
    </svg>
    <svg style="opacity: 1; z-index: 1" v-on:mousemove="tooltipMenu = true" v-on:mouseout="tooltipMenu = false"
         :style="position ? 'top: 4rem; opacity:1': 'top: 1rem; opacity:0'"
         class="rounded-figure" xmlns="http://www.w3.org/2000/svg"
         height="34px" viewBox="0 -960 960 960" width="34px" fill="#8C1AF6">
      <path
          d="M246.78-206.78H347V-453h266v246.22h100.22v-349.83L480-731.52 246.78-556.61v349.83Zm-106 106v-508.83L480-864.31 819.22-609.8v509.02H515.48v-254.7h-70.96v254.7H140.78ZM480-468.87Z"/>
    </svg>
    <div class="tooltip py-2" style="left: 5rem; top: 4rem" :style="tooltipMenu ? 'opacity:1' : 'opacity:0'">Головна\Картка</div>
    <svg style="opacity: 1; z-index: 1" v-on:mousemove="tooltipAnalytics = true" v-on:mouseout="tooltipAnalytics = false"
         :style="position ? 'top: 7rem; opacity:1': 'top: 1rem; opacity:0'"
         class="rounded-figure" xmlns="http://www.w3.org/2000/svg" height="34px" viewBox="0 -960 960 960" width="34px"
         fill="#8C1AF6">
      <path
          d="M120-120v-77.33L186.67-264v144H120Zm163.33 0v-237.33L350-424v304h-66.67Zm163.34 0v-304l66.66 67.67V-120h-66.66ZM610-120v-236.33L676.67-423v303H610Zm163.33 0v-397.33L840-584v464h-66.67ZM120-346.33v-94.34l280-278.66 160 160L840-840v94.33L560-465 400-625 120-346.33Z"/>
    </svg>
    <div class="tooltip py-2" style="left: 5rem; top: 7rem" :style="tooltipAnalytics ? 'opacity:1' : 'opacity:0'">Історія платежів</div>
  </div>

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

.tooltip {
  background-color: rgba(0, 0, 0, 0.4) !important;
  position: fixed;
  padding: 5px;
  border-radius: 20%;
  user-select: none;
  text-align: center;
  font-family: sans-serif;
  color: white;
  transition-duration: 0.5s;
}
</style>