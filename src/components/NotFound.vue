<template>
  <div>
    <div class="flex justify-center">
      <div class="min-h-screen icons pb-5">
        <IconsMenu></IconsMenu>
      </div>
      <div class="main mx-auto container mt-5">
        <h1 class="text-9xl bg-red-500 text-white text-center p-1">Erreu 404</h1>
        <p class="text-center text-3xl text-gray-400">
            Page not Found
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import IconsMenu from "./layout/IconsMenu.vue";
export default {
  components: {
    IconsMenu,
  },
};
</script>

<style>
</style>