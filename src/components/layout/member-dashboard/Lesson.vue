<template>
  <input
    @keypress.enter="sendLesson"
    @blur="sendLesson"
    v-model="lessonTitle"
    type="text"
    class="border-1 w-full border-slate-800 rounded-lg"
  />
</template>

<script>
export default {
  data() {
    return {
      lessonTitle: "",
      send : false
    };
  },
  methods: {
    sendLesson(e) {
      if(!this.send){
        this.send = !this.send
        this.$emit("sendLesson", this.lessonTitle);
      }
    },
  },
};
</script>

<style>
</style>