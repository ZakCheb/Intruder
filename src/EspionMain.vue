<template>
  <div id="app">
    <Header/>
    <EspionLobby v-show="!gamestarted"  :ws="websocket"   :PlayersReady="PlayersReady" :PlayersNames="PlayersNames"/>
    <EspionInGame :Selected="Selected" :PlayerName="PlayerName" :Turn="Turn" v-show="gamestarted" :ws="websocket" :Faction="Faction"  :Names="PlayersNames" :Votes="Votes" :Votes_Results="Votes_Results"  :NUMBER_OF_PLAYER_IN_TEAM="NUMBER_OF_PLAYER_IN_TEAM"/>
    <Footer/>
  </div>
</template>

<script>
import EspionLobby from '@/components/EspionLobby'
import EspionInGame from '@/components/EspionInGame'
import Header from '@/components/Header'
import Footer from '@/components/Footer'
//<img src="./assets/logo.png">
export default {
  name: 'EspionMain',
    data () {
    return {
      websocket: new WebSocket("ws://127.0.0.1:8888"),
      gamestarted:false,

      PlayerName:'', // current player
      //Lobby
      PlayersReady: {}, // players if ready
      PlayersNames:{}, // names of the players
      //Votes
      Votes:{},
      Votes_Results:{},
      //GoToMission
      NUMBER_OF_PLAYER_IN_TEAM:2,
      Turn:"", // wich person who select team
      Faction:'',  //Faction of the player Revolu1/Spy0
      Selected:[],
      //Choice
      Decide:'' // Fail0/Success1

      
    }
  },
  methods:{
  }
  ,
  created:function(){ //When page loaded
      var ref = this;// keep the Vue instance scope inside the callback.
        this.websocket.onmessage = function (event) { // on receiving message from server
                let data = JSON.parse(event.data);                
                console.log('UI RECEIVE:',data)
                switch (data.type) {
                    case 'ready':
                        ref.PlayersReady=data.ready;
                        console.log('Ready type',ref.PlayersReady)
                        break;
                    case 'names':
                        ref.PlayersNames=data.names;
                        console.log('Users type',ref.PlayersNames)
                        break;
                    case 'faction':
                        ref.Faction=data.faction;
                        setTimeout(()=>{
                            ref.gamestarted=true;
                        },1000);
                        
                        console.log("Faction type",ref.Faction)
                        break;
                    case 'votes':
                        ref.Votes=data.votes;
                        console.log('Votes type',ref.Votes)
                        break;
                    case 'vote_result':
                        ref.Votes_Results=data.vote_result;
                        console.log('Votes type',ref.Votes_Results)
                        ref.Votes={};
                        break;
                    case 'turn':
                        ref.Turn=data.turn;
                        console.log('Turn type',ref.turn)
                    break;
                    case 'selected':
                        ref.Selected=data.selected;
                        console.log('Selected type',ref.Selected)
                    break;
                    default:
                        console.error("unsupported event", data);
                }
    }
  },
  components:{Header,Footer,EspionLobby,EspionInGame}  
}
</script>

<style>
/* http://meyerweb.com/eric/tools/css/reset/ 
   v2.0 | 20110126
   License: none (public domain)
*/

html, body, div, span, applet, object, iframe,
 p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed, 
figure, figcaption, footer, header, hgroup, 
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure, 
footer, header, hgroup, menu, nav, section {
	display: block;
}
body {
	line-height: 1;
}
ol, ul {
	list-style: none;
}
blockquote, q {
	quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
	content: '';
	content: none;
}
table {
	border-collapse: collapse;
	border-spacing: 0;
}


#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

}
/* RESET */

</style>
