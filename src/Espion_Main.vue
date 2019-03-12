<template>
  <div id="app">
    
    <Espion_Lobby :Players_Ready="Players_Ready"/>
  </div>
</template>

<script>
import Espion_Lobby from '@/components/Espion_Lobby'
//<img src="./assets/logo.png">
//import PlayerList from
export default {
  name: 'Espion_Main',
    data () {
    return {
      websocket: new WebSocket("ws://127.0.0.1:8888/"),
      Name:'',
      Players_Ready:{},
      Players_Names:{},
    }
  },
  created:function(){
        this.websocket.onmessage = function (event) {
                //console.log(event)
                let data = JSON.parse(event.data);
                //console.log(data);
                switch (data.type) {
                    case 'ready':
                        this.Players_Ready=data.ready
                        console.log("Ready type",data.ready)
                        break;
                    case 'users':
                        this.Players_Names=data.names
                        console.log('Users type',this.Players_Names)
                        break;
                    default:
                        console.error("unsupported event", data);
                }
    }
  },
  components:{Espion_Lobby}  
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
