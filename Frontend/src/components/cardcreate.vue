<template>
  <main class="cardcreate">
    <br/>
    <div style="width:80%;float:left">
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
    <div style="width:20%;float:left">
      <h2 id="button" style="border-color:LightPink;background-color:LightPink;">Cards left - {{count-1}}</h2>
    </div>
  </main>
</template>
<style>
    .cardcreate{background-color:Plum ;
    font-size:larger ;
    border-radius: 100px;
    margin: 100px;
    border-style: hidden;
    height:500px;
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
      count: this.$route.params.no_cards,
      card_no: 0,
    };
  },
  methods: {
    createcard(evt) {
      evt.preventDefault();
      const payload = {
        question: this.question,
        answer: this.answer,
      };
      const path = `http://localhost:5000/${this.$route.params.username}/card/${this.$route.params.title}/${this.card_no}`;
      axios.post(path, payload)
        .then(() => {
        if (this.count === 1) {
        this.$router.push( {name:'deckdone', params: {username:this.$route.params.username, } });
        }
        else {
          this.question = '';
          this.answer = '';
          this.card_no += 1;
          this.count -= 1;
        }
        })
        .catch((error) => {
        // eslint-disable-next-line
        console.log(error);
        });
    },
  },
};
</script>
