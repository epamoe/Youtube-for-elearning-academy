<template>
  <div>
    <div class="grid grid-cols-12">
      <div class="col-span-2 min-h-screen">
            <Aside></Aside>
      </div>
      <div class="main col-span-10">
        <AppBar></AppBar>
        <Main></Main>
      </div>
    </div>
  </div>
</template>

<script>
import Main from "./layout/dashboard/Main.vue";
import Aside from "./layout/dashboard/Aside.vue";
import AppBar from "./layout/dashboard/AppBar.vue";
export default {
  components: {
    Main,
    Aside,
    AppBar,
  },
};
</script>

<style>
</style>