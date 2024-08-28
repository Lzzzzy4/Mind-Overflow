<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'

</script>



<template>
   <div id="app"></div>
 <header>
   <!-- 导航栏 -->
  <div class="navi">
    <img src="@/assets/logo.jpg" alt="">
    <span class="title">AI助教</span>
    <span class="spacer"></span>
    
    <router-link to="/">AI答疑</router-link>
    <router-link to="/Register">注册</router-link>
    <router-link to="/Login">登录</router-link>
     <!-- <router-link to="/navigator">问答</router-link> -->
    <!-- <router-link to="/Editmd">md编辑</router-link> -->
    <router-view></router-view>

    
   
  </div>
</header>

</template>



<style>
/* 导入CSS文件 */
@import url('@/assets/css/conmmon.css');

</style>

