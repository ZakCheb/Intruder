


<script>
export default{
    props:['ws','PlayerName'],
    methods:{
        SendDecide(d){
            this.Decide=d;
            console.log(this.PlayerName,this.Decide);
            this.ws.send(JSON.stringify({Decide: this.Decide}));
        }
    }, 
    data(){
            return{Decide:1}
        }
    

}

</script>


<template>
<div class="choice">
<span class="success" v-bind:class="{border:this.Decide}" @click="SendDecide(1)">Success</span>
<span class="fail"    v-bind:class="{border:!this.Decide}" @click="SendDecide(0)">Failure</span>
    </div>
</template>

<style>
.border{
    border: 5px solid green;
}
.choice{
    margin: 15px;
    font-size: 15px;
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