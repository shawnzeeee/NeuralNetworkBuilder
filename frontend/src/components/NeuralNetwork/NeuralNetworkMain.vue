<template>
    <svg
        viewBox="0 0 1000 800"
        id="box2"
        @mousedown="mouseHold=true"
        @mouseup="()=>{
            mouseHold = false
            selectedNode = null
        }"
    >
        <Node
            v-for="(node, i) in nodes"
            @mousedown="()=>{
                selectedNode = i
            }"
            :key="i"
            :x="node.x"
            :y="node.y"
        />
    </svg>

</template>

<script>
import Node from './Node'
export default {
    components:{
        Node
    },
    props:{
        nodes:{
            type: Array,
            default: ()=>[]
        }
    },
    data(){
        return{
            mouseHold:false,
            selectedNode: null
        }
    },
    computed:{
        boxCoords(){
            const box =  document.getElementById("box");
            const boxPos = box.getBoundingClientRect();
            return {x: boxPos.x, y: boxPos.y}
        },
    },
    methods:{
        updateMouseCoor(event){
            const x = event.clientX - this.boxCoords.x;
            const y = event.clientY - this.boxCoords.y
            if(this.mouseHold && this.selectedNode != null){
                this.nodes[this.selectedNode].x = x
                this.nodes[this.selectedNode].y = y-50
            }
        }
    },
    created(){
        window.onload=()=>{
            const box =  document.getElementById("box");  
            box.addEventListener("mousemove", this.updateMouseCoor, false);
            console.log(this.boxCoords)
        }    
    },
}
</script>
