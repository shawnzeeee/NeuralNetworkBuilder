import { createStore } from "vuex";
import NeuralNetwork from "./NeuralNetwork/NeuralNetwork";
//test
export default createStore({
    modules: {
        NeuralNetwork,
    },
});
