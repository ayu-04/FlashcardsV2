<template>
	<main class="edit">
  <br/>
  <div v-if="decks.length">
    <h1 align="center">Select the deck you want to edit</h1>
    <br>
    <div class="grid-container">
    <div class="grid-item" v-for="(i,idx) in decks" :key="idx">
      <router-link id="button"
      style="border-color:LightBlue;background-color:LightBlue;"
      :to="{ name: 'deck_edit', params: { username:$route.params.username, title:i.title } }">
      {{i.title}}
      </router-link>
      <br/>
      <br/>
      <br/>
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
  .edit{background-color:MediumPurple;
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
