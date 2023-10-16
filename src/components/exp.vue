<template>
<main class="exp">
<br/>
<div v-if="decks.length">
  <h1 align="center">Select the deck you want to export</h1>
  <br>
  <div class="grid-container">
  <div class="grid-item" v-for="(i,idx) in decks" :key="idx">
    <button id="button"
    style="border-color:LightPink;background-color:LightPink;"
    @click="exp(i.title)">
    {{i.title}}
    </button>
  </div>
  </div>
</div>
<div v-else>
  <h2> You don't have any decks</h2>
</div>
<br/>
<br/>
<p>
  <router-link id="button"
  style="border-color:Lavender;background-color:Lavender;"
  :to="{ name: 'dashboard', params: { username: $route.params.username } }">
  Go to dashboard
  </router-link>
</p>
</main>
</template>
<style>
  .exp{background-color:DarkOrchid;
  font-size:larger;
  border-radius: 100px;
  margin: 100px;
  border-style: hidden;
  height:600px;
  padding:10px;}
  #button{text-decoration:none;
  border-style:solid;
  color:Black;
  padding:30px;
  border-radius: 25px;}
  .grid-container {
  display: grid;
  grid-template-columns: auto auto auto;
  padding: 5px;
  }
  .grid-item {
  padding: 5px;
  font-size: 30px;
  text-align: center;
  }
</style>
<script>
  import axios from 'axios';

  export default {
    data() {
      return {
      decks: [],
      };
    },
    methods: {
      exp(t) {
        const path = `http://localhost:5000/${this.$route.params.username}/export`;
        const payload = {
          title: t,
        };
        axios.post(path, payload)
          .then((res) => {
          // eslint-disable-next-line
          console.log(res);
          // eslint-disable-next-line
          alert('Your deck has been exported');
          })
          .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          });
      },
      getDecks() {
        const path = `http://localhost:5000/${this.$route.params.username}/decks`;
        axios.get(path)
          .then((res) => {
          // eslint-disable-next-line
          console.log('got decks');
          this.decks = res.data.decks;
          })
          .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          });
      },
    },
    created() {
      this.getDecks();
    },
  };
</script>
