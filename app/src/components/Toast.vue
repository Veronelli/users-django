<template>
    <div class="toast show">
        <div class="toast-header d-flex justify-content-between">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-circle-fill" viewBox="0 0 16 16">
  <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 4a.905.905 0 0 0-.9.995l.35 3.507a.552.552 0 0 0 1.1 0l.35-3.507A.905.905 0 0 0 8 4zm.002 6a1 1 0 1 0 0 2 1 1 0 0 0 0-2z"/>
</svg>
            <p>{{ msg }}</p>
            <button
                type="button"
                class="btn-close"
                data-bs-dismiss="toast"
            ></button>
        </div>
    </div>
</template>

<style>
.justify-content-between {
    align-items: center;
}
.toast {
    top: 20px;
    left: 20px;
    position: absolute;
}
p {
    font-weight: 600;
    margin: 0px;
    padding: 0px;
}
</style>

<script >
import ServerConnection from '../services/server-connection.service'
const serviceServer = new ServerConnection
export default {
    name: 'ComToast',
    async mounted() {
        this.server_status = await this.getServerStatus();
        
        if(this.server_status.server_status == true){
            this.msg = "Connection was successfully"
        }
        else{
            this.msg = "Connection was not successfully"
        }
    },
    methods: {
        async getServerStatus() {
            return serviceServer.verifyConnection()
        },

    },
    data: () => ({
        msg: "Connecting to the Back-end server",

    }),
}
</script>
