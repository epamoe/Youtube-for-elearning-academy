<template>
  <div class="bg-white mt-2">
    <div class="p-5 relative">
      <h2 class="text-lg font-semibold">Section {{ num }}: {{ title }}</h2>
      <p class="text-sm font-semibold">5/5 |10min</p>
      <button class="absolute right-4 top-8" v-if="show" @click="show = !show">
        <svg
          width="14"
          height="8"
          viewBox="0 0 14 8"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M12.0864 7.82605L6.84783 2.98887L1.60924 7.82605L0 6.33688L6.84783 -3.71933e-05L13.6957 6.33688L12.0864 7.82605Z"
            fill="black"
          />
        </svg>
      </button>
      <button class="absolute right-4 top-8" v-if="!show" @click="show = !show">
        <svg
          width="14"
          height="8"
          viewBox="0 0 14 8"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M1.60939 0L6.84797 4.83718L12.0866 0L13.6958 1.48917L6.84797 7.82609L0.000148773 1.48917L1.60939 0Z"
            fill="black"
          />
        </svg>
      </button>
    </div>
  </div>
  <transition name="show-section">
    <div class="p-5 mb-2" v-if="show">
      <CheckedList @lesson-video="$emit('videoLesson', lesson)" :item="lesson.title" v-for="lesson in lessons" :key="lesson" ></CheckedList>
    </div>
  </transition>
</template>

<script>
import CheckedList from '../CheckedList.vue'
export default {
  emits: ['videoLesson'],
  props: {
    title: String,
    num: String,
    lessons: Object,
  },
  components: {
    CheckedList
  },
  data() {
    return {
      show: false,
    };
  },
};
</script>

<style>
.show-section-enter-active {
  animation: slide-height 0.25s;
}

.show-section-leave-active {
  animation: slide-height 0.25s reverse;
}

@keyframes slide-height {
  from {
    transform: translateY(-20px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}
</style>