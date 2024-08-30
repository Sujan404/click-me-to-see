import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PostView from "../views/main/Post.vue";
import CategoryView from "@/views/main/Category.vue";
import TagView from "@/views/main/Tag.vue";
import AllCategoriesView from "@/views/main/AllCategories.vue";
import AllTagsView from "@/views/main/AllTags.vue";
import SignInView from "@/views/user/SignIn.vue";
import SignUpView from "@/views/user/SignUp.vue";
import ProfileView from "@/views/user/Profile.vue";
import UserView from "@/views/user/User.vue";
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
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
