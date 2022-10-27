<template>
  <v-container>
    <v-row class="mb-16">
    <v-app-bar>
      <v-app-bar-title>Mind Box</v-app-bar-title>
    </v-app-bar>
  </v-row>
  <v-row class="mt-16">
    <v-col cols="4">
    <v-card
      height="800"
      width="500"
      outlined
      elevation="10"
      >
      <v-card-title>Neural Network Menu</v-card-title>
      <v-btn
        fab
        large
        @click="addNode"
        >
        <v-icon>mdi-plus-circle-outline</v-icon>
      </v-btn>
    </v-card>
    </v-col>
    <v-col cols="6">
      <v-card 
        width="1000"
        height="800"
        outlined
        elevation="10"
        id="box"
      >
        <v-card-title>Sand Box</v-card-title>
        <NeuralNetworkMain
          :nodes="nodes"
        />
      </v-card>
    </v-col>
  </v-row>
  </v-container>
</template>

<script>
// @ is an alias to /src

import NeuralNetworkMain from '../components/NeuralNetwork/NeuralNetworkMain'

export default {
  name: 'NeuralNetworkView',
  components: {
    NeuralNetworkMain
  },
  data(){
    return{
      nodes:[],
      id:0,
    }
  },
  methods:{
    addNode(){
      this.id += 1
      this.nodes.push({
        x:10,
        y:10,
        id:this.id
      })
    }
  },
}
</script>
