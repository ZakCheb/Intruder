<script>

import PlayerList from './PlayerList.vue'
export default{
    props:['Names','Votes','ws','Votes_Results',
    'NUMBER_OF_PLAYER_IN_TEAM',"Selected"],
    components:{PlayerList},
    methods:{
        Voted(V){        
            let count=0;
            for (let i in this.Votes){
                count = count +1;
                
            }
            console.log("Countring votes",count,this.Votes,this.Names.length)
            
            if (count+1  == this.Names.length){ //if the last one voted
                this.ActiveTimer = true
                this.RecursiveTimer(V)
                
                
            }
            else{
                console.log({Vote: V})
                this.ws.send(JSON.stringify({Votes: V}));
            
            }
            ////////////////

        },

        RecursiveTimer(V){
            setTimeout(()=>{
                this.Timer=this.Timer-1;
                if(this.Timer >= 0){
                    this.RecursiveTimer(V)

                }
                else{
                    console.log("Last Vote",{Vote: V})
                    this.ws.send(JSON.stringify({Votes: V}));
                    this.Timer =5;
                    this.ActiveTimer =false;
                }
            },1000);
        }
        
    },
    data(){
        return{
            ActiveTimer:false,
            Timer:5
          
        }

    },
    
 
}

</script>

<template>

<div class="votebox" >
    
    <h5> Vote if you accept the mission crew.</h5>
    <PlayerList  :Selected="Selected" :Bool="Votes" :Names="Names" :Text="['Accepted','Refused']"/>
    <h2 v-show="Votes_Results.Y != undefined">Vote {{Votes_Results.Yes>Votes_Results.No?"Accepted.":"Rejected."}}  </h2>
    <div class="waves-effect waves-light btn" @click="Voted(false)">Refuse</div>
    <div class="waves-effect waves-light btn" @click="Voted(true)">Accept</div>
    <span v-show="ActiveTimer">Its time to choose {{Timer}}sec.</span>
  
</div>
</template>

<style>
.votebox{
   border: 5px solid rgb(11, 206, 5);
   border-radius: 3px;
   
}

</style>