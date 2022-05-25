import axios from "axios"
import store from '../store/index'


const axiosClient = axios.create({
    baseURL: 'https://youtubedev-api.herokuapp.com',
    headers: { 'content-type': 'application/json' },
});

axiosClient.interceptors.request.use(config => {
    config.headers.Authorization = `Bearer ${store.state.user.token}`;
    return config;
})

export default axiosClient;