<template>
    <g>
        <circle 
            :cx="x"
            :cy="y"
            r="15"
            />
    </g>
</template>

<script>


export default {
    data(){
        return{

        }
    },
    props:{
        x:{
            type:Number,
            default:null
        },
        y:{
            type:Number,
            default:null
        }
    }
}
</script>
