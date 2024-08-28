<!-- src/views/LoginPage.vue -->
<template>
  <div class="login-container">
    <div class="login-dialog">
      <h3>登录</h3>
      <div class="row">
        <span>学校邮箱</span>
        <input type="text" v-model="schoolEmail" @blur="validateSchoolEmail" class="email-input">
        <span v-if="!isSchoolEmailValid" class="error-message">请输入有效的学校邮箱地址</span>
      </div>
      <div class="row">
        <span>验证码</span>
        <input type="text" v-model="verificationCode">
        <button @click="sendVerificationCode" :disabled="!isSchoolEmailValid || isSendingCode">发送验证码</button>
      </div>
      <div class="row">
        <button id="submit" @click="login">登录</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      schoolEmail: '',
      verificationCode: '',
      isSchoolEmailValid: true, // 用于存储学校邮箱的验证状态
      isSendingCode: false // 用于标识是否正在发送验证码
    };
  },
  methods: {
    login() {
      // 登录逻辑
      console.log('登录逻辑');
    },
    sendVerificationCode() {
      // 发送验证码逻辑
      this.isSendingCode = true;
      console.log('发送验证码到邮箱:', this.schoolEmail);
      // 模拟发送验证码的异步操作
      setTimeout(() => {
        this.isSendingCode = false;
      }, 3000); // 假设发送验证码需要3秒钟
    },
    validateSchoolEmail() {
      const emailRegex = /^[0-9]{11}@stu.ecnu.edu.cn$/;
      this.isSchoolEmailValid = emailRegex.test(this.schoolEmail);
    }
  }
};
</script>

/*schoolEmail和verificationCode数据属性,绑定学校邮箱和验证码的输入
validateSchoolEmail方法来验证邮箱地址是否符合给定的格式
sendVerificationCode方法来模拟发送验证码的过程
isSchoolEmailValid用于标识邮箱地址是否有效
isSendingCode用于防止用户在验证码发送过程中重复点击发送按钮 */

<style scoped>
/* 导入CSS文件 */
@import url('@/assets/css/conmmon.css');
@import url('@/assets/css/login.css');

</style>
