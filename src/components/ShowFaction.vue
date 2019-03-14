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
<div class="faction" @click="show=!show" >{{PlayerName}} =>
    <span v-show="show" >
        {{Faction?"Révolutionaire":"Espion"}}
        </span> 
</div>
</template>
<style>
.faction{
    border: 1px dotted black;
}
</style>