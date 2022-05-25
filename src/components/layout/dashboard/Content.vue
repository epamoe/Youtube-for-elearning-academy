<template>
  <div class="content mt-5">
    <h1 class="text-3xl font-bold mb-5 p-5">Content</h1>
    <Section
      num="1"
      title="Introduction"
      :listOfTopics="listOfTopics"
    ></Section>
    <Section
      num="1"
      title="Introduction"
      :listOfTopics="listOfTopics"
    ></Section>
    <Section
      num="1"
      title="Introduction"
      :listOfTopics="listOfTopics"
    ></Section>
    <Section
      num="1"
      title="Introduction"
      :listOfTopics="listOfTopics"
    ></Section>
    <Section
      num="1"
      title="Introduction"
      :listOfTopics="listOfTopics"
    ></Section>
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
  components: {
    Section,
  },
  setup() {
    return {
      listOfTopics,
    };
  },
};
</script>

<style>
* {
  padding: 0;
  margin: 0;
}
</style>