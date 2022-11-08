<template>
    <g>
        <path
            v-if="x1 && x2 && y1 && y2"
            style="stroke-width: 2; stroke: black"
            :d="coords"
        />
    </g>
</template>

<script>
export default {
    props: {
        weight: {
            type: Object,
            default: () => {},
        },
        nodes: {
            type: Array,
            default: () => [],
        },
    },
    data() {
        return {};
    },
    computed: {
        x1() {
            return this.nodes.find((node) => this.weight.k == node.id).x;
        },
        y1() {
            return this.nodes.find((node) => this.weight.k == node.id).y;
        },
        x2() {
            return this.nodes.find((node) => this.weight.j == node.id).x;
        },
        y2() {
            return this.nodes.find((node) => this.weight.j == node.id).y;
        },
        coords() {
            return `M ${this.x1} ${this.y1} L ${this.x2} ${this.y2}`;
        },
    },
};
</script>
