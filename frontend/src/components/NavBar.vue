<script>
export default {
  data() {
    return {
      position: false,
      tooltipMenu: false,
      tooltipAnalytics: false,
      settingsDropdown: false,
    }
  }

};
</script>

<template>

  <div class="navbarComp">
    <svg class="rounded-figure" style="z-index: 2" v-on:click="position=!position"
         xmlns="http://www.w3.org/2000/svg" height="34px" viewBox="0 -960 960 960" width="34px" fill="#FFF">
      <path d="M120-240v-80h720v80H120Zm0-200v-80h720v80H120Zm0-200v-80h720v80H120Z"/>
    </svg>
    <svg style="opacity: 1; z-index: 1" v-on:mousemove="tooltipMenu = true" v-on:mouseout="tooltipMenu = false"
         :style="position ? 'top: 4rem; opacity:1': 'top: 1rem; opacity:0'"
         class="rounded-figure" xmlns="http://www.w3.org/2000/svg"
         height="34px" viewBox="0 -960 960 960" width="34px" fill="#FFF">
      <path
          d="M246.78-206.78H347V-453h266v246.22h100.22v-349.83L480-731.52 246.78-556.61v349.83Zm-106 106v-508.83L480-864.31 819.22-609.8v509.02H515.48v-254.7h-70.96v254.7H140.78ZM480-468.87Z"/>
    </svg>
    <div class="tooltip py-2" style="left: 5rem; top: 4rem" :style="tooltipMenu ? 'opacity:1' : 'opacity:0'">
      Головна\Картка
    </div>
    <svg style="opacity: 1; z-index: 1" v-on:mousemove="tooltipAnalytics = true"
         v-on:mouseout="tooltipAnalytics = false"
         :style="position ? 'top: 7rem; opacity:1': 'top: 1rem; opacity:0'"
         class="rounded-figure" xmlns="http://www.w3.org/2000/svg" height="34px" viewBox="0 -960 960 960" width="34px"
         fill="#FFF">
      <path
          d="M120-120v-77.33L186.67-264v144H120Zm163.33 0v-237.33L350-424v304h-66.67Zm163.34 0v-304l66.66 67.67V-120h-66.66ZM610-120v-236.33L676.67-423v303H610Zm163.33 0v-397.33L840-584v464h-66.67ZM120-346.33v-94.34l280-278.66 160 160L840-840v94.33L560-465 400-625 120-346.33Z"/>
    </svg>
    <div class="tooltip py-2" style="left: 5rem; top: 7rem" :style="tooltipAnalytics ? 'opacity:1' : 'opacity:0'">
      Історія платежів
    </div>
    <div id="NavDropDown">
      <svg class="rounded-figure" xmlns="http://www.w3.org/2000/svg" height="34px" viewBox="0 -960 960 960" width="34px"
         v-on:click="settingsDropdown=!settingsDropdown"
         fill="#FFFFFF"
         :style="position ? 'top: 10rem; opacity:1': 'top: 1rem; opacity:0'">
        <path
          d="m370-80-16-128q-13-5-24.5-12T307-235l-119 50L78-375l103-78q-1-7-1-13.5v-27q0-6.5 1-13.5L78-585l110-190 119 50q11-8 23-15t24-12l16-128h220l16 128q13 5 24.5 12t22.5 15l119-50 110 190-103 78q1 7 1 13.5v27q0 6.5-2 13.5l103 78-110 190-118-50q-11 8-23 15t-24 12L590-80H370Zm70-80h79l14-106q31-8 57.5-23.5T639-327l99 41 39-68-86-65q5-14 7-29.5t2-31.5q0-16-2-31.5t-7-29.5l86-65-39-68-99 42q-22-23-48.5-38.5T533-694l-13-106h-79l-14 106q-31 8-57.5 23.5T321-633l-99-41-39 68 86 64q-5 15-7 30t-2 32q0 16 2 31t7 30l-86 65 39 68 99-42q22 23 48.5 38.5T427-266l13 106Zm42-180q58 0 99-41t41-99q0-58-41-99t-99-41q-59 0-99.5 41T342-480q0 58 40.5 99t99.5 41Zm-2-140Z"/>
      </svg>

  </div>
  </div>
</template>

<style>
@import "animate.css";

.rounded-figure {
  position: fixed;
  background-color: rgba(0, 0, 0, 0.09) !important;
  padding: 5px;
  top: 1rem;
  left: 2rem;
  border-radius: 50%;
  transition-duration: 0.4s;
}

.rounded-figure:hover {
  background-color: rgba(0, 0, 0, 0.3) !important;
  cursor: pointer !important;
}

.rounded-figure:active {
  animation: pulse 0.3s;
}

.tooltip {
  background-color: rgba(0, 0, 0, 0.4) !important;
  position: fixed;
  padding: 5px;
  border-radius: 10%;
  user-select: none;
  text-align: center;
  font-family: sans-serif;
  color: white;
  transition-duration: 0.5s;
}


@keyframes pulse {
  from {
    transform: scale3d(1, 1, 1);
  }

  50% {
    transform: scale3d(1.15, 1.15, 1.15);
  }

  to {
    transform: scale3d(1, 1, 1);
  }
}
</style>