import Vue from 'vue'
import Router from 'vue-router'
import Espion_Lobby from '@/components/Espion_Lobby'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Espion_Lobby',
      component: Espion_Lobby
    }
  ]
})
