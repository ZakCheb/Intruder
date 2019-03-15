

<script>
export default {
  // name:'PlayerList',
   props:['Bool','Names','Text','Selected'],
   
}
</script>

<template>

  <div class="comp" v-show="Names.length != 0"> 
    PlayerList :

    <ul class="collection">
     <li v-for="Name in Names" :key="Name" class="collection-item" v-bind:class="{active:Bool[Name]}">
        <span  @click="$emit('NameClicked',Name)"> 
           {{ Name }}  
            <span v-show="Bool[Name] != undefined" class="right" >
              {{Bool[Name]?Text[0]:Text[1]}}</span></span>
      </li>
    </ul>
  </div>
</template>

<style>
.comp{
   border: 2px solid red;
   border-radius: 3px;
}
.green{
  color: #11EE11;
}
.right {
  text-align: right;
}
</style>