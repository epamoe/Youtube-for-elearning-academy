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
import Inscription from '../components/identification/Inscription.vue'
import Login from '../components/identification/Login.vue'
import MemberDashboard from "../components/MemberDashboard.vue"
import NotFound from "../components/NotFound.vue"
import Home from "../components/Home.vue"
import store from "../store/index"

const routes = [{
		path: "/",
		name: 'Home',
		component: Home,
		children: [{
				path: "/dashboard",
				component: Dashboard,
				meta: {requiresAuth: true},
				name: "Dashboard",
				children: [{
						path: "/dashboard/presentation",
						name: "Presentation",
						component: Presentation,
					},
					{
						path: "/dashboard/testimonies",
						name: "Testimonies",
						component: Testimonies,
					},
					{
						path: "/dashboard/links",
						name: "Links",
						component: Links,
					},
					{
						path: "/dashboard/chat",
						name: "Chat",
						component: Chat,
					},
				]
			},
			{
				path: "/member-dashboard",
				component: MemberDashboard,
				meta: {requiresAuth: true},
				name: "MemberDashboard",
				children: [{
						path: "/member-dashboard",
						name: "Overview",
						component: Overview,
					},
					{
						path: "/member-dashboard/followed-syllabus",
						name: "FollowedSyllabus",
						component: FollowedSyllabus,
					},
					{
						path: "/member-dashboard/syllabus",
						name: "Syllabus",
						component: Syllabus,
					},
					{
						path: "/member-dashboard/new-syllabus",
						name: "NewSyllabus",
						component: NewSyllabus,
					},
				]
			},
		]
	},
	{
		path: "/register",
		name: "Register",
		meta: {isGuest: true},
		component: Inscription,
	},
	{
		path: "/login",
		name: "Login",
		meta: {isGuest: true},
		component: Login,
	},
	{
		path: '/:catchAll(.*)',
		name: 'NotFound',
		component: NotFound
	},
	

]


const router = createRouter({
	history: createWebHistory(),
	routes,
})

router.beforeEach((to, from, next) => {
	if(to.meta.requiresAuth && !store.state.user.token){
		next({name: 'Login'})
	} else if(store.state.user.token && to.meta.isGuest){
		next({name: 'Dashboard'})
	} else{
		next()
	}
})

export default router;