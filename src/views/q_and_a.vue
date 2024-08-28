<!-- src/views/q_and_a.vue -->
<template>
    <div class="q_and_a">

     <title>AI助教 - 对话窗口</title>
 
      <div class="sidebar-content" :class="{ show: isSidebarOpen }">
        <CollapsibleSidebar :records="historyRecords" />
      </div>
     
        <span v-if="isSidebarOpen"></span>
        <span v-else></span>

    
  
  </div>

  <!-- 对话窗口 -->
  <div id="app">
    <div class="chat-container">
      <h1 class="custom-title">AI_Navigator</h1>

      <div class="chat-window">
        <div v-for="message in messages" :key="message.id"
            :class="{'chat-message': true, 'user-message': message.sender === 'user', 'ai-message': message.sender === 'ai'}">
          {{ message.text }}
        </div>
      </div>

      <div class="input-container">
        <input type="text" v-model="userInput" placeholder="请输入内容..." @keydown.enter="sendMessage" />
        <button @click="sendMessage">发送</button>
      </div>
    </div>
  </div>

</template>



<script>

import CollapsibleSidebar from '@/components/CollapsibleSidebar.vue';
import { ref, onMounted } from 'vue';
import axios from 'axios';





export default {
  components: {
    CollapsibleSidebar
  },
  setup() {
    // 使用Vue 3的Composition API中的ref函数创建响应式数据
     const isSidebarOpen = ref(true);
    const historyRecords = ref([]);

    const userInput = ref('');
    const messages = ref([]);
    const apiUrl = ref('https://api.qwen2.model/ask');



 // 模拟获取历史记录
    const fetchHistoryRecords = async () => {
      // 这里应该是一个API调用，获取历史记录
      // 以下为模拟数据
      historyRecords.value = [
        // ...历史记录数据...
      ];
    };

    onMounted(() => {
      fetchHistoryRecords();
    });

    const toggleSidebar = () => {
      isSidebarOpen.value = !isSidebarOpen.value;
    };

    // ...其他响应式数据和定义的方法...





    // 定义一个方法来发送消息
    const sendMessage = () => {
      if (userInput.value.trim() === '') return;

      messages.value.push({ id: Date.now(), text: userInput.value, sender: 'user' });

      getAiResponse(userInput.value);

      userInput.value = '';
    };



    // 定义一个方法来获取AI回复
    const getAiResponse = async (userMessage) => {
      try {
        const response = await fetch(apiUrl.value, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ message: userMessage })
        });
        const data = await response.json();

        messages.value.push({ id: Date.now(), text: data.reply, sender: 'ai' });
      } catch (error) {
        console.error('获取AI助教回复时出错:', error);
      }
    };




    // 返回响应式数据和定义的方法
    return {

       isSidebarOpen,
      historyRecords,
      toggleSidebar,

      userInput,
      messages,
      sendMessage,
      getAiResponse
    };
  }
};
</script>


<style>
/* 导入CSS文件 */
@import url('@/assets/css/conmmon.css');
@import url('@/assets/css/q_and_a.css');

</style>
