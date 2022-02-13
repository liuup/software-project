<template>
  <div id="nav">
    <router-link to="/">User</router-link> |
    <router-link to="/guard">Guard</router-link>
  </div>
  <router-view/>
</template>

<style>
#app {
  text-align: center;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}

#nav a.router-link-exact-active {
  color: #409EFF;
  text-decoration: none;
}
</style>
