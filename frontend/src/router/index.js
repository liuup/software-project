import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'User',
    component: () => import('../views/User.vue')
  },
  {
    path: '/guard',
    name: 'Guard',
    component: () => import('../views/Guard.vue')
  },
  {
    path: "/guard/admin",
    name: "GuardAdmin",
    component: () => import("../views/GuardAdmin.vue")
  },
  {
    path: "/user/admin",
    name: "UserAdmin",
    component: () => import("../views/UserAdmin.vue")
  },
  {
    path: "/user/register",
    name: "UserRegister",
    component: () => import("../views/UserRegister.vue")
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
