<script>

import PlayerList from './PlayerList.vue'
export default{
    props:['Names','Votes','ws','Votes_Results','NUMBER_OF_PLAYER_IN_TEAM'],
    components:{PlayerList},
    methods:{
        Voted(V){
            console.log({Vote: V})
            this.ws.send(JSON.stringify({Votes: V}));
        }
        
    },
    data(){
        return{
            Selected:[]
        }

    }

}

</script>

<template>

<div class="votebox" >
    <h3> Vote if you accept the mission crew.</h3>
    <PlayerList  :Selected="Selected" :Bool="Votes" :Names="Names" :Text="['Accepted','Refused']"/>
    <h2 v-show="Votes_Results != undefined">Vote {{Votes_Results.Yes>Votes_Results.No?"Accepted.":"Rejected."}}  </h2>
    <button @click="Voted(false)">Refuse</button><button @click="Voted(true)">Accept</button>
  
</div>
</template>

<style>
.votebox{
   border: 5px solid rgb(11, 206, 5);
   border-radius: 3px;
   
}

</style>