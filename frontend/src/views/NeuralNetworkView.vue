<template>
    <v-container>
        <v-row class="mb-16">
            <v-app-bar>
                <v-app-bar-title>Mind Box</v-app-bar-title>
            </v-app-bar>
        </v-row>
        <v-row class="mt-16">
            <v-col cols="4">
                <v-card height="800" width="500" outlined elevation="10">
                    <v-card-title>Neural Network Menu</v-card-title>
                    <v-row>
                        <v-spacer />
                        <v-col cols="4">
                            <p>Add Layer</p>
                            <v-btn fab large @click="addLayer">
                                <v-icon>mdi-plus-circle-outline</v-icon>
                            </v-btn>
                        </v-col>
                        <v-col cols="4">
                            <input type="file" ref="file" @change="addFile" />
                            <v-btn fab large @click="submitFile">
                                Submit
                            </v-btn>
                        </v-col>
                        <v-spacer />
                    </v-row>
                </v-card>
            </v-col>
            <v-col cols="6">
                <v-card
                    :width="boxWidth"
                    :height="boxHeight"
                    outlined
                    elevation="10"
                    id="box"
                >
                    <v-card-title>Sand Box</v-card-title>
                    <NeuralNetworkMain
                        :nodes="nodes"
                        :layers="layers"
                        :weights="weights"
                        :boxWidth="boxWidth"
                        :boxHeight="boxHeight"
                        :layerID="layerID"
                        @add-node="addNode"
                        @remove-layer="removeLayer"
                    />
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
// @ is an alias to /src

import NeuralNetworkMain from "../components/NeuralNetwork/NeuralNetworkMain";
import { mapActions, mapGetters, mapMutations } from "vuex";
export default {
    name: "NeuralNetworkView",
    components: {
        NeuralNetworkMain,
    },
    data() {
        return {
            nodes: [],
            layers: [],
            layerID: 0,
            nodeID: 0,
            blob: null,
            trainingData: null,
        };
    },
    methods: {
        ...mapActions({
            trainNetwork: "NeuralNetwork/train",
        }),
        addFile() {
            this.file = this.$refs.file.files[0];
        },
        async submitFile() {
            let rows = [];
            const reader = new FileReader();
            reader.readAsText(this.file);
            reader.onload = (e) => {
                this.trainingData = e.target.result;
                this.trainNetwork({
                    trainingData: this.trainingData,
                    layers: this.layers,
                }).then((res) => {
                    console.log(res);
                });
            };
        },
        addNode(layerID) {
            //adding nodes, x and y defaulted to null because its defaulted in Node.vue
            this.nodes.push({
                layerID,
                x: null,
                y: null,
                id: this.nodeID,
            });
            this.layers.find((layer) => layer.id == layerID).nodesLength += 1;
            this.nodeID += 1;
        },
        addLayer() {
            this.layers.push({
                type: "Hidden Layer",
                id: this.layerID,
                nodesLength: 0,
            });
            this.layerID += 1;
        },
        removeLayer(id) {
            for (let i = this.layers.length - 1; i >= 0; i--) {
                if (this.layers[i].id == id) {
                    this.layers.splice(i, 1);
                    for (let j = this.nodes.length - 1; j >= 0; j--) {
                        if (this.nodes[j].layerID == id) {
                            this.nodes.splice(j, 1);
                        }
                    }
                }
            }
        },
    },
    computed: {
        boxWidth() {
            return 1000;
        },
        boxHeight() {
            return 800;
        },
        weights() {
            let arr = [];
            if (this.layers.length > 1) {
                for (let i = 0; i < this.layers.length - 1; i++) {
                    const layer1 = this.nodes.filter(
                        (node) => node.layerID == this.layers[i].id
                    );
                    const layer2 = this.nodes.filter(
                        (node) => node.layerID == this.layers[i + 1].id
                    );
                    layer1.forEach((node1) => {
                        layer2.forEach((node2) => {
                            arr.push({
                                k: node1.id,
                                j: node2.id,
                            });
                        });
                    });
                }
            }
            return arr;
        },
    },
};
</script>
