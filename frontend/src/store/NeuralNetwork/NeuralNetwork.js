import Axios from "axios";

export default {
    namespaced: true,
    state: {},
    mutations: {},
    actions: {
        async train({}, payload) {
            try {
                const result = await Axios.get(
                    "http://127.0.0.1:8000/api/NeuralNetwork/train",
                    {
                        params: {
                            trainingData: payload.trainingData,
                            layers: JSON.stringify(payload.layers),
                        },
                    }
                );
                return Promise.resolve(result);
            } catch (error) {
                console.log(error);
            }
        },
    },
    getters: {},
};
