<template>
<main class="create">
  <br/>
  <h1 align="center">Create a deck</h1>
  <form @submit="createdeck">
    <p>
    Title&nbsp;&nbsp;<input type="text" name="title" required placeholder="Enter title" v-model="title"/>
    </p>
    <p>
    Number of cards&nbsp;&nbsp;<input type="integer" name="no_cards" required placeholder="Enter number of cards" v-model="no_cards"/>
    </p>
    <p>
    <input id="button" style="border-color: LightBlue;background-color:LightBlue;" type="submit" name="submit_button" value="Create"/>
    </p>
  </form>
  <br/>
  <p>	
  <router-link id="button" style="border-color:Lavender;background-color:Lavender;" :to="{ name: 'dashboard', params: { username: $route.params.username } }">
  Go to dashboard
  </router-link>
  </p>
</main>
</template>
<style>
    .create{background-color:Plum ;
    font-size:larger;
    border-radius: 100px;
    margin: 100px;
    border-style: hidden;
    height:600px;
    padding:10px;}
    #button{padding:30px;
    border-style:solid;
    text-decoration:none;
    border-radius: 25px;
    color:black;}
</style>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      title: '',
      no_cards: null,
    };
  },
  methods: {
    createdeck(evt) {
      evt.preventDefault();
      const payload = {
        title: this.title,
        no_of_cards: this.no_cards,
      };
      const path = `http://localhost:5000/${this.$route.params.username}/decks`;
      axios.post(path, payload)
        .then(() => {
        this.$router.push({name:'create_card', params: {username:this.$route.params.username, title:this.title, no_cards:this.no_cards } });
        })
        .catch((error) => {
        // eslint-disable-next-line
        console.log(error);
        this.$router.push({name: 'titleexists', params: {username:this.$route.params.username } });
        });
    },
  },
};
</script>