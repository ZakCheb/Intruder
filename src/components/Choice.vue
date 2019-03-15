


<script>
export default{
    props:['ws','PlayerName',"Selected","Decide"],
    methods:{
        SendDecide(d){
            this.Decide=d;
            console.log(this.PlayerName,this.Decide);
            this.ws.send(JSON.stringify({Decide: this.Decide}));
        }
    }, 
    data(){
            return{
                
                show:1,
            }

        },

}
    



</script>


<template>
<div class="choice" v-show="Selected.indexOf(PlayerName) != -1">
    Decide before last vote. <span @click="show = !show" v-show="!show">[SHOW]</span>
<span v-show="show" @click="show = !show">

<span class="success" v-bind:class="{borderG:this.Decide}" @click="SendDecide(1)">Success</span>
<span class="fail"    v-bind:class="{borderR:!this.Decide}" @click="SendDecide(0)">Failure</span>
    </span>
</div>
</template>

<style>
.borderR{
    border: 5px solid red;
}
.borderG{
    border: 5px solid green;
}
.choice{
    margin: 15px;
    font-size: 30px;
    text-align: center;
}
.success{
    background: black;
    color: green;
}
.fail{
    background:black;
    color: red;
}

</style>