<template>
  <main class="dashboard">
    <br/>
    <div>
    <h1>Flashcards</h1>
    </div>
    <div>
    <div class="container">
    <div>
      <h2>Play again</h2>
      <br />
      <div v-if="do_it_again.length">
        <table>
          <thead>
            <th style="padding: 30px">Title</th>
            <th style="padding: 20px">Recent score</th>
            <th style="padding: 20px">Last played</th>
          </thead>
          <tbody>
            <tr v-for="(i, idx) in do_it_again" :key="idx">
              <td>
                <router-link  style = "border-color: lightblue; background-color: lightblue;" id="title" :to="{ name: 'flashcards', params: { username: $route.params.username, title: i.title } }">
                  {{ i.title }}
                </router-link>
                <br />
                <br />
              </td>
              <td style="padding: 20px;">
                {{ i.rec_score }}
                <br />
                <br />
              </td>
              <td style="padding: 20px;">
                {{ formatdatetime(i.date_time) }}
                <br />
                <br />
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div v-else>You haven't played anything yet</div>
      <br />
      <h2>Try someting new</h2>
      <br />
      <div class="deck-container" v-if="try_smtg_new.length">
        <div class="deck-item" v-for="(i, idx) in try_smtg_new" :key="idx">
          <router-link style="border-color: LightPink; background-color: LightPink" id="title" :to="{ name: 'flashcards', params: { username: $route.params.username, title: i.title } }">
            {{ i.title }}
          </router-link>
          &nbsp;&nbsp;
          <br />
        </div>
      </div>
    </div>
    <div class="btn-div">
      <button class="logout">
        <router-link @click="logout" to="/"> Log out </router-link>
      </button>

      <button class="create-deck">
        <router-link   :to="{ name: 'create', params: { username: $route.params.username } }"> create a deck </router-link>
      </button>

      <button class="delete-deck">
        <router-link   :to="{ name: 'dele', params: { username: $route.params.username } }"> delete a deck </router-link>
      </button>

      <button class="edit-deck">
        <router-link   :to="{ name: 'edit', params: { username: $route.params.username } }"> edit a deck </router-link>
      </button>

      <button class="export-deck">
        <router-link  :to="{ name: 'export', params: { username: $route.params.username } }"> export a deck </router-link>
      </button>

    </div>
    </div>
    </div>
  </main>
</template>
<style>
.dashboard {
  display: flex;
  flex-direction: column;
  margin: auto;
  background-color: Lavender;
  font-size: larger;
  border-radius: 100px;
  border-style: hidden;
  padding:20px;
}
.container{
  display: flex;
  flex-direction:row;
  justify-content: space-between;
  padding: 30px 80px;
}
.btn-div{
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}
#title {
  text-decoration: none;
  border-style: solid;
  color: Black;
  padding: 30px;
  border-radius: 25px;
}

a{
text-decoration: none;
color: Black;
}
.logout,.create-deck,.delete-deck,.edit-deck,.export-deck {
  text-decoration: none;
  background-color: transparent;
  color: Black;
  padding: 30px;
  border-style: solid;
  border-radius: 25px;
}
.logout{
  color: Black;
  background-color: red;
  border: 1px red solid;
}

.create-deck{
  color: Black;
  background-color: plum;
  border: 1px plum solid;
}

.delete-deck{
  color: Black;
  background-color: orchid;
  border: 1px orchid solid;
}

.edit-deck{
  color: Black;
  background-color: mediumpurple;
  border: 1px mediumpurple solid;
}

.export-deck{
  color: Black;
  background-color: darkorchid;
  border: 1px darkorchid solid;
}


.deck-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  flex-wrap: wrap;
  height: fit-content;
  padding: 5px;
  row-gap: 25px;
}
.deck-item {
  padding: 30px 5px;
  text-align: center;
}
</style>
<script>
import axios from "axios";

import moment from "moment";

export default {
  data() {
    return {
      do_it_again: [],
      try_smtg_new: [],
    };
  },
  methods: {
    formatdatetime(value) {
      if (value) {
        return moment(String(value)).format("MM/DD/YYYY hh:mm");
      }
    },
    getTitle() {
      const path = `http://localhost:5000/dashboard/${this.$route.params.username}`;
      axios
        .get(path)
        .then((res) => {
          this.do_it_again = res.data.do_it_again;
          this.try_smtg_new = res.data.try_smtg_new;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    logout() {
      const path = "http://localhost:5000/logout";
      axios
        .post(path, { username: this.$route.params.username })
        .then(() => {
          // eslint-disable-next-line
          console.log("logged out");
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
  },
  created() {
    this.getTitle();
  },
};
</script>
