<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h3 v-show="submited">Welcome {{playername}}</h3>
    <input v-show="!submited" v-model="playername" placeholder="Input your tag.">
    <button v-show="!submited" @click="submit_name">Join</button>
    <button v-show="submited"  @click="Ready"> Ready</button>
     <PlayerList :players="Players_Ready"/>
  </div>
</template>

<script>
import PlayerList from '@/components/PlayerList'
export default {
  name: 'Espion_Lobby',
  props: ['Players_Ready'],
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
      console.log(this.$parent);
      this.submited = true;
      //router.replace(  
    },
    Ready(){
      this.is_ready = !this.is_ready;
      this.$parent.websocket.send(JSON.stringify({Ready: this.is_ready}));
      console.log("Parernt>",this.$parent.Players_Ready)
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
