<template>
  <div class="lobby">
    <div><img src="../assets/logo.png" ></div>
    <div>    <input class="border" v-show="!submited" 
             v-model="playername" placeholder="Input your tag." >
    
            <div class="waves-effect waves-light btn center" v-show="!submited" 
            @click="submit_name">Join</div>
            <h3 v-show="submited">Welcome {{playername}}</h3>
                <h4 v-show="submited">Ready up.<br></h4><button class="waves-effect waves-light btn center" v-show="submited" 
     @click="Ready">{{is_ready?"Unready":"Ready"}} </button>
    </div>
    
    
    
    
    
    
    
    
    

     
    <PlayerList :Bool="this.PlayersReady" :Names="this.PlayersNames" :Text="['Ready','Unready']"/>
  </div>
</template>

<script>
import PlayerList from '@/components/PlayerList'
export default {
  name: 'EspionLobby',
  props: ['PlayersReady','PlayersNames','ws'],
  data () {
    return {
      submited:false,
      is_ready:false,
      playername : '',
    }
  },
    components: {
    PlayerList,
  },
  mounted() {
    console.log('Lobby UPDATED PlayersReady',this.PlayersReady)
  },
  methods: {
    submit_name(){
      //Check if Name empty or forbidden
      if (!this.playername.length  | this.playername == 'type'){
        console.log('Empty name.')
        return 1 ;
      }
      this.$parent.PlayerName=this.playername;     
      // Send it to the server
      this.ws.send(JSON.stringify({Name: this.playername}));
      this.submited = true;

    },
    Ready(){
      this.is_ready = !this.is_ready;
      this.ws.send(JSON.stringify({Ready: this.is_ready}));
      console.log("Lobby PlayerReady PROP:",this.PlayersReady)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.center{
  text-align: center;
}
.border{
  border-color:red;
}
.lobby{
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
