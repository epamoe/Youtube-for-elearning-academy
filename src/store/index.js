import axios from "axios";
import {
    createStore
} from "vuex"
import axiosClient from "../axios/axios";
import { useRouter } from "vue-router";

const router = useRouter()

const store = createStore({
    state: {
        user: {
            profile: {
                login:'ChristAfroTech',
                email: 'tchiaguiachristophe25@gmail.com',
                image_path:'/images/bg-member.png',
                profile_image:'/images/member.png',
                experiences: []
                //description: 'orem ipsum dolor sit amet consectetur adipisicing elit. Dicta harum magni ducimus rerum dolorem, laborum nam amet, molestiae alias ullam quae iste? Dolore excepturi ullam deleniti sunt expedita, voluptas recusandae?',
                //listTrainingFollow: [],
                //trainingList: [],
            },
            token: sessionStorage.getItem('TOKEN'),
            userType: sessionStorage.getItem('USERTYPE'),
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
        },
        baseUrl: 'https://youtube-dev-production.herokuapp.com/',
        displayCheckEmail: false
    },
    getters: {
        getUser: (state) => state.user,
        getTraining: (state) => state.training,
    },
    actions: {
        async register({commit}, user) {
            const response = await axiosClient.post('/register', user)
                .then(function (response) {
                    console.log(response);
                    router.push({name: "Login"})
                    return response;
                })
                .catch(function (error) {
                    console.log(error);
                });
        },
        async login({commit}, user) {
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
                    commit('setUser', response.data)
                })
                .catch(function (error) {
                    console.log(error);
                    return error
                });
        },
        logOut({commit}){
            commit('logout')
        },
        async getProfile({commit}){
            const response = await axiosClient.get('/dashboard/profile')
                    .then(function(res){
                        commit('setUserProfile', res.data)
                        console.log(res.data)
                    })
                    .catch(function(err){
                        console.log(err);
                        return err
                    })
            
        },
        async getProfileUser({commit}, login){
            const response = await axiosClient.get(`/dashboard/profile/${login}`)
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },
        async getUserTraining({commit}){
            const response = await axiosClient.get('/dashboard/profile/trainings')
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },
        async updateProfileLogin({commit}, login){
            const response = await axiosClient.put('/dashboard/profile/login')
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },
        async updateProfileLogin({commit}, login){
            const response = await axiosClient.put('/dashboard/profile/login', login)
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },
        async updateProfileEmail({commit}, email){
            const response = await axiosClient.put('/dashboard/profile/email', email)
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },
        async updateProfilePassword({commit}, NewPass){
            const response = await axiosClient.put('/dashboard/profile/password', NewPass)
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },
        async updateProfilePassword({commit}, image_path){
            const response = await axiosClient.put('/dashboard/profile/profile_image', image_path)
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },
        async getNotifications({commit}){
            const response = await axiosClient.get('/dashboard/notifications')
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },
        async getFollowedTraining({commit}, uuid){
            const response = await axiosClient.get(`/dashboard/user/training/follow/${uuid}`)
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },
        async becomeMember({commit}){
            const response = await axiosClient.get('/dashboard/expert/apply')
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },
        //  Expert Actions
        async getExpertTraining({commit}, login){
            const response = await axiosClient.get(`/dashboard/expert/trainings/${login}`)
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },
        async createTraining({commit}, training){
            const response = await axiosClient.post('/dashboard/expert/training/create', training)
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },
        async createChapiter({commit}, chapiter){
            const response = await axiosClient.post('/dashboard/expert/training/chapter/create/', chapiter)
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },
        async createLesson({commit}, lesson){
            const response = await axiosClient.post('/dashboard/expert/training/chapter/lesson/create/', lesson)
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },
        async updateTraining({commit}, training){
            const response = await axiosClient.put('/dashboard/expert/training', training)
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },
        async updateChapiter({commit}, chapiter){
            const response = await axiosClient.put('/dashboard/expert/training/chapter', chapiter)
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },
        async updateLesson({commit}, lesson){
            const response = await axiosClient.put('/dashboard/expert/training/chapter/lesson', lesson)
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },
        async updateTraining({commit}, idTraining){
            const response = await axiosClient.delete(`/dashboard/expert/training/${idTraining}`, training)
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },
        async deleteChapiter({commit}, idChapiter){
            const response = await axiosClient.delete(`/dashboard/expert/training/chapter/${idChapiter}`)
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },
        async updateLesson({commit}, idLesson){
            const response = await axiosClient.delete(`/dashboard/expert/training/chapter/lesson/${idLesson}`, lesson)
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },

        //Admin Actions
        
        async updateLesson({commit}, idLesson){
            const response = await axiosClient.delete(`/dashboard/expert/training/chapter/lesson/${idLesson}`, lesson)
                    .then((res) => {
                        console.log(res.data)
                        return res.data
                    })
                    .catch((err) => {
                        console.log(err)
                        return err
                    })
        },


    },
    mutations: {
        logout: (state) => {
            state.user.data = {}
            state.user.token = null
            state.user.userType = null
            sessionStorage.clear()
            console.log(state.user)
        },
        setUser: (state, userData) => {
            state.user.token = userData.access_token
            state.user.userType = userData.user_type
            sessionStorage.setItem('TOKEN', userData.access_token)
            sessionStorage.setItem('USERTYPE', userData.user_type)
            console.log(userData.access_token, userData.user_type)
        },
        setUserProfile: (state, profile) => {
            state.user.profile.login = profile.login
            state.user.profile.email = profile.email
            state.user.profile.profile_image = profile.profile_image
            state.user.profile.experiences = profile.experiences
        },
        cDisplayCheckmail (state,playload) {
            state.displayCheckEmail = playload
        }
    },
    modules: {},
})

export default store;