<template>
  <div class="content mt-5">
    <h1 class="text-3xl font-bold mb-5 p-5">Content</h1>
    <div class="mb-2" v-for="chapiter in chapiters" :key="chapiter.title">
      <Section
        num="1"
        :title="chapiter.title"
        :lessons="chapiter.lessons"
        @video-lesson="emitVideo"
      ></Section>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import Section from "./Section.vue";

const listOfTopics = [
  "on Ubuntu",
  "on Mac",
  "on Windows",
  "visual studio",
  "Hello world",
];
export default {
  emits: ['emitVideo'],
  props: {
    chapiters: Object,
  },
  data() {
    return {
      videos: {}
    }
  },
  components: {
    Section,
  },
  setup() {
    return {
      listOfTopics,
    };
  },
  methods: {
    emitVideo(lesson){
      this.videos = lesson.videos
      this.$emit('emitVideo', this.videos)
    }
  }
};
</script>

<style>
* {
  padding: 0;
  margin: 0;
}
</style>