import {
	createRouter,
	createWebHistory
} from "vue-router"
import Chat from "../components/layout/dashboard/children/Chat.vue"
import Links from "../components/layout/dashboard/children/Links.vue"
import Testimonies from "../components/layout/dashboard/children/Testimonies.vue"
import Presentation from "../components/layout/dashboard/children/Presentation.vue"
import Overview from "../components/layout/member-dashboard/children/Overview.vue"
import FollowedSyllabus from "../components/layout/member-dashboard/children/FollowedSyllabus.vue"
import Syllabus from "../components/layout/member-dashboard/children/Syllabus.vue"
import NewSyllabus from "../components/layout/member-dashboard/children/NewSyllabus.vue"
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

const routes = [{
		path: "/",
		name: 'Home',
		redirect: {
			name: 'LandingPage'
		},
		component: Home,
		children: [{
				path: "/dashboard/:token/:id",
				component: Dashboard,
				name: 'Dashboard'
			},
			{
				path: "/member-dashboard/:token",
				component: MemberDashboard,
				meta: {
					requiresAuth: true
				},
				name: "MemberDashboard",
			},
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
		path: "/edit-profile/:token",
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
			name: 'Dashboard'
		})
	} else {
		next()
	}
})

export default router;