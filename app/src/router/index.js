import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ServerConnection from '@/services/server-connection.service'

const serverConnection = new ServerConnection

const routes = [

  {
    path: '/',
    name: 'home',
    async beforeEnter( ){
      const tokenValid = await serverConnection.verifyToken()
      if(tokenValid==true)return({name:"dashboard"})
    },
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path:'/dashboard',
    name:'dashboard',
    async beforeEnter( ){
      const tokenValid = await serverConnection.verifyToken()
      if(tokenValid==false)return({name:"home"})
    },
    component: () => import('../views/user/dashboard.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
