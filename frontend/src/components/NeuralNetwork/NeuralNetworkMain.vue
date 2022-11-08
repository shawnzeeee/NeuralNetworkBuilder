<template>
    <svg
        :viewBox="viewBox"
        id="box2"
        @mousedown="mouseHold = true"
        @mouseup="
            () => {
                mouseHold = false;
                selectedNode = null;
            }
        "
    >
        <Layer
            v-for="(layer, i) in layers"
            :key="i"
            :index="i"
            :layerLength="layers.length"
            :boxWidth="boxWidth"
            :boxHeight="boxHeight"
            :id="layer.id"
            @add-node="
                (e) => {
                    $emit('add-node', e);
                }
            "
            @remove-layer="
                (e) => {
                    $emit('remove-layer', e);
                }
            "
        />
        <Node
            v-for="(node, i) in nodes"
            @mousedown="
                () => {
                    selectedNode = i;
                }
            "
            :key="i"
            :layers="layers"
            :node="node"
            :boxWidth="boxWidth"
            :boxHeight="boxHeight"
            :nodes="nodes"
            :index="i"
        />
        <Weights
            v-for="(weight, i) in weights"
            :key="i"
            :layers="layers"
            :nodes="nodes"
            :weight="weight"
            :index="i"
        />
    </svg>
</template>

<script>
import Node from "./Node";
import Layer from "./Layer";
import Weights from "./Weights";
export default {
    components: {
        Node,
        Layer,
        Weights,
    },
    props: {
        nodes: {
            type: Array,
            default: () => [],
        },
        layers: {
            type: Array,
            default: () => [],
        },
        weights: {
            type: Array,
            default: () => [],
        },
        boxWidth: {
            type: Number,
            default: null,
        },
        boxHeight: {
            type: Number,
            default: null,
        },
    },
    data() {
        return {
            mouseHold: false,
            selectedNode: null,
        };
    },
    computed: {
        boxCoords() {
            const box = document.getElementById("box");
            const boxPos = box.getBoundingClientRect();
            return { x: boxPos.x, y: boxPos.y };
        },
        viewBox() {
            return `0 0 ${this.boxWidth} ${this.boxHeight}`;
        },
    },
    methods: {
        updateMouseCoor(event) {
            const x = event.clientX - this.boxCoords.x;
            const y = event.clientY - this.boxCoords.y;
            if (this.mouseHold && this.selectedNode != null) {
                this.nodes[this.selectedNode].x = x;
                this.nodes[this.selectedNode].y = y - 50;
            }
        },
    },
    created() {
        window.onload = () => {
            const box = document.getElementById("box");
            box.addEventListener("mousemove", this.updateMouseCoor, false);
        };
    },
};
</script>
