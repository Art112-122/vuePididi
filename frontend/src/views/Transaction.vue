<script>

export default {
  name: "TransactionTo",
  data () {return {
    inputValue: 1,
    cardInputValue: null
  }},
  methods: {
    checkValue() {

      switch (this.inputValue) {
        case 1:

      }

      if (this.inputValue <= 0 || this.inputValue === null) {
        this.inputValue = 1;
      }
      else if (this.inputValue >= 1000000) {
        this.inputValue = 999999;
      }
    },
    // cardInputFunc() {
    //   if (this.cardInputValue.length>4) {
    //
    //   }
    // }
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
  <div class="fixed-grid has-9-cols">
    <div class="grid">
      <div class="cell is-col-start-3">

      </div>


      <div class="cell is-col-start-5">
        <h1 class="title is-1" style="width: 30rem; text-align: center">Переказ</h1>

        <input v-model="inputValue" v-on:focusout="checkValue" value="{{inputValue}}" class="input-int input mb-6"
               min="1" max="999999" style="" type="number" required>


        <div class="container">
          <div class="left-side">
            <div class="card">
              <div class="card-line"></div>
              <div class="buttons"></div>
            </div>
            <div class="post">
              <div class="post-line"></div>
              <div class="screen">
                <div class="dollar">$</div>
              </div>
              <div class="numbers"></div>
              <div class="numbers-line2"></div>
            </div>
          </div>
          <div class="right-side">
            <div class="new">Підтвердити транзакцію</div>

            <svg viewBox="0 0 451.846 451.847" height="512" width="512" xmlns="http://www.w3.org/2000/svg"
                 class="arrow">
              <path fill="#cfcfcf" data-old_color="#000000" class="active-path" data-original="#000000"
                    d="M345.441 248.292L151.154 442.573c-12.359 12.365-32.397 12.365-44.75 0-12.354-12.354-12.354-32.391 0-44.744L278.318 225.92 106.409 54.017c-12.354-12.359-12.354-32.394 0-44.748 12.354-12.359 32.391-12.359 44.75 0l194.287 194.284c6.177 6.18 9.262 14.271 9.262 22.366 0 8.099-3.091 16.196-9.267 22.373z"></path>
            </svg>

          </div>
        </div>
      </div>
      <div class="cell is-col-start-3">
        <h1 class="title is-1">{{cardNumber}}</h1>
        <h3 class="title is-3">{{userName}}</h3>
      </div>
    </div>
  </div>


  </body>
  </html>
</template>

<style scoped>


.input-int {

  border: none;
  box-shadow: none;
  text-align: center;
  font-size: 5rem;
  font-family: 'Impact';
  background-color: rgba(207, 207, 207, 0);
  input::-webkit-outer-spin-button,
  input::-webkit-inner-spin-button {
    display: none;
    -webkit-appearance: none;
    margin: 0; /* <-- Apparently some margin are still there even though it's hidden */
  }
}



/* submit anim */
.container {
  background-color: #292929;
  display: flex;
  width: 460px;
  height: 120px;
  position: relative;
  border-radius: 10px;
  transition: 0.3s ease-in-out;
}

.container:hover {
  transform: scale(1.03);
  width: 220px;
}

.container:hover .left-side {
  width: 100%;
}

.left-side {
  background-color: #5de2a3;
  width: 130px;
  height: 120px;
  border-radius: 10px;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  transition: 0.3s;
  flex-shrink: 0;
  overflow: hidden;
}

.right-side {
  width: calc(100% - 130px);
  display: flex;
  align-items: center;
  overflow: hidden;
  cursor: pointer;
  justify-content: space-between;
  white-space: nowrap;
  transition: 0.3s;
}

.right-side:hover {
  background-color: #f9f7f9;
}

.arrow {
  width: 20px;
  height: 20px;
  margin-right: 20px;
}

.new {
  font-size: 23px;
  font-family: "Lexend Deca", sans-serif;
  margin-left: 20px;
}

.card {
  width: 70px;
  height: 46px;
  background-color: #c7ffbc;
  border-radius: 6px;
  position: absolute;
  display: flex;
  z-index: 10;
  flex-direction: column;
  align-items: center;
}

.card-line {
  width: 65px;
  height: 13px;
  background-color: #80ea69;
  border-radius: 2px;
  margin-top: 7px;
}

@media only screen and (max-width: 480px) {
  .container {
    transform: scale(0.7);
  }

  .container:hover {
    transform: scale(0.74);
  }

  .new {
    font-size: 18px;
  }
}

.buttons {
  width: 8px;
  height: 8px;
  background-color: #379e1f;
  box-shadow: 0 -10px 0 0 #26850e, 0 10px 0 0 #56be3e;
  border-radius: 50%;
  margin-top: 5px;
  transform: rotate(90deg);
  margin: 10px 0 0 -30px;
}

.container:hover .card {
  animation: slide-top 1.2s cubic-bezier(0.645, 0.045, 0.355, 1) both;
}

.container:hover .post {
  animation: slide-post 1s cubic-bezier(0.165, 0.84, 0.44, 1) both;
}

@keyframes slide-top {
  0% {

    transform: translateY(0);
  }

  50% {

    transform: translateY(-70px) rotate(90deg);
  }

  60% {

    transform: translateY(-70px) rotate(90deg);
  }

  100% {

    transform: translateY(-8px) rotate(90deg);
  }
}

.post {
  width: 63px;
  height: 75px;
  background-color: #373737;
  position: absolute;
  z-index: 11;
  bottom: 10px;
  top: 120px;
  border-radius: 6px;
  overflow: hidden;
}

.post-line {
  width: 47px;
  height: 9px;
  background-color: #545354;
  position: absolute;
  border-radius: 0px 0px 3px 3px;
  right: 8px;
  top: 8px;
}

.post-line:before {
  content: "";
  position: absolute;
  width: 47px;
  height: 9px;
  background-color: #757375;
  top: -8px;
}

.screen {
  width: 47px;
  height: 23px;
  background-color: #ffffff;
  position: absolute;
  top: 22px;
  right: 8px;
  border-radius: 3px;
}

.numbers {
  width: 12px;
  height: 12px;
  background-color: #838183;
  box-shadow: 0 -18px 0 0 #838183, 0 18px 0 0 #838183;
  border-radius: 2px;
  position: absolute;
  transform: rotate(90deg);
  left: 25px;
  top: 52px;
}

.numbers-line2 {
  width: 12px;
  height: 12px;
  background-color: #aaa9ab;
  box-shadow: 0 -18px 0 0 #aaa9ab, 0 18px 0 0 #aaa9ab;
  border-radius: 2px;
  position: absolute;
  transform: rotate(90deg);
  left: 25px;
  top: 68px;
}

@keyframes slide-post {
  50% {

    transform: translateY(0);
  }

  100% {

    transform: translateY(-70px);
  }
}

.dollar {
  position: absolute;
  font-size: 16px;
  font-family: "Lexend Deca", sans-serif;
  width: 100%;
  left: 0;
  top: 0;
  color: #4b953b;
  text-align: center;
}

.container:hover .dollar {
  animation: fade-in-fwd 0.3s 1s backwards;
}

@keyframes fade-in-fwd {
  0% {
    opacity: 0;
    transform: translateY(-5px);
  }

  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>