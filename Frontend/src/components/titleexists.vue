<template>
<div class="titleexists">
<br/>

<h1 align="center">This title already exists, please choose a different title</h1>
<br/>
<div class="parent">
<router-link class="button"
style="border-color:LightPink;background-color:LightPink"
:to="{name: 'create', params:{ username: $route.params.username } }">
Go back
</router-link>
<br/>
<router-link class="button"
:to="{name: 'dashboard', params:{ username: $route.params.username } }">
Go to dashboard
</router-link>
</div>
</div>
</template>

<style>
.parent{
    display:flex;
    flex-direction:row;
    justify-content:space-around;
    padding:0px 10rem;
}
.titleexists{height:500px;
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
