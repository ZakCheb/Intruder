<script>
import ShowFaction from './ShowFaction.vue'
import Vote from './Vote.vue' 
import GoToMission from './GoToMission.vue'
import Choice from './Choice.vue'
import Result from './Result.vue'
import HistoryView from './History.vue'
export default{


    props:['Names','Votes','ws','Faction',"Votes_Results","Turn",
    'History',"PlayerName","Selected","Decide","NUMBER_OF_PLAYER_IN_TEAM"],


    components:{Result,ShowFaction,Vote,GoToMission,Choice,HistoryView},

    data(){
        return{
            
            Decide:1,
        }
    }

}

</script>

<template>

<div class="" >

    <ShowFaction  :PlayerName="PlayerName" :Faction="Faction"/>  
    
    <Choice :PlayerName="PlayerName" :ws="ws" :Selected="Selected" :Decide="Decide"/>  
    
    <GoToMission  :Selected="Selected" :PlayerName="PlayerName" :Names="Names"
     :ws="ws" :Turn="Turn" :NUMBER_OF_PLAYER_IN_TEAM="NUMBER_OF_PLAYER_IN_TEAM"/>
    
    <Vote :Names="Names" :Votes="Votes" :ws="ws" :Votes_Results="Votes_Results"  />
    <Choice :PlayerName="PlayerName" :ws="ws" :Selected="Selected"  :Decide="Decide"/>  
    <Result :Votes_Results="Votes_Results" />
    <HistoryView :History="History"/>
</div>
</template>