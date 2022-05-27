import axios from "axios";
import {
    createStore
} from "vuex"
import axiosClient from "../axios/axios";
import qs from 'qs'


const store = createStore({
    state: {
        stats: [
          {
            color: 'orange',
            per: 2,
            title: 'SYLLABUS FOLLOW '
          },
          {
            color: 'green',
            per: 1,
            title: 'VIDEOS COMMENT'
          },
          {
            color: 'blue',
            per: 3,
            title: 'VIDEOS SHARED'
          },
          {
            color: 'red',
            per: 4,
            title: 'VIDEOS LIKED'
          },
        ],
        user: {
            data: {
                login:'ChristAfroTech',
                email: 'tchiaguiachristophe25@gmail.com',
                image_path:'/images/bg-member.png',
                image_path_profile:'/images/member.png',
                description: 'orem ipsum dolor sit amet consectetur adipisicing elit. Dicta harum magni ducimus rerum dolorem, laborum nam amet, molestiae alias ullam quae iste? Dolore excepturi ullam deleniti sunt expedita, voluptas recusandae?',
                listTrainingFollow: [],
                trainingList: [],
            },
            token: '1'//sessionStorage.getItem('TOKEN'),
        },
        training: {
            comments: [
                {
                    id: '1',
                    content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dicta harum magni ducimus rerum dolorem, laborum nam amet, molestiae alias ullam quae iste? Dolore excepturi ullam deleniti sunt expedita, voluptas recusandae? ',
                    by: 'Fai'
                },
                {
                    id: '2',
                    content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dicta harum magni ducimus rerum dolorem, laborum nam amet, molestiae alias ullam quae iste? Dolore excepturi ullam deleniti sunt expedita, voluptas recusandae? ',
                    by: 'Fai'
                },
                {
                    id: '3',
                    content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dicta harum magni ducimus rerum dolorem, laborum nam amet, molestiae alias ullam quae iste? Dolore excepturi ullam deleniti sunt expedita, voluptas recusandae? ',
                    by: 'Fai'
                },
                {
                    id: '4',
                    content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dicta harum magni ducimus rerum dolorem, laborum nam amet, molestiae alias ullam quae iste? Dolore excepturi ullam deleniti sunt expedita, voluptas recusandae? ',
                    by: 'Fai'
                },
                {
                    id: '5',
                    content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dicta harum magni ducimus rerum dolorem, laborum nam amet, molestiae alias ullam quae iste? Dolore excepturi ullam deleniti sunt expedita, voluptas recusandae? ',
                    by: 'Fai'
                },
                {
                    id: '6',
                    content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dicta harum magni ducimus rerum dolorem, laborum nam amet, molestiae alias ullam quae iste? Dolore excepturi ullam deleniti sunt expedita, voluptas recusandae? ',
                    by: 'Fai'
                },
            ],
            description: 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Commodi autem quos, adipisci exercitationem deserunt totam vitae tempore culpa. Beatae quibusdam impedit maiores porro natus optio dolor sit placeat, qui vitae? ',
            chapiters: [
                {
                    title: 'Introduction',
                    lessons: [
                        {
                            title: "on Ubunt",
                            videos: [
                                {
                                    id:'1',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'2',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'3',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'4',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'5',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },
                            ]
                        },{
                            title: "on Ubuntu",
                            videos: [
                                {
                                    id:'1',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'2',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'3',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'4',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'5',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },
                            ]
                        },{
                            title: "on Ubuntu",
                            videos: [
                                {
                                    id:'1',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'2',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'3',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'4',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'5',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },
                            ]
                        },{
                            title: "on Ubuntu",
                            videos: [
                                {
                                    id:'1',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'2',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'3',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'4',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'5',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },
                            ]
                        },
                    ]
                },
                {
                    title: 'Introduction',
                    lessons: [
                        {
                            title: "on Ubuntu",
                            videos: [
                                {
                                    id:'1',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'2',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'3',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'4',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'5',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },
                            ]
                        },{
                            title: "on Ubuntu",
                            videos: [
                                {
                                    id:'1',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'2',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'3',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'4',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'5',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },
                            ]
                        },{
                            title: "on Ubuntu",
                            videos: [
                                {
                                    id:'1',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'2',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'3',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'4',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'5',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },
                            ]
                        },{
                            title: "on Ubuntu",
                            videos: [
                                {
                                    id:'1',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'2',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'3',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'4',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'5',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },
                            ]
                        },
                    ]
                },
                {
                    title: 'Introduction',
                    lessons: [
                        {
                            title: "on Ubuntu",
                            videos: [
                                {
                                    id:'1',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'2',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'3',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'4',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'5',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },
                            ]
                        },{
                            title: "on Ubuntu",
                            videos: [
                                {
                                    id:'1',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'2',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'3',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'4',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'5',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },
                            ]
                        },{
                            title: "on Ubuntu",
                            videos: [
                                {
                                    id:'1',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'2',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'3',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'4',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'5',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },
                            ]
                        },{
                            title: "on Ubuntu",
                            videos: [
                                {
                                    id:'1',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'2',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'3',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'4',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'5',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },
                            ]
                        },
                    ]
                },
                {
                    title: 'Introduction',
                    lessons: [
                        {
                            title: "on Ubuntu",
                            videos: [
                                {
                                    id:'1',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'2',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'3',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'4',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'5',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },
                            ]
                        },{
                            title: "on Ubuntu",
                            videos: [
                                {
                                    id:'1',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'2',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'3',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'4',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'5',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },
                            ]
                        },{
                            title: "on Ubuntu",
                            videos: [
                                {
                                    id:'1',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'2',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'3',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'4',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'5',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },
                            ]
                        },{
                            title: "on Ubuntu",
                            videos: [
                                {
                                    id:'1',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'2',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'3',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'4',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },{
                                    id:'5',
                                    videoID: 'xCnrI6IdsrI',
                                    link: `https://www.youtube.com/embed/xCnrI6IdsrI`
                                },
                            ]
                        },
                    ]
                },
            ]
        }
    },
    getters: {
        getUser: (state) => state.user,
        getTraining: (state) => state.training,
        getStats: (state) => state.stats
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
                    headers: {
                        Accept:'*/*',
                        'content-type': 'application/x-www-form-urlencoded;charset=utf-8'
                    }
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