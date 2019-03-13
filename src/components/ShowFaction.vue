<script>
export default{
    props:['Faction'],
    data(){
        return{
            show:true
        }
    }
}

</script>

<template>
<span @click="show=!show" >My Faction :<span v-show="show" >{{Faction?"Révolutionaire":"Espion"}}</span> </span>
</template>