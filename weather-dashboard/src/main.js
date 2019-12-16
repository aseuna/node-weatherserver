import Vue from 'vue'
import App from './App.vue'

import ECharts from 'vue-echarts'

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import PortalVue from 'portal-vue'

Vue.component('v-chart', ECharts)

Vue.use(PortalVue)
Vue.use(BootstrapVue)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
