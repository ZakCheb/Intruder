

<script>
export default {
  // name:'PlayerList',
   props:['Bool','Names','Text','Selected'],
   
   data(){
     return{
       Is_Selected:[]
     }
   },
    updated() {    
     //console.log('PlayerList:',this.List)
   },
   methods:{
   }
}
</script>

<template>
  <div class="comp" > 
    PlayerList :
    
    <ul>
     <li v-for="Name in Names" :key="Name">
        <span  @click="$emit('NameClicked',Name)"> 
           {{ Name }}  
            <span v-show="Bool[Name] != undefined">
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

</style>