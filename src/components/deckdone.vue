<template>
<div class="deckdone">
<br/>
<h1 align="center">Your deck has been created</h1>
<br/>
<router-link class="button"
:to="{name: 'dashboard', params:{ username: $route.params.username } }">
Go to dashboard
</router-link>
</div>
</template>

<style>
.deckdone{height:400px;
background-color:Plum ;
font-size:larger;
border-radius: 100px;
margin: 100px;
border-style: hidden;
padding:10px;}
.button{text-decoration:none;
color:Black;
padding:30px;
border-style:solid;
border-color:Lavender;
border-radius: 25px;
background-color:Lavender}
</style>
