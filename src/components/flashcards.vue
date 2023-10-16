<template>
  <main class="card">
    <br/>
    <h1 align="center">{{$route.params.title}}</h1>
    <div style="width:30%;float:left">
      <h2>Score</h2>
      <p>
        {{rec_score}}
      </p>
      <br/>
      <p>
        <h2>Total cards {{tot_cards}}</h2>
      </p>
      <p>
        <button id="button"
        style="border-color:LightBlue;background-color:LightBlue;"
        @click="next">
          Next
        </button>
      </p>
      <br/>
      <p>
        <button id="button"
        style="border-color:LightPink;background-color:LightPink;"
        @click="retry">
          Retry
        </button>
      </p>
      <br/>
      <p>
        <router-link id="button"
        style="border-color:Red;background-color:Red;"
        :to="{name:'dashboard',params:{username:$route.params.username}}">
          Exit
        </router-link>
      </p>
    </div>
    <div style="width:70%;float:left">
      <br/>
      <div class="flip-card">
        <div class="flip-card-inner">
          <div class="flip-card-front">
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <h1>{{question}}</h1>
          </div>
          <div class="flip-card-back">
            <br/>
            <br/>
            <h1>{{answer}}</h1>
            <br/>
            <br/>
            <br/>
            <div style="display:flex;flex-direction: row;justify-content: space-around;padding: 0px 100px;">
              <button @click="easy" 
              style="padding:10px;border-style:solid;border-radius: 5px;"
              v-bind:style="{backgroundColor:easycolor}">
                Easy
              </button>
              <button @click="medium"
              style="padding:10px;border-style:solid;border-radius: 5px;"
              v-bind:style="{backgroundColor:mediumcolor}">
                Medium
              </button>
              <button @click="hard"
              style="padding:10px;border-style:solid;border-radius: 5px;"
              v-bind:style="{backgroundColor:hardcolor}">
                Hard
              </button>
              <button @click="incorrect"
              style="padding:10px;border-style:solid;border-radius: 5px;"
              v-bind:style="{backgroundColor:incorrectcolor}">
                Incorrect
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
<style>
.flip-card {
  background-color: transparent;
  width: 800px;
  height: 500px;
  border: 1px solid #f1f1f1;
  border-radius: 100px;
  perspective: 1000px;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.8s;
  transform-style: preserve-3d;
}

.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  border-radius: 100px;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
}

.flip-card-front {
  background-color: pink;
  color: black;
}

.flip-card-back {
  background-color: RoyalBlue;
  color: white;
  transform: rotateY(180deg);
}

.card{background-color: Lavender ;
font-size:larger;
border-radius: 100px;
margin: 100px;
border-style: hidden;
height:900px;
padding:10px;}

#button{text-decoration:none;
color:Black;
padding:30px;
border-style:solid;
border-radius: 25px;}
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
    question: '',
    answer: '',
    score: 0,
    rec_score: 0,
    card_no: 0,
    tot_cards: 0,
    easycolor: '',
    mediumcolor: '',
    hardcolor: '',
    incorrectcolor: '',
    };
  },
  methods: {
    update(res) {
      // eslint-disable-next-line
      console.log(res);
      this.question = res.data.c.question;
      this.answer = res.data.c.answer;
      this.score = res.data.c.score;
      this.rec_score = res.data.score;
      this.card_no = res.data.c_no;
      this.tot_cards = res.data.tot_cards;
      this.c_no = res.data.c.card_no;
      this.easycolor = '';
      this.mediumcolor = '';
      this.hardcolor = '';
      this.incorrectcolor = '';
    },
    getCard() {
      const path = `http://localhost:5000/${this.$route.params.username}/flashcard/${this.$route.params.title}/${this.card_no}`;
      axios.get(path)
        .then((res) => {
        this.update(res);
        })
        .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
        this.$router.push({ name: 'nocards', params: { username: this.$route.params.username } });
        });
    },
    next() {
      const path = `http://localhost:5000/${this.$route.params.username}/flashcard/${this.$route.params.title}/${this.card_no + 1}`;
      axios.get(path)
        .then((res) => {
        this.update(res);
        })
        .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
        this.$router.push( { name : 'gameover', params: { username: this.$route.params.username, score: this.rec_score, title: this.title } });
        });
    },
    retry() {
      const path = `http://localhost:5000/${this.$route.params.username}/flashcard/${this.$route.params.title}/0`;
      axios.get(path)
        .then((res) => {
        this.update(res);
        })
        .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
        this.$router.push({ name: 'nocards', params: { username: this.$route.params.username } });
        });
    },
    easy() {
      this.score = 10;
      this.rec_score += 10;
      this.postscore();
      this.easycolor = 'lightgreen';
    },
    medium() {
      this.score = 5;
      this.rec_score += 5;
      this.postscore();
      this.mediumcolor = 'yellow';
    },
    hard() {
      this.score = 3;
      this.rec_score += 3;
      this.postscore();
      this.hardcolor = 'orange';
    },
    incorrect() {
      this.score = 0;
      this.rec_score += 0;
      this.postscore();
      this.incorrectcolor = 'red';
    },
    postscore() {
      // eslint-disable-next-line
      console.log('in postscore');
      const path = `http://localhost:5000/${this.$route.params.username}/flashcard/${this.$route.params.title}/${this.card_no}`;
      const payload = {
        username: this.$route.params.username,
        title: this.$route.params.title,
        card_no: this.c_no,
        score: this.score,
        rec_score: this.rec_score,
      };
      axios.post(path, payload)
        .then((res) => {
        this.rec_score = res.data.rec_score;
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
