<template>
  <div class="md:flex sm:flex-wrap w-full my-5">
    <div class="mx-auto lg:w-3/4 sm:w-full">
      <Video :videos="videos !== {} ? getTraining.chapiters[0].lessons[0].videos : videos"></Video>
    </div>
    <div class="lg:w-1/4 sm:w-full justify-self-end">
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