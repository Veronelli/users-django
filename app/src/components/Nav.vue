<template>
  <nav class="nav justify-content-end">
    <router-link class="btn-white" to="/">Home</router-link> 
    <router-link class="btn-white" to="/about">About</router-link>
  </nav>
</template>

<style>
  nav{
    background: #41b883;
  }
  .btn-white{
    color: rgb(255, 255, 255);
    text-decoration: none;
    margin: .5rem;
    font-weight: 650;
  }
  .btn-white:hover{
    color: rgb(221, 221, 221);
  }
</style>

<script>
export default {
  name: 'HelloWld',
}
</script>
