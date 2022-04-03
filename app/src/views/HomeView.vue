<template>
  <div class="home">
    <div class="container mt-5">
      <div class="row">
        <div class="col-5 overflow-hidden">
          <img src="../assets/employeeretention.png" alt />
        </div>

        <div class="col-7 pe-5 px-5">
          <div class="card h-100">
            <div class="card-header">
              <h1>Login</h1>
            </div>
            <div class="card-body">
              <form>
                <p v-if="validUser" class="text-danger">Nombre o contraseña incorrecta</p>
                <div class="mb-3" style="text-align:left">
                  <label for="exampleInputEmail1" class="form-label">Name</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Facundo"
                    v-model="user.name"
                    id="exampleInputEmail1"
                    state="false"
                    required
                    aria-describedby="emailHelp"
                  />
                  <div v-if="error.name" class="form-text">Nombre invalido</div>
                </div>
                <div class="mb-3" style="text-align:left">
                  <label for="exampleInputPassword1" class="form-label">Password</label>
                  <input
                    type="password"
                    v-model="user.password"
                    placeholder="Test"
                    class="form-control"
                    id="exampleInputPassword1"
                    required
                  />
                  <div v-if="error.password" class="form-text">Contraseña invalida</div>
                </div>
                <div class="d-grid gap-2">
                  <button class="btn btn-primary" v-on:click="submit">Iniciar</button>
                </div>
                <p class="text-muted pt-2" style="text-align:left;font-weight:500;">
                  No tienes una cuenta?
                  <a href="#" class="text-reset" style="font-weight:500">Registrate</a>.
                </p>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <Toast />
</template> 

<script>
import ServerConnection from '@/services/server-connection.service'
import Toast from '../components/Toast.vue'
const serviceServer = new ServerConnection()

export default {

  name: 'HomeView',
  props: {},
  components: {
    Toast

  },
  data: () => ({
    user: {
      name: null,
      password: null

    },
    error: {},
    validUser: false
  }),
  methods: {
    async submit(e) {
      e.preventDefault()
      for (const item in this.user) {
        if (this.user[item]==='' || this.user[item] == null) {
          this.error[item] = true
        }
        else{
          this.error[item] = false

        }
      }
      const data = await serviceServer.login(this.user)
      if (data.jwt) {
        localStorage.setItem("my_app", JSON.stringify(data.jwt))
        this.$router.push('dashboard')
      }
      else {
        this.validUser = true
      }
    }
  },

}
</script>
