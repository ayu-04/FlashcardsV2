<template>
  <div id="app">
    <div id="nav">
      <h3>
      <router-link to="/">Login</router-link> |
      <router-link to="/signup">Sign Up</router-link>
      </h3>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #C3B1E1;
  height:2000px;
  padding:10px;
}

#nav {
  padding: 10px;
}

#nav a {
  font-weight: bold;
  color: #440682;
}

#nav a.router-link-exact-active {
  color: #7B0CBF;
}
</style>
