<template>
  <div class="grid gap-5 grid-cols-12 my-5">
    <div class="col-span-9">
      <FormSearch />
      <Video :videos="videos !== {} ? getTraining.chapiters[0].lessons[0].videos : videos"></Video>
    </div>
    <div class="col-span-3 w-full">
      <IconsProfil />
      <Content @emit-video="setVideos" :chapiters="getTraining.chapiters"></Content>
    </div>
  </div>
</template>

<script>
import Video from "./Video.vue";
import Content from "./Content.vue";
import IconsProfil from "../IconsProfil.vue";
import FormSearch from "../FormSearch.vue";
import {mapGetters} from 'vuex'

export default {
  data() {
    return {
      videos: {}
    }
  },
  components: {
    Video,
    Content,
    IconsProfil,
    FormSearch,
  },
  computed: {
    ...mapGetters(['getTraining']),
  },
  methods: {
    setVideos(videos){
      console.log(videos);
      this.videos = videos
    }
  }
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