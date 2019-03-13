<template>
  <div id="app">
    <EspionLobby :PlayersReady="PlayersReady"/>
  </div>
</template>

<script>
import EspionLobby from '@/components/EspionLobby'
//<img src="./assets/logo.png">
export default {
  name: 'EspionMain',
    data () {
    return {
      websocket: new WebSocket("ws://127.0.0.1:8888"),
      Name:'',
      PlayersReady: 'INITIAL',
      PlayersNames:{},
    }
  },
  methods:{
  }
  ,
  created:function(){
      var ref = this;// keep the Vue instance scope inside the callback.
        this.websocket.onmessage = function (event) {
                let data = JSON.parse(event.data);                
                switch (data.type) {
                    case 'ready':
                        ref.PlayersReady=data.ready;
                        break;
                    case 'users':
                        ref.PlayersNames=data.names;
                        console.log('Users type',ref.PlayersNames)
                        break;
                    default:
                        console.error("unsupported event", data);
                }
    }
  },
  components:{EspionLobby}  
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
