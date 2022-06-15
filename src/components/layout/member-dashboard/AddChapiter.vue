<template>
  <div
    class="my-5 relative border-1 border-slate-800 rounded-lg p-5"
    style="width: 400px"
    v-for="i in chapiterCount + 1"
    :key="i"
  >
    <Chapiter :i="i" @send-chapiter-title="addChapiter" />
  </div>

  <button
    @click.prevent="chapiterCount += 1"
    class="absolute plus-chap"
    title="add a chapiter"
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="36"
      height="36"
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
import Chapiter from './Chapiter.vue'
export default {
  data() {
    return {
      chapiterCount: 0,
      chapiters: []
    };
  },
  components: {
    Chapiter
  },
  methods: {
    addChapiter(chapiter) {
      this.chapiters = this.chapiters.filter(
        (chap) => chap.title !== chapiter.title
      );
      this.chapiters = [...this.chapiters, chapiter];

      this.$emit("sendChapiters", this.chapiters);
    },
  }
};
</script>

<style>
.plus {
  left: calc(50% - 26px);
  bottom: -30px;
}
.plus-chap {
  left: calc(50% - 30px);
  bottom: -25px;
}
</style>