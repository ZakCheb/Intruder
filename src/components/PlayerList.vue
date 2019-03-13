

<script>
export default {
  // name:'PlayerList',
   props:['List'],
   
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
     <li v-for="item in List">
          {{ item }} => 
    </li>
  </div>
</template>