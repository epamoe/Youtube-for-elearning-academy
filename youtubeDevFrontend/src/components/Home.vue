<template>
  <div class="min-h-screen">
    <div class="flex">
      <div class="min-h-screen icons pb-5">
        <IconsMenu></IconsMenu>
      </div>
      <div class="main w-full">
        <router-view></router-view>
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