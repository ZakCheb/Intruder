

<script>
import PlayerList from './PlayerList.vue'
export default {
  
   props:['ws','Turn','Names','Selected','PlayerName','NUMBER_OF_PLAYER_IN_TEAM'],
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
           if( this.Turn  != this.PlayerName){
               return ;
           }
            if (this.Selected.indexOf(Player) == -1){ // if the player is not selected yet
                if(this.Selected.length < this.NUMBER_OF_PLAYER_IN_TEAM ) {
                    console.log('Selected ',Player);
                    
                    this.Selected.push(Player);
                    
                    
                    this.ws.send(JSON.stringify({Selected: this.Selected}));
                    
                }
            }
            else{
                this.Selected.pop(Player)
                console.log('Unselected ',Player);
                this.ws.send(JSON.stringify({Selected: this.Selected}));
            }
            console.log('SelectGoMission ',Player);
            }
   }
}
</script>

<template>
    
  <div class="MissionBox">  
   
      <h5>{{Turn}} select {{NUMBER_OF_PLAYER_IN_TEAM}} mission crew</h5>
           Mission Crew: <span v-for="crew in Selected" > {{crew}} </span>
    <ul class="collection">
       <li v-for="Name in Names" :key="Name" class="collection-item"  v-bind:class="{active:Selected.indexOf(Name) > -1}"
        @click="SelectedToGoMission(Name)">
        <span  > 
           {{ Name }}  
        </span>
        </li>
    </ul>

  
  </div>
</template>

<style>
.MissionBox{
   border: 5px solid rgb(4, 1, 182);
   border-radius: 3px;
}
</style>