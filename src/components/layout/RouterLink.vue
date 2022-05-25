<template>
  <div class="flex font-medium border-b-1 text-lg text-center">
    <router-link :class="'w-1/4'" v-for="link in ListOfLinks" :to="{ name: link }"
      :key="link"><span>{{ link }}</span></router-link
    >
  </div>
</template>

<script>
export default {
    props: {
        ListOfLinks: Object,
        col: Number
    }
};
</script>

<style scoped>
    .flex.font-medium.text-lg a{
        background-color: transparent;
    }
    .border-b-1{
      border-bottom: 1px solid rgb(211, 211, 211);
    }
</style>