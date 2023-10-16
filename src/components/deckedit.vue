<template>
	<main class="deckedit">
  <div><br/></div>
  <router-link style="border-color:LightPink;background-color:LightPink;"
  id="button"
  :to="{ name: 'deck_edit_card_create', params: { username: $route.params.username, title: $route.params.title } }">
  Add Card
  </router-link>
  <div v-if="c.length">
    <br/>
	  <h1 align="center">Select the card you want to edit</h1>
	  <br/>
    <table style="border: 2px solid white;" align="center">
      <thead>
        <tr>
          <th style="border: 1px solid white; padding:10px" scope="col"><h2>Question</h2></th>
          <th style="border: 1px solid white; padding:10px" scope="col"><h2>Answer</h2></th>
          <th style="border: 1px solid white; padding:10px"></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(i, index) in c" :key="index">
          <td style="border: 1px solid white; padding:10px"><h3>{{ i.question }}</h3></td>
          <td style="border: 1px solid white; padding:10px"><h3>{{ i.answer }}</h3></td>
          <td style="border: 1px solid white; padding:10px">
            <div>
              <router-link style="border-color:LightBlue;background-color:LightBlue;"
              id="button"
              :to="{ name: 'deck_edit_card_edit', params: { username: $route.params.username, title: $route.params.title, card_no: i.card_no } }">
              Update
              </router-link>
              &nbsp;&nbsp;&nbsp;
              <button style="border-color:PaleVioletRed;background-color:PaleVioletRed;"
              id="button"
              @click="dele(i.card_no)">
              Delete
              </button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
	</div>
	<div v-else>
	  <h2> You don't have any cards in this deck</h2>
	</div>
	<br>
	<p>
	<router-link id="button"
  style="border-color:Lavender;background-color:Lavender;"
  :to="{ name: 'dashboard', params: { username: $route.params.username } }">
  Go to dashboard
  </router-link>
  </p>
	</div>
	</main>
</template>
<style>
  .deckedit{background-color:MediumPurple ;
  font-size:larger;
  border-radius: 100px;
  margin: 100px;
  border-style: hidden;
  height:1800px;
  padding:10px;}
  #button{text-decoration:none;
  border-style:solid;
  color:Black;
  padding:30px;
  border-radius: 25px;}
</style>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      c: [],
    };
  },
  methods: {
    getCards() {
      const path = `http://localhost:5000/${this.$route.params.username}/cards/${this.$route.params.title}`;
      axios.get(path)
        .then((res) => {
          this.c = res.data.c;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    dele(c_no) {
      const path = `http://localhost:5000/${this.$route.params.username}/card/${this.$route.params.title}/${c_no}`;
      axios.delete(path)
        .then(() => {
          // eslint-disable-next-line
          console.log('deleted');
          this.getCards();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getCards();
  },
};
</script>
