<template>

  <div class="home">
    <div class="container mt-5" >
      <div class="row">
        <div class="col-4 overflow-hidden">
          <img src="../assets/employeeretention.png" alt="">
        </div>
        <div class="col-8">
        <h1>Login</h1>
        <hr>
        </div>
      </div>
    </div>
  </div>
  <Toast />
</template>

<script>
import Toast from '../components/Toast.vue'
export default {
  
  name: 'HomeView',
  props:{},
  components: {
    Toast
    
  }
}
</script>
