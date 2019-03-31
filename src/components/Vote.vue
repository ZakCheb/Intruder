<script>

import PlayerList from './PlayerList.vue'
export default{
    props:['Names','Votes','ws','Votes_Results',
    'NUMBER_OF_PLAYER_IN_TEAM','Timer'],
    components:{PlayerList},
    methods:{
        Voted(V){
            console.log({Vote: V})
            this.ws.send(JSON.stringify({Votes: V}));
            
        }
        
    },
    data(){
        return{
            
          
        }

    },
    
 
}

</script>

<template>

<div class="" >
    <h5> Vote if you accept the mission crew.</h5>
    <PlayerList  :Selected="Selected" :Bool="Votes" :Names="Names" :Text="['Accepted','Refused']"/>
    <h2 v-show="Votes_Results.Y != undefined">Vote {{Votes_Results.Yes>Votes_Results.No?"Accepted.":"Rejected."}}  </h2>
    <div class="waves-effect waves-light btn" @click="Voted(false)">Refuse</div>
    <div class="waves-effect waves-light btn" @click="Voted(true)">Accept</div>
  {{Timer}}
</div>
</template>

<style>
.votebox{
   border: 5px solid rgb(11, 206, 5);
   border-radius: 3px;
   
}

</style>