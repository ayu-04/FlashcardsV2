<template>
<div class="nocards">
<br/>
<h1 align="center">This deck has no cards</h1>
<br/>
<router-link class="button"
:to="{name: 'dashboard', params: {username: $route.params.username } }">
Go to dashboard
</router-link>
</div>
</template>

<style>
.nocards{height: 300px;
background-color:AntiqueWhite ;
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
