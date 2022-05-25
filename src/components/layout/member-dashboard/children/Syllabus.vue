<template>
  <div class="relative">
    Syllabus <Edit title="Add a new Syllabus" @button-click="addSyllabus" />
  </div>
</template>

<script setup>
import Edit from "../Edit.vue";
function addSyllabus(){
  console.log('syllabus add...')
}
</script>

<style>
</style>