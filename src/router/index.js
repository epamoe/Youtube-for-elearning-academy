import {
	createRouter,
	createWebHistory
} from "vue-router"
import Dashboard from "../components/Dashboard.vue"
import Setting from "../components/Setting.vue"
import EditProfile from "../components/EditProfile.vue"
import Inscription from '../components/identification/Inscription.vue'
import Login from '../components/identification/Login.vue'
import MemberDashboard from "../components/MemberDashboard.vue"
import NotFound from "../components/NotFound.vue"
import Home from "../components/Home.vue"
import store from "../store/index"
import LandingPage from "../components/landingPage/LandingPage.vue"
import Trainings from "../components/trainings/Trainings.vue"

const routes = [{
		path: "/",
		name: 'Home',
		redirect: {
			name: 'LandingPage'
		},
		component: Home,
		children: [{
				path: "/dashboard",
				component: Dashboard,
				name: 'Dashboard'
			},
			{
				path: "/member-dashboard",
				component: MemberDashboard,
				meta: {
					requiresAuth: true
				},
				name: "MemberDashboard",
			},
			{
				path: "/edit-profile",
				component: EditProfile,
				meta: {
					requiresAuth: true
				},
				name: "EditProfile",
				props: true
			},
			{
				path: "/setting",
				component: Setting,
				meta: {
					requiresAuth: true
				},
				name: "Setting",
			}
		]
	},
	{
		path: "/register",
		name: "Register",
		meta: {
			isGuest: true
		},
		component: Inscription,
	},
	{
		path: "/login",
		name: "Login",
		meta: {
			isGuest: true
		},
		component: Login,
	},
	{
		path: '/:catchAll(.*)',
		name: 'NotFound',
		component: NotFound
	},
	{
		path: '/',
		name: 'LandingPage',
		component: LandingPage
	},
	{
		path: '/trainings',
		name: 'trainings',
		component: Trainings
	},

]


const router = createRouter({
	history: createWebHistory(),
	routes,
})

router.beforeEach((to, from, next) => {
	if (to.meta.requiresAuth && !store.state.user.token) {
		next({
			name: 'Login'
		})
	} else if (store.state.user.token && to.meta.isGuest) {
		next({
			name: 'MemberDashboard',
			params: {
				token: 'store.state.user.token'
			}
		})
	} else {
		next()
	}
})

export default router;