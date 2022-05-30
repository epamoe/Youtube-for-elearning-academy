<template>
  <div>
    <div class="flex">
      <div class="min-h-screen" v-if="width > 1230">
          <Aside></Aside>
      </div>
      <div class="grid grid-cols-1 w-full">
        <div class="mt-2">
          <div class="md:flex sm:flex-wrap">
            <div class="lg:w-3/4 w-full">
              <FormSearch/>
            </div>
            <div class="lg:w-1/4 sm:w-1/2 sm:mx-auto mt-2">
              <IconsProfil />
            </div>
          </div>
        </div>
        <div>
          <div class="md:flex sm:flex-wrap w-full my-5">
            <div class="lg:w-3/4 sm:w-full">
              <Video :videos="videos !== {} ? getTraining.chapiters[0].lessons[0].videos : videos"></Video>
            </div>
            <div class="lg:w-1/4 sm:w-full">
              <Content @emit-video="setVideos" :chapiters="getTraining.chapiters"></Content>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Main from "./layout/dashboard/Main.vue";
import Video from "./layout/dashboard/Video.vue";
import Aside from "./layout/dashboard/Aside.vue";
import Content from "./layout/dashboard/Content.vue";
import IconsProfil from "./layout/IconsProfil.vue";
import FormSearch from "./layout/FormSearch.vue";
import {mapGetters} from 'vuex'

export default {
  data() {
    return {
      width: document.documentElement.clientWidth,
    }
  },
  components: {
    Main,
    Aside,
    IconsProfil,
    FormSearch,
    Video,
    Content,
  },
  methods: {
    size(e){
      this.width = document.documentElement.clientWidth
        console.log(this.width)
    },
    setVideos(videos){
      console.log(videos);
      this.videos = videos
    }
  },
  mounted() {
    window.addEventListener('resize', this.size);
  },
  unmounted() {
    window.removeEventListener('resize', this.size);
  },
  computed: {
    ...mapGetters(['getTraining']),
  },
};
</script>

<style>
</style>