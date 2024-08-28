<!-- src/views/Register.vue -->
<template>
  <div class="login-container">
    <div class="login-dialog">
      <h3>注册</h3>
      <div class="row">
        <span>用户名</span>
        <input type="text" v-model="username">
      </div>
      <div class="row">
        <span>学校邮箱</span>
        <input type="text" v-model="schoolEmail" @blur="validateSchoolEmail">
        <span v-if="!isSchoolEmailValid" class="error-message">请输入有效的学校邮箱地址</span>
      </div>
      <div class="row">
        <button @click="register">一键注册</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data() {
    return {
      username: '',
      schoolEmail: '',
      isSchoolEmailValid: true // 用于存储学校邮箱的验证状态
    };
  },
  methods: {
    register() {
      // 注册逻辑
      console.log('注册逻辑');
    },
    validateSchoolEmail() {
      const emailRegex = /^[0-9]{11}@stu.ecnu.edu.cn$/;
      if (!emailRegex.test(this.schoolEmail)) {
        this.isSchoolEmailValid = false;
      } else {
        this.isSchoolEmailValid = true;
      }
    }
  }
};
</script>

<style scoped>
/* 导入CSS文件 */
@import url('@/assets/css/conmmon.css');
@import url('@/assets/css/login.css');

/* 添加学校邮箱验证提示的样式 */
.error-message {
  color: red;
  margin-top: 5px;
}
</style>
