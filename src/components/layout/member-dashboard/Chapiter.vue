<template>
  <div
    style="width: 355px"
    class="mx-auto relative"
    @keypress.enter="addLesson"
  >
    <label class="text-xs">Chapiter {{ i }} </label> <br />
    <input
      v-model="chapiter.title"
      type="text"
      class="border-1 w-full border-slate-800 rounded-lg"
    />
    <AddLesson @send-lesson-title="addLesson" />
  </div>
</template>

<script>
import AddLesson from "./AddLesson.vue";
import Title from "./Lesson.vue";
export default {
  props: {
    i: Number,
  },
  data() {
    return {
      chapiterCount: 0,
      chapiter: {
        title: "",
        lessons: [],
      },
      send: false,
    };
  },
  components: {
    AddLesson,
    Title,
  },
  methods: {
    addLesson(lesson) {
      if (!this.send) {
        this.chapiter.lessons = this.chapiter.lessons.filter(
          (les) => les !== lesson
        );
        this.chapiter.lessons = [...this.chapiter.lessons, lesson];
        this.send = !this.send
        this.$emit("sendChapiterTitle", this.chapiter)
      }
    },
  },
};
</script>

<style>
</style>