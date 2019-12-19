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
*{
	margin: 0;
	padding: 0;
	border: none;
	font-family: 'Arial', 'Helvetica','sans-serif';
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
