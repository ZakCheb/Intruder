

<script>
export default {
  // name:'PlayerList',
   props:['Bool','Names','Text'],
   
   data(){
     return{
       count:0
     }
   },
    created() {    
     console.log('PlayerList:',this.List)
   }
}
</script>

<template>
  <div> PlayerList :
     <li v-for="Name in Names">
          {{ Name }}   <span v-show="Bool[Name] != undefined">{{Bool[Name]?Text[0]:Text[1]}}</span>
    </li>
  </div>
</template>