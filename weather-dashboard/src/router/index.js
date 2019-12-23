import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Find from '../views/Find.vue'

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
  }
]

const router = new VueRouter({
  routes
})

export default router