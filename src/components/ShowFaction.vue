<script>
export default{
    props:['Faction','PlayerName'],
    data(){
        return{
            show:true
        }
    }
}

</script>

<template>
<div class="col s1" >
<div class="faction" @click="show=!show" >{{PlayerName}}
    <span v-show="show" >
        {{Faction?" => Révolutionaire  (Click to Hide)":" => Espion  (Click to Hide)"}}
        </span> 
</div>
</div>
</template>
<style>
.faction{
    border: 2px dotted black;
    border-radius: 10px;
    border-style:dashed;
    text-align :center;
    font-size: 18px;
}

</style>