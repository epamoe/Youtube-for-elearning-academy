<template>
  <div>
    <div class="grid grid-cols-12">
      <div class="col-span-2 min-h-screen">
            <Aside></Aside>
      </div>
      <div class="main col-span-10">
        <Main></Main>
      </div>
    </div>
  </div>
</template>

<script>
import Main from "./layout/dashboard/Main.vue";
import Aside from "./layout/dashboard/Aside.vue";
export default {
  components: {
    Main,
    Aside,
  },
};
</script>

<style>
</style>