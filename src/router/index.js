import {
	createRouter,
	createWebHistory
} from "vue-router"
import Chat from "../components/layout/dashboard/children/Chat.vue"
import Links from "../components/layout/dashboard/children/Links.vue"
import Testimonies from "../components/layout/dashboard/children/Testimonies.vue"
import Presentation from "../components/layout/dashboard/children/Presentation.vue"
import Overview from "../components/layout/member-dashboard/children/Overview.vue"
import Posts from "../components/layout/member-dashboard/children/Posts.vue"
import Syllabus from "../components/layout/member-dashboard/children/Syllabus.vue"
import Events from "../components/layout/member-dashboard/children/Events.vue"
import More from "../components/layout/member-dashboard/children/More.vue"
import Dashboard from "../components/Dashboard.vue"
import Register from "../components/Register.vue"
import Login from "../components/Login.vue"
import Auth from "../components/Auth.vue"
import MemberDashboard from "../components/MemberDashboard.vue"
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
						path: "/member-dashboard/posts",
						name: "Posts",
						component: Posts,
					},
					{
						path: "/member-dashboard/syllabus",
						name: "Syllabus",
						component: Syllabus,
					},
					{
						path: "/member-dashboard/events",
						name: "Events",
						component: Events,
					},
					{
						path: "/member-dashboard/more",
						name: "More",
						component: More,
					},
				]
			},
		]
	},
	{
		path: "/auth",
		redirect: "/login",
		name: "Auth",
		component: Auth,
		meta: {isGuest: true},
		children: [
			{
				path: "/register",
				name: "Register",
				component: Register,
			},
			{
				path: "/login",
				name: "Login",
				component: Login,
			},
		]
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