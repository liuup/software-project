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
  // TODO: 用户登录后的界面，还需要增加用户提交数据的表单
  // TODO: 用户注册的组件
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
