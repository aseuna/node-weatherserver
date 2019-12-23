<template>
    <div id="app">
        <b-nav>
            <b-nav-item><router-link to="/">Etusivu</router-link></b-nav-item>
            <b-nav-item><router-link to="/find">Haku</router-link></b-nav-item>
            <b-nav-item>Meistä</b-nav-item>
        </b-nav>
        <router-view />
    </div>
</template>

<script>

export default {
  name: 'app',
  components: {
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
