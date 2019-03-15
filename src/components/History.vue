
<script>
export default {
    props:['History']
,
data(){
    return{
        
    }
}
}
</script>

<template>
    <div>
         History:
<ul class="collection">
    <li v-for="R in History" class="collection-item">
        {{R.Turn}} => Crew: <span  v-for="S in R.Selected"> {{S}} </span> {{R.Yes>R.No?'':"Not accepted"}}   <span style="text-align:right;color:green;"> {{R.Success}}</span> <span style="text-align:right;color:red;">{{R.Failure}}</span>

    </li>
</ul>

    </div>
</template>