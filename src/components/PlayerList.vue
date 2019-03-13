

<script>
export default {
  // name:'PlayerList',
   props:['Bool','Names'],
   
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
          {{ Name }}  is {{Bool[Name]?"Ready":"Unready"}}
    </li>
  </div>
</template>