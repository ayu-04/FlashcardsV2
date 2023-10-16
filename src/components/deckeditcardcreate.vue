<template>
  <main class="deckeditcardcreate">
    <div>
      <br/>
      <h1 align="center">Create a card</h1>
      <form @submit="createcard">
        <p>
        Question&nbsp;&nbsp;
        <input type="text" name="question" required placeholder="Enter question" v-model="question"/>
        </p>
        <p>
        Answer&nbsp;&nbsp;
        <input type="text" name="answer" required placeholder="Enter answer" v-model="answer"/>
        </p>
        <p>
        <input id="button" style="border-color:LightBlue; background-color: LightBlue;"  type="submit" name="submit_button" value="Create">
        </p>
      </form>
    </div>
  </main>
</template>
<style>
    .deckeditcardcreate{background-color:MediumPurple ;
    font-size:larger ;
    border-radius: 100px;
    margin: 100px;
    border-style: hidden;
    padding:10px;}
    #button{border-style:solid;
    color:Black;
    padding:30px;
    border-radius: 25px;}
</style>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      question: '',
      answer: '',
    };
  },
  methods: {
    createcard(evt) {
      evt.preventDefault();
      const payload = {
        question: this.question,
        answer: this.answer,
      };
      const path = `http://localhost:5000/${this.$route.params.username}/cards/${this.$route.params.title}`;
      axios.post(path, payload)
        .then(() => {
        this.$router.push({ name: 'deck_edit', params:{ username: this.$route.params.username, title: this.$route.params.title } });
        })
        .catch((error) => {
        // eslint-disable-next-line
        console.log(error);
        });
    },
  },
};
</script>
