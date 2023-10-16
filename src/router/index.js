import Vue from 'vue';
import VueRouter from 'vue-router';
import login from '../views/login.vue';
import signup from '../views/signup.vue';
import dashboard from '../components/dashboard.vue';
import incpass from '../components/incpass.vue';
import userexists from '../components/userexists.vue';
import flashcards from '../components/flashcards.vue';
import create from '../components/create.vue';
import gameover from '../components/gameover.vue';
import nocards from '../components/nocards.vue';
import cardcreate from '../components/cardcreate.vue';
import edit from '../components/edit.vue';
import deckedit from '../components/deckedit.vue';
import deckeditcardcreate from '../components/deckeditcardcreate.vue';
import deckeditcardedit from '../components/deckeditcardedit.vue';
import dele from '../components/dele.vue';
import deckdone from '../components/deckdone.vue';
import titleexists from '../components/titleexists.vue';
import deckdonedel from '../components/deckdonedel.vue';
import exp from '../components/exp.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'login',
    component: login,
  },
  {
    path: '/signup',
    name: 'signup',
    component: signup,
  },
  {
    path: '/dashboard/:username',
    name: 'dashboard',
    component: dashboard,
  },
  {
    path: '/incpass',
    name: 'incpass',
    component: incpass,
  },
  {
    path: '/userexists',
    name: 'userexists',
    component: userexists,
  },
  {
    path: '/flashcards/:username/:title',
    name: 'flashcards',
    component: flashcards,
  },
  {
    path: '/create/:username',
    name: 'create',
    component: create,
  },
  {
    path: '/gameover/:username/:score/:title',
    name: 'gameover',
    component: gameover,
  },
  {
    path: '/nocards/:username',
    name: 'nocards',
    component: nocards,
  },
  {
    path: '/create/:username/:title/:no_cards',
    name: 'create_card',
    component: cardcreate,
  },
  {
    path: '/edit/:username',
    name: 'edit',
    component: edit,
  },
  {
    path: '/edit/:username/:title',
    name: 'deck_edit',
    component: deckedit,
  },
  {
    path: '/edit/:username/:title/create',
    name: 'deck_edit_card_create',
    component: deckeditcardcreate,
  },
  {
    path: '/edit/:username/:title/edit/:card_no',
    name: 'deck_edit_card_edit',
    component: deckeditcardedit,
  },
  {
    path: '/delete/:username',
    name: 'dele',
    component: dele,
  },
  {
    path: '/deckdone/:username',
    name: 'deckdone',
    component: deckdone,
  },
  {
    path: '/titleexists/:username',
    name: 'titleexists',
    component: titleexists,
  },
  {
    path: '/deckdonedel/:username',
    name: 'deckdonedel',
    component: deckdonedel,
  },
  {
    path: 'export/:username',
    name: 'export',
    component: exp,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
