<template>
  <div class="w-64 my-3 mx-auto" v-for="j in lessonsCount + 1" :key="j">
    <label class="text-xs">Lessons {{ j }} </label> <br />
    <Lesson @send-lesson="sendLessonTitle" />
  </div>
  <button
    @click.prevent="lessonsCount += 1"
    class="absolute plus"
    title="add a lesson"
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="26"
      height="26"
      fill="yellow"
      class="bi bi-plus-circle-fill"
      viewBox="0 0 16 16"
    >
      <path
        d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3z"
      />
    </svg>
  </button>
</template>

<script>
import Lesson from "./Lesson.vue";
export default {
  data() {
    return {
      lessonsCount: 0,
      lessonTitle: "",
    };
  },
  components: {
    Lesson,
  },
  methods: {
    sendLessonTitle(lesson) {
      if (lesson !== "") this.$emit("sendLessonTitle", lesson);
    },
  },
};
</script>

<style>
</style>