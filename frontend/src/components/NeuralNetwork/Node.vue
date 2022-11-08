<template>
    <g>
        <circle v-if="node.x && node.y" :cx="node.x" :cy="node.y" r="15" />
    </g>
</template>

<script>
export default {
    data() {
        return {
            x: null,
            y: null,
        };
    },
    props: {
        boxWidth: {
            type: Number,
            default: null,
        },
        boxHeight: {
            type: Number,
            default: null,
        },
        layers: {
            type: Array,
            default: () => [],
        },
        nodes: {
            type: Array,
            default: () => [],
        },
        node: {
            type: Object,
            defaultr: () => {},
        },
        index: {
            type: Number,
            default: null,
        },
    },
    computed: {
        layerLength() {
            return this.layers.length;
        },
    },
    mounted() {
        //console.log(this.node);
        const layerWidth = (this.boxWidth - 30) / this.layerLength;
        for (let i = 0; i < this.layerLength; i++) {
            if (this.layers[i].id === this.node.layerID) {
                this.node.x = layerWidth * i + layerWidth / 2;
                console.log(this.node.x);
            }
        }
        const layerHeight = this.boxHeight - 100;
        const arr = this.nodes.filter(
            (node) => node.layerID == this.node.layerID
        );
        if (arr.length == 1) {
            this.node.y = layerHeight / 4;
        } else {
            const yCoords = arr.map((node) => {
                return node.y;
            });
            this.node.y = Math.max(...yCoords) + 80;
        }
    },
    watch: {
        layerLength() {
            const layerWidth = (this.boxWidth - 30) / this.layerLength;
            for (let i = 0; i < this.layerLength; i++) {
                if (this.layers[i].id === this.node.layerID) {
                    this.node.x = layerWidth * i + layerWidth / 2;
                }
            }
        },
    },
};
</script>
