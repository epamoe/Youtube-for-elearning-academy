import axios from "axios";
export default {
    name: "InputSearch",
    data() {
        return {
            toSearch: "",
        };
    },
    methods: {
        search() {
            axios
                .get(
                    this.$store.state.baseUrl + "landing/search/" + this.toSearch
                )
                .then((response) => {
                    console.log(response.data);
                    this.$emit('trainings',response.data)
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
};
