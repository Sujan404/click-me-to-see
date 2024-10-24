import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/App.vue'
import PostView from "../views/main/Post.vue";
import CategoryView from "@/views/main/Category.vue";
import TagView from "@/views/main/Tag.vue";
import AllCategoriesView from "@/views/main/AllCategories.vue";
import AllTagsView from "@/views/main/AllTags.vue";
import SignInView from "@/views/user/SignIn.vue";
import SignUpView from "@/views/user/SignUp.vue";
import ProfileView from "@/views/user/Profile.vue";
import UserView from "@/views/user/User.vue";
import BastionHost from "@/views/home/blogs/2024/BastionHost.vue"
import Docker from "@/views/home/blogs/2024/Docker.vue"
import NavBar from "@/views/home/Navigation.vue"
import AboutMe from "@/views/home/AboutMe.vue"
import Footer from "@/views/home/Footer.vue"
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      components: {
        default: NavBar,
        a: AboutMe,
        b:Footer
      }
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: "/category/:category",
      name: "Category",
      component: CategoryView,
    },
    {
      path: "/tag",
      name: "Tag",
      component: TagView,
    },
    {
      path: "/categories",
      name: "Categories",
      component: AllCategoriesView,
    },
    {
      path: "/tags",
      name: "Tags",
      component: AllTagsView,
    },
    {
      path: "/signin",
      name: "SignIn",
      component: SignInView,
    },
    {
      path: "/signup",
      name: "SignUp",
      component: SignUpView,
    },
    {
      path: "/user",
      name: "User",
      component: UserView,
      meta:{
        requiresAuth: true
      },
      children:[
        {
          path: "/user/profile",
          name: "Profile",
          component: ProfileView,
        },
        {
          path: "/user/post",
          name: "Post",
          component: PostView,
        },
      ]
    },
    {
      path:"/2024/bastion-host-architecture",
      name:"BastionHost",
      component: BastionHost,
    },
    {
      path:"/2024/docker",
      name:"Docker",
      component: Docker,
    }
  ]
})

router.beforeEach(async(to, from, next) => {
  if (to.meta.requiresAuth) {
    const token = localStorage.getItem('token');
    if (token) {
      // User is authenticated, proceed to the route
      next();
    } else {
      // User is not authenticated, redirect to login
      // next('signin');
    }
  } else {
    // Non-protected route, allow access
    next();
  }
  // if(to.meta.requiresAuth && !isAuthenticated){
  //   // return {
  //   //   path: '/login',
  //   //   // save the location we were at to come back later
  //   //   query: { redirect: to.fullPath },
  //   // }
  // }
})
export default router
