import axios from "axios";
import {
    createStore
} from "vuex"
import axiosClient from "../axios/axios";
import qs from 'qs'


const store = createStore({
    state: {
        user: {
            data: {
                login:'',
                email: '',
                image_path:'',
                listTrainingFollow: [],
                trainingList: [],
            },
            token: '1'//sessionStorage.getItem('TOKEN'),
        },
    },
    getters: {
        getUser: (state) => state.user,
    },
    actions: {
        async register({
            commit
        }, user) {
            const response = await axiosClient.post('/register', user)
                .then(function (response) {
                    console.log(response);
                    return response;
                })
                .catch(function (error) {
                    console.log(error);
                });
        },
        async login({
            commit
        }, user) {
            const response = await axios({
                    method: 'post',
                    url: 'https://youtubedev-api.herokuapp.com/login',
                    data: qs.stringify(user),
                    headers: {'content-type': 'application/x-www-form-urlencoded;charset=utf-8'}
                })
                .then(function (response) {
                    console.log(response);
                    return response
                })
                .catch(function (error) {
                    console.log(error);
                });
            commit('setUserToken', response.data)
        },
        logOut({commit}){
            commit('logout')
        }
    },
    mutations: {
        logout: (state) => {
            state.user.data = {}
            state.user.token = null
            sessionStorage.clear()
            console.log(state.user)
        },
        setUserToken: (state, userData) => {
            state.user.token = userData.token
            sessionStorage.setItem('TOKEN', userData.token)
        },
    },
    modules: {},
})

export default store;