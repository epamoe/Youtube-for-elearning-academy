<template>
  <div class="flex relative h-full">
    <div class="absolute top-12 left-1">
      <button @click="show = !show">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          :fill="show ? '#fff' : 'black'"
          class="bi bi-chevron-left"
          viewBox="0 0 16 16"
        >
          <path
            fill-rule="evenodd"
            d="M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z"
          />
        </svg>
      </button>
    </div>
    <transition name="show-dashboard">
      <div class="dashboard w-full p-5" v-if="show">
        <DashboardMenuVue></DashboardMenuVue>
      </div>
    </transition>
  </div>
</template>

<script>
import DashboardMenuVue from "./DashboardMenu.vue";
import IconsMenu from "../IconsMenu.vue";
export default {
  components: {
    DashboardMenuVue,
    IconsMenu,
  },
  data() {
    return {
      show: true,
    };
  },
};
</script>

<style>
.dashboard {
  background-color: #45a4ff;
  color: white;
}
.icons {
  background-color: #0077ea;
}
.show-dashboard-enter-active {
  animation: slide-dashboard 0.5s;
}

.show-dashboard-leave-active {
  animation: slide-dashboard 0.5s reverse;
}

@keyframes slide-dashboard {
  from {
    width: 0;
    opacity: 0;
  }
  to {
    width: 100%;
    opacity: 1;
  }
}
</style>