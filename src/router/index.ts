import { createRouter, createWebHistory } from 'vue-router'

import Register from '@/views/Register.vue';
import q_and_a from '@/views/q_and_a.vue';
import Login from '@/views/Login.vue';
// import Editmd from '@/views/Editmd.vue';
import navigator from '@/views/ainavigator.vue';

const routes = [
  {
    path: '/',
    name: 'q_and_a',
    component: q_and_a
  },

  {
    path: '/Register',
    name: 'Register',
    component: Register
  },

  {
    path: '/Login',
    name: 'Login',
    component: Login
  },

  // {
  //   path: '/Editmd',
  //   name: 'Editmd',
  //   component: Editmd
  // },
  // ... 其他路由

  {
    path: '/navigator',
    name: 'navigator',
    component: navigator
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'q_and_a',
      component: q_and_a
    },

    {
      path: '/Register',
      name: 'Register',
      component: Register
    },

    {
      path: '/Login',
      name: 'Login',
      component: Login
    },

    // {
    //   path: '/Editmd',
    //   name: 'Editmd',
    //   component: Editmd
    // },


    {
      path: '/navigator',
      name: 'navigator',
      component: navigator
    },

  ]
})

export default router
