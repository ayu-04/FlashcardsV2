<template>
  <main class="deckeditcardedit">
    <div>
      <br/>
      <h1 align="center">Edit a card</h1>
      <form @submit="putCard">
        <p>
        Question&nbsp;&nbsp;
        <input type="text" name="question" required v-model="question"/>
        </p>
        <p>
        Answer&nbsp;&nbsp;
        <input type="text" name="answer" required v-model="answer"/>
        </p>
        <p>
        <input id="button"
        style="border-color:LightBlue; background-color: LightBlue;" 
        type="submit"
        name="submit_button"
        value="Ok">
        </p>
      </form>
    </div>
  </main>
</template>
<style>
    .deckeditcardedit{background-color:MediumPurple ;
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
    putCard(evt) {
      evt.preventDefault();
      const payload = {
        question: this.question,
        answer: this.answer,
      };
      const path = `http://localhost:5000/${this.$route.params.username}/card/${this.$route.params.title}/${this.$route.params.card_no}`;
      axios.put(path, payload)
        .then(() => {
        // eslint-disable-next-line
        console.log('card edited');
        this.$router.push({ name: 'deck_edit', params:{ username: this.$route.params.username, title:this.$route.params.title } });
        })
        .catch((error) => {
        // eslint-disable-next-line
        console.log(error);
        });
    },
    getCard() {
      const path = `http://localhost:5000/${this.$route.params.username}/card/${this.$route.params.title}/${this.$route.params.card_no}`;
      axios.get(path)
        .then((res) => {
        this.question=res.data.question;
        this.answer=res.data.answer;
        })
        .catch((error) => {
        // eslint-disable-next-line
        console.log(error);
        });
    },
  },
  created() {
    this.getCard();
  },
};
</script>
