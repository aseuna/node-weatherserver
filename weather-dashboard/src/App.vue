<template>
  <div id="app">

    <Home/>
  </div>
</template>

<script>
import Home from "./components/Home.vue";

export default {
  name: 'app',
  components: {
    Home
  }
}
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 50px;
}
</style>
