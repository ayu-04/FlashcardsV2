<template>
  <div class="login">
    <br/>
    <h1 align="center">Login</h1>
    <form @submit="onSubmit" id="login-form">
    <p>
      Username&nbsp;&nbsp;
      <input
        type="text"
        name="username"
        required
        placeholder="Enter Username"
        v-model="loginform.username" />
    </p>
    <p>
      Password&nbsp;&nbsp;
      <input
        type="password"
        name="password"
        required
        placeholder="Enter Password"
        v-model="loginform.password" />
    </p>
    <p>
      <input id="sub" type="submit" name="submit_button" value="OK" />
    </p>
  </form>
</div>
</template >

<script>
import axios from 'axios';

export default {
  data() {
    return {
      loginform: {
      username: '',
      password: '',
      },
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        username: this.loginform.username,
        password: this.loginform.password,
      };
      const path = 'http://localhost:5000/';
      axios.post(path, payload)
        .then(() => {
        this.$router.push({name:'dashboard',params:{username:this.loginform.username,}});
        })
        .catch((error) => {
        // eslint-disable-next-line
        console.log(error);
        this.$router.push('/incpass')
        });
    },
  },
};
</script>
<style>
.login {background-color:Lavender ;
font-size:larger;
border-radius: 100px;
margin: 100px;
border-style: hidden;
height: 400px;}
#sub {text-decoration:none;
color:Black;
padding:30px;
border-style:solid;
border-color:LightBlue;
background-color:LightBlue;
border-radius: 25px;}
</style>
