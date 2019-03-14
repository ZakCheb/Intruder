

<script>
import PlayerList from './PlayerList.vue'
export default {
  
   props:['Turn','Names','Selected','PlayerName'],
   components:{
       PlayerList
   },
   data(){
     return{
       Is_Selected:[]
     }
   },
    updated() {    
  
   },
   methods:{  
       SelectedToGoMission:function(Player){
            if (this.Selected.indexOf(Player) == -1){ // if the player is not selected yet
                if(this.Selected.length < this.NUMBER_OF_PLAYER_IN_TEAM ) {
                    this.Selected.push(Player)
                }
            }
            else{
                this.Selected.pop(Player)
            }
            console.log('SelectGoMission ',Player);
            }
   }
}
</script>

<template>
    
  <div class="MissionBox">  
    
      <h3>{{Turn}} choosing who go to Mission</h3>
            <PlayerList :Names="Names" :Bool="[1,1,1]" v-on:NameClicked="SelectedToGoMission" :Text="['Accepted','Refused']"/>
  
  </div>
</template>

<style>
.MissionBox{
   border: 5px solid rgb(4, 1, 182);
   border-radius: 3px;
}
</style>