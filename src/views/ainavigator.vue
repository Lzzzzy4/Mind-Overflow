<template>
  <div class="container chat-container mt-5">
    <h1 class="text-center">AINavigator</h1>
    <div id="chat-box" class="d-flex flex-column chat-box"></div>
    <div class="form-group d-flex">
      <input type="text" class="form-control mr-2" id="query" placeholder="输入你的问题"
        onkeydown="handleKeyDown(event)" @keydown.enter="askQuestion">
      <button class="btn btn-primary" @click="askQuestion">提问</button>
    </div>
    <div id="loader" class="loader"></div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';

export default {
  setup() {
    const query = ref('');
    const loader = ref(null);
    const chatBox = ref(null);

    function askQuestion() {
      if (!query.value.trim()) return;

      const questionBubble = createBubble(query.value, 'question');
      chatBox.value.appendChild(questionBubble);
      chatBox.value.scrollTop = chatBox.value.scrollHeight;

      query.value = '';

      loader.value.style.display = 'block';

      fetch('http://localhost:5174/ask', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: query.value })
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          loader.value.style.display = 'none';
          console.log("Received data:", data);

          const answerBubble = createBubble(data.answer, 'answer');
          chatBox.value.appendChild(answerBubble);
          chatBox.value.scrollTop = chatBox.value.scrollHeight;
        })
        .catch(error => {
          loader.value.style.display = 'none';
          const errorBubble = createBubble('出现错误，请稍后再试。', 'answer');
          chatBox.value.appendChild(errorBubble);
          console.error('There was a problem with the fetch operation:', error);
        });
    }

    function createBubble(content, type) {
      var bubble = document.createElement('div');
      bubble.className = 'chat-bubble ' + type;
      bubble.innerHTML = marked.parse(content);
      MathJax.typesetPromise([bubble]).then(() => {
        console.log("MathJax typesetting completed.");
      }).catch(err => {
        console.error("MathJax typesetting error:", err);
      });
      return bubble;
    }

    function handleKeyDown(event) {
      if (event.key === 'Enter') {
        event.preventDefault();
        askQuestion();
      }
    }

    onMounted(() => {
      loader.value = document.getElementById('loader');
      chatBox.value = document.getElementById('chat-box');
    });

    return {
      query,
      loader,
      chatBox,
      askQuestion,
      handleKeyDown
    };
  }
};
</script>

<style scoped>
/* 在这里添加或引用AINavigator.css文件 */
@import '@/assets/css/ainavigator.css';
</style>
