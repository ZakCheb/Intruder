<script>
import ShowFaction from './ShowFaction.vue'
import Vote from './Vote.vue' 
import GoToMission from './GoToMission.vue'
export default{
    props:['Names','Votes','ws','Faction',"Votes_Results","Turn","PlayerName","Selected"],
    components:{ShowFaction,Vote,GoToMission},
    data(){
        return{
            NUMBER_OF_PLAYER_IN_TEAM:2,
            //Selected:[]
        }
    }
}

</script>

<template>

<div>
    Game
    <ShowFaction :PlayerName="PlayerName" :Faction="Faction"/>    
    <GoToMission :Selected="Selected" :PlayerName="PlayerName" :Names="Names" :ws="ws" :Turn="Turn" :NUMBER_OF_PLAYER_IN_TEAM="NUMBER_OF_PLAYER_IN_TEAM"/>
    <Vote :Names="Names" :Votes="Votes" :ws="ws" :Votes_Results="Votes_Results" />
</div>
</template>