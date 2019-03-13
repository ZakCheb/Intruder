<script>
import ShowFaction from './ShowFaction.vue'
import Vote from './Vote.vue' 
export default{
    props:['Names','Votes','ws','Faction',"Votes_Results"],
    components:{ShowFaction,Vote}
}

</script>

<template>

<div>
    Game
    <Vote :Names="Names" :Votes="Votes" :ws="ws" :Votes_Results="Votes_Results"/>
    <ShowFaction :Faction="Faction"/>
</div>
</template>