import { createRouter, createWebHistory } from 'vue-router'
// import Home from '../views/User.vue'

const routes = [
  {
    path: '/',
    name: 'User',
    component: () => import('../views/User.vue')
  },
  {
    path: '/guard',
    name: 'Guard',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Guard.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
