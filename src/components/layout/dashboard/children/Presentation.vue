<template>
  <div class="container mx-auto">
    <h2 class="text-3xl font-bold">About this page</h2>
    <h3 class="text-2xl my-3 font-semibold">Description</h3>
    <p class="text-sm">
      {{getTraining.description}}
    </p>
    <ul class="my-5 text-sm">
      <li>Level: Beginner</li>
      <li>Participants: 422</li>
      <li>language: English</li>
      <li>Sub-title: yes</li>
      <li>leçon: {{ lessonCount }}</li>
      <li>Vidéo: 1 hour in total</li>
    </ul>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
export default {
  computed: {
    ...mapGetters(['getTraining']),
    lessonCount(){
      let count = 0
      for (let index = 0; index < this.getTraining.chapiters.length; index++) {
        const chap = this.getTraining.chapiters[index];
        for (let i = 0; i < chap.lessons.length; i++) {
            count++
        }
      }
      return count
    }
  },
};
</script>

<style>
</style>