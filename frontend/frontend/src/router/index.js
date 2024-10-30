import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/App.vue'
import PostView from '../views/main/Post.vue'
import CategoryView from '@/views/main/Category.vue'
import TagView from '@/views/main/Tag.vue'
import AllCategoriesView from '@/views/main/AllCategories.vue'
import AllTagsView from '@/views/main/AllTags.vue'
import SignInView from '@/views/user/SignIn.vue'
import SignUpView from '@/views/user/SignUp.vue'
import ProfileView from '@/views/user/Profile.vue'
import UserView from '@/views/user/User.vue'
import BastionHost from '@/views/home/blogs/2024/BastionHost.vue'
import Docker from '@/views/home/blogs/2024/Docker.vue'
import HotReloadVueContainer from '@/views/home/blogs/2024/HotReloadVueContainer.vue'
import CssFlex from '@/views/home/blogs/2024/CSSFlex.vue'
import NavBar from '@/views/home/Navigation.vue'
import AboutMe from '@/views/home/AboutMe.vue'
import Footer from '@/views/home/Footer.vue'
import BlogsCollection from '@/views/home/BlogsCollection.vue'
import { userUserStore } from '@/stores/user'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      components: {
        default: NavBar,
        a: AboutMe,
        b: Footer
      },
      meta: {
        title: 'Home Page - Example App',
        metaTags: [
          {
            name: 'description',
            content: 'The home page of our example app.'
          },
          {
            property: 'og:description',
            content: 'The home page of our example app.'
          }
        ]
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
      path: '/category/:category',
      name: 'Category',
      component: CategoryView
    },
    {
      path: '/tag',
      name: 'Tag',
      component: TagView
    },
    {
      path: '/categories',
      name: 'Categories',
      component: AllCategoriesView
    },
    {
      path: '/tags',
      name: 'Tags',
      component: AllTagsView
    },
    {
      path: '/signin',
      name: 'SignIn',
      component: SignInView
    },
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUpView
    },
    {
      path: '/user',
      name: 'User',
      component: UserView,
      meta: {
        requiresAuth: true
      },
      children: [
        {
          path: '/user/profile',
          name: 'Profile',
          component: ProfileView
        },
        {
          path: '/user/post',
          name: 'Post',
          component: PostView
        }
      ]
    },
    {
      path: '/blogs-collection',
      name: 'BlogsCollection',
      component: BlogsCollection
    },
    {
      path: '/2024/bastion-host-architecture',
      name: 'BastionHost',
      component: BastionHost
    },
    {
      path: '/2024/docker',
      name: 'Docker',
      component: Docker
    },
    {
      path: '/2024/hot-reload-vue-with-vite-in-docker-container',
      name: 'HotReloadVueContainer',
      component: HotReloadVueContainer
    },
    {
      path: '/2024/css-flex',
      name: 'CssFlex',
      component: CssFlex
    }
  ]
})

router.beforeEach(async (to, from, next) => {
  const userStore = userUserStore()
  const token = localStorage.getItem('token')
  const isLoggedIn = userStore.getUser
  console.log('askdjfgajshdfgjahsdf')
  console.log(to.name)
  // Check if the user is already signed in and tries to access the /signin route
  if (to.path === '/signin' && isLoggedIn && token) {
    return next({ path: '/user' })
  }

  // Check if route requires authentication
  if (to.meta.requiresAuth) {
    if (isLoggedIn && token) {
      // User is authenticated, allow access
      next()
    } else {
      // User not authenticated, redirect to sign-in
      next({
        path: '/signin',
        query: { redirect: to.fullPath } // Save the intended path to redirect back after sign-in
      })
    }
  } else {
    console.log('i am neither redirectiing nor logged in')
    // Non-protected route, allow access
    next()
  }
})
export default router
