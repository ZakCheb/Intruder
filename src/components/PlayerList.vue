

<script>
export default {
  // name:'PlayerList',
   props:['players'],
   
   data(){
     return{
       count:0
     }
   },
   created:function() {
     console.log('PlayerList:',players)
   }
}
</script>

<template>
  <div> PlayerList  _:
     <li v-for="item in players">
          {{ item }}
    </li>
  </div>
</template>