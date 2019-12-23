import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Find from '../views/Find.vue'
import About from '../views/About.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
      path: '/find',
      name: 'find',
      component: Find
  },
  {
      path: '/about',
      name: 'about',
      component: About
  }
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router