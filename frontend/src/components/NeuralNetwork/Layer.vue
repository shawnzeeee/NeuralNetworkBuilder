<template>
    <g>
        <text :x="index * width + width / 2 - 20" :y="20">Remove Layer</text>
        <rect
            width="50"
            height="50"
            style="fill: rgb(255, 0, 0); stroke-width: 0"
            :x="index * width + width / 2"
            :y="30"
            @click="$emit('remove-layer', id)"
        />
        <text :x="index * width + width / 4 - 10" :y="120">Add Node</text>
        <rect
            width="50"
            height="50"
            style="fill: rgb(0, 255, 0); stroke-width: 0"
            :x="index * width + width / 4"
            :y="130"
            @click="$emit('add-node', id)"
        />
        <polygon
            :points="getPolygonArea"
            style="fill: none; stroke-width: 2; stroke: black"
        />
    </g>
</template>

<script>
export default {
    data() {
        return {};
    },
    props: {
        index: {
            type: Number,
            default: null,
        },
        layerLength: {
            type: Number,
            default: null,
        },
        boxWidth: {
            type: Number,
            default: null,
        },
        boxHeight: {
            type: Number,
            default: null,
        },
        id: {
            type: Number,
            default: null,
        },
    },
    computed: {
        width() {
            return (this.boxWidth - 30) / this.layerLength;
        },
        height() {
            return this.boxHeight - 200;
        },
        getPolygonArea() {
            const originX = this.index * this.width + 10;
            const originY = 100;
            return `${originX} ${originY} ${originX + this.width} ${originY} ${
                originX + this.width
            } ${originY + this.height} ${originX} ${originY + this.height}`;
        },
    },
};
</script>
