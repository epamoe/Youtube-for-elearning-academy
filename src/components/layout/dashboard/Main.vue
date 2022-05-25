<template>
  <div class="grid gap-5 grid-cols-12 my-5">
    <div class="col-span-9">
      <FormSearch />
      <Video></Video>
    </div>
    <div class="col-span-3 w-full">
      <IconsProfil />
      <Content></Content>
    </div>
  </div>
</template>

<script>
import Video from "./Video.vue";
import Content from "./Content.vue";
import IconsProfil from "../IconsProfil.vue";
import FormSearch from "../FormSearch.vue";

export default {
  components: {
    Video,
    Content,
    IconsProfil,
    FormSearch,
  },
};
</script>

<style>
.content {
  background: #ededed;
}
.border-r-1 {
  border-right-width: 1px;
}
.border-1 {
  border-width: 1px;
}
.form,
.input,
.form div div select {
  background-color: #e5e5e5;
}
</style>