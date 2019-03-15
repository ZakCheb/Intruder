<script>
import ShowFaction from './ShowFaction.vue'
import Vote from './Vote.vue' 
import GoToMission from './GoToMission.vue'
import Choice from './Choice.vue'
import Result from './Result.vue'
export default{
    props:['Names','Votes','ws','Faction',"Votes_Results","Turn","PlayerName","Selected","Decide","NUMBER_OF_PLAYER_IN_TEAM"],
    components:{Result,ShowFaction,Vote,GoToMission,Choice},
    data(){
        return{
            
            //Selected:[]
        }
    }
}

</script>

<template>

<div>
    <ShowFaction :PlayerName="PlayerName" :Faction="Faction"/>    
    <GoToMission :Selected="Selected" :PlayerName="PlayerName" :Names="Names" :ws="ws" :Turn="Turn" :NUMBER_OF_PLAYER_IN_TEAM="NUMBER_OF_PLAYER_IN_TEAM"/>
    
    <Vote :Names="Names" :Votes="Votes" :ws="ws" :Votes_Results="Votes_Results" />
    <Choice :PlayerName="PlayerName" :ws="ws" />
    <Result :Votes_Results="Votes_Results" />
</div>
</template>