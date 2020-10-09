<template>
  <div class="pitch">
    <div class="away-corner-left"></div>
    <div class="away-corner-right"></div>
    <div class="away-six-yard-box"></div>
    <div class="away-box"></div>
    <div class="away-box-half-circle"></div>
    <div class="centre-circle"></div>
    <div class="centre-line"></div>
    <div class="home-box"></div>
    <div class="home-box-half-circle"></div>
    <div class="home-six-yard-box"></div>
    <div class="home-corner-left"></div>
    <div class="home-corner-right"></div>
  </div>
</template>

<script>
export default {
  name: 'Pitch',
  data () {
    return {}
  }
}
</script>

<style scoped>

* {
  box-sizing:border-box;
}

.pitch {
  background: linear-gradient(
    to bottom,
    #5d9634,
    #5d9634 50%,
    #538c2b 50%,
    #538c2b
  );
  background-size: 100% 20vmin;
  border: solid 3px #fff;
  position: relative;
  height: 100%;
  width: 75%;
}

.away-six-yard-box {
  position: absolute;
  border-left: solid 3px #fff;
  border-right: solid 3px #fff;
  border-bottom: solid 3px #fff;
  bottom: 92.5%;
  left: 35%;
  right: 35%;
  top: 0;
}

.away-box {
  position: absolute;
  border-left: solid 3px #fff;
  border-right: solid 3px #fff;
  border-bottom: solid 3px #fff;
  bottom: 80%;
  left: 20%;
  right: 20%;
  top: 0;
}

.away-box-half-circle {
  position: absolute;
  border-left: solid 3px #fff;
  border-right: solid 3px #fff;
  border-bottom: solid 3px #fff;
  left: 30%;
  right: 30%;
  top: 20%;
  bottom: 75%;
  border-radius: 50% / 100%;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

.home-box {
  position: absolute;
  border-left: solid 3px #fff;
  border-right: solid 3px #fff;
  border-top: solid 3px #fff;
  bottom: 0;
  left: 20%;
  right: 20%;
  top: 80%;
}

.centre-circle {
  position: absolute;
  border: solid 3px #fff;
  border-radius: 100%;
  bottom: 40%;
  left: 30%;
  right: 30%;
  top: 40%;
}

.home-box-half-circle {
  position: absolute;
  border-left: solid 3px #fff;
  border-right: solid 3px #fff;
  border-top: solid 3px #fff;
  left: 30%;
  right: 30%;
  top: 75%;
  bottom: 20%;
  border-radius: 50% / 100%;
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;
}

.home-six-yard-box {
  position: absolute;
  border-left: solid 3px #fff;
  border-right: solid 3px #fff;
  border-top: solid 3px #fff;
  bottom: 0;
  left: 35%;
  right: 35%;
  top: 92.5%;
}

.centre-line {
  position: absolute;
  border-bottom: solid 3px #fff;
  bottom: 50%;
  left: 0;
  right: 0;
  top: 0;
}

.away-corner-left {
  position: absolute;
  width: 25px;
  height: 25px;
  top: 0%;
  left: 0%;
  border-radius: 0 0 50px 0;
  border-right: 3px solid aliceblue;
  border-bottom: 3px solid aliceblue;
}

.away-corner-right {
  position: absolute;
  width: 25px;
  height: 25px;
  top: 0%;
  right: 0%;
  border-radius: 0 0 0 50px;
  border-left: 3px solid aliceblue;
  border-bottom: 3px solid aliceblue;
}

.home-corner-right {
  position: absolute;
  width: 25px;
  height: 25px;
  bottom: 0%;
  right: 0%;
  border-radius: 50px 0 0 0;
  border-left: 3px solid aliceblue;
  border-top: 3px solid aliceblue;
}

.home-corner-left {
  position: absolute;
  width: 25px;
  height: 25px;
  bottom: 0%;
  left: 0%;
  border-radius: 0 50px 0 0;
  border-right: 3px solid aliceblue;
  border-top: 3px solid aliceblue;
}
</style>
