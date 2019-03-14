<script>
import PlayerList from './PlayerList.vue'
export default{
    props:['Names','Votes','ws','Votes_Results'],
    components:{PlayerList},
    methods:{
        Voted(V){
            console.log({Vote: V})
            this.ws.send(JSON.stringify({Votes: V}));
        }
    },
}

</script>

<template>

<div style="background:#BBFFFF">
    VoteBox
    <PlayerList :Bool="Votes" :Names="Names" :Text="['Accepted','Refused']"/>
    <h2 v-show="Votes_Results != undefined">Vote {{Votes_Results.Yes>Votes_Results.No?"Accepted.":"Rejected."}}  </h2>
    <button @click="Voted(false)">Refuse</button><button @click="Voted(true)">Accept</button>
  </div>
</div>
</template>