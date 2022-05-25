<template>
  <div action="" class="grid grid-cols-12 px-2 mt-5 gap-5">
    <div class="col-span-8"><FormSearch></FormSearch></div>
    <div class="col-span-4">
      <IconsProfil></IconsProfil>
    </div>
  </div>
</template>

<script>
import IconsProfil from '../IconsProfil.vue';
import FormSearch from '../FormSearch.vue';
export default {
  components: {
    IconsProfil,
    FormSearch
  }
};
</script>

<style>

</style>