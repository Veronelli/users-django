import axios from 'axios'

class ServerConnection{
    bad_connection = {"server_connection": "offline", "server_status": false }

    async verifyConnection(){
        try {
            const json = await axios
                .get('http://localhost:8000/api/status/');
            return json.data;
        }
        catch (e) {
            return this.bad_connection
        }
    }

    async login(user){
        try {
            const json = await axios
                .post('http://localhost:8000/api/login',
                user);
            return json.data;
        }
        catch (e) {
            return this.bad_connection 
        }
    }

    async verifyToken(){
         
            const token = localStorage.getItem('my_app');
            const tokenJson = {}

            tokenJson.token = JSON.parse(token)

            const json = await axios.post("http://localhost:8000/api/verify",{},{headers:{
                token:tokenJson.token
            }}).catch(err=>{return err.response})
            return json.data.token
        
    }

}
export default ServerConnection;