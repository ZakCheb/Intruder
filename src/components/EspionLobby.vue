<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h3 v-show="submited">Welcome {{playername}}</h3>
    <input v-show="!submited" v-model="playername" placeholder="Input your tag.">
    <button v-show="!submited" @click="submit_name">Join</button>
    <button v-show="submited"  @click="Ready"> Ready</button>
     <PlayerList :List="this.PlayersReady"/>
  </div>
</template>

<script>
import PlayerList from '@/components/PlayerList'
export default {
  name: 'EspionLobby',
  props: ['PlayersReady'],
  data () {
    return {
      submited:false,
      is_ready:false,
      msg: 'Spy game.',
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
      this.$parent.Name=this.playername;     
      // Send it to the server
      this.$parent.websocket.send(JSON.stringify({Name: this.playername}));
      this.submited = true;

    },
    Ready(){
      this.is_ready = !this.is_ready;
      this.$parent.websocket.send(JSON.stringify({Ready: this.is_ready}));
      console.log("Lobby PlayerReady PROP:",this.PlayersReady)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
