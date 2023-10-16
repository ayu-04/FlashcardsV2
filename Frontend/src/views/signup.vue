<template>
  <div class="signup">
    <br/>
    <h1 align="center">Sign Up</h1>
    <form @submit="onSubmit" id="signup-form">
    <p>
      Email&nbsp;&nbsp;
      <input
        type="email"
        name="email"
        required
        placeholder="Enter Email"
        v-model="signupform.email" />
    </p>
    <p>
      Username&nbsp;&nbsp;
      <input
        type="text"
        name="username"
        required
        placeholder="Enter Username"
        v-model="signupform.username" />
    </p>
    <p>
      Password&nbsp;&nbsp;
      <input
        type="password"
        name="password"
        required
        placeholder="Enter Password"
        v-model="signupform.password" />
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
signupform: {
email:'',
username: '',
password: '',
},
};
},
methods: {
onSubmit(evt) {
evt.preventDefault();
const payload = {
email:this.signupform.email,
username: this.signupform.username,
password: this.signupform.password,
};
const path = 'http://localhost:5000/create_account';
axios.post(path, payload)
.then(() => {
// eslint-disable-next-line
console.log('a');
this.$router.push({name:'dashboard',params:{username:this.signupform.username,}});
})
.catch((error) => {
// eslint-disable-next-line
console.log(error);
this.$router.push('/userexists');
});
},
},
};
</script>
<style>
.signup {background-color:Lavender ;
font-size:larger;
border-radius: 100px;
margin: 100px;
border-style: hidden;
height: 500px;}
#sub {text-decoration:none;
color:Black;
padding:30px;
border-style:solid;
border-color:LightBlue;
background-color:LightBlue;
border-radius: 25px;}
</style>
