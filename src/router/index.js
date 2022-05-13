import {
	createRouter,
	createWebHistory
} from "vue-router"
import Chat from "../components/layout/dashboard/children/Chat.vue"
import Links from "../components/layout/dashboard/children/Links.vue"
import Testimonies from "../components/layout/dashboard/children/Testimonies.vue"
import Presentation from "../components/layout/dashboard/children/Presentation.vue"
import Overview from "../components/layout/user-dashboard/children/Overview.vue"
import Posts from "../components/layout/user-dashboard/children/Posts.vue"
import Syllabus from "../components/layout/user-dashboard/children/Syllabus.vue"
import Events from "../components/layout/user-dashboard/children/Events.vue"
import More from "../components/layout/user-dashboard/children/More.vue"
import Dashboard from "../components/Dashboard.vue"
import Register from "../components/Register.vue"
import Login from "../components/Login.vue"
import UserDashboard from "../components/UserDashboard.vue"
import Home from "../components/Home.vue"
import store from "../store/index"


const routes = [{
		path: "/",
		name: 'Home',
		component: Home,
		children: [{
				path: "/dashboard",
				component: Dashboard,
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
				path: "/user-dashboard",
				component: UserDashboard,
				name: "UserDashboard",
				children: [{
						path: "/dashboard/overview",
						name: "Overview",
						component: Overview,
					},
					{
						path: "/user-dashboard/posts",
						name: "Posts",
						component: Posts,
					},
					{
						path: "/user-dashboard/syllabus",
						name: "Syllabus",
						component: Syllabus,
					},
					{
						path: "/user-dashboard/events",
						name: "Events",
						component: Events,
					},
					{
						path: "/user-dashboard/more",
						name: "More",
						component: More,
					},
				]
			},
		]
	},
	{
		path: "/register",
		name: "Register",
		component: Register,
	},
	{
		path: "/login",
		name: "Login",
		component: Login,
	}

]


const router = createRouter({
	history: createWebHistory(),
	routes,
})

export default router;