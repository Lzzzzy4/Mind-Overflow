<!-- src/components/CollapsibleSidebar.vue -->
<template>
  <div class="sidebar" :class="{ 'collapsed': isCollapsed }">
    <button @click="toggleCollapsed">{{ isCollapsed ? '展开' : '收起' }}</button>
    <div v-if="!isCollapsed" class="content">
      <h3 class="historylist">历史记录</h3>
      <ul>
        <li v-for="record in records" :key="record.id">
          {{ record.text }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SidebarHistory',
  props: {
    records: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      isCollapsed: false
    };
  },
  methods: {
    toggleCollapsed() {
      this.isCollapsed = !this.isCollapsed;
    }
  }
};
</script>

<style scoped>
.historylist{
  color:black;
}
/*.sidebar {
  侧边栏的样式 
}
.sidebar.collapsed {
  折叠后的侧边栏样式 
}
.content {
  侧边栏内容区域的样式 
} */
</style>
