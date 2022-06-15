<template>
  <h3 class="font-bold text-xl my-2">Followed Syllabus</h3>
  <ul>
    <li v-for="i in 5" :key="i" class="my-2">
      <router-link :to="{name: 'Dashboard', params:{token: getUser.token, id:'5' } }" class="flex items-center justify-between"
        ><div class="w-fit">
          <input
            type="checkbox"
            class="
              mr-5
              p-2
              bg-blue-600
              default:right-0
              ring-0
              active:ring-0
              checked:ring-0
              border-none
              rounded-full
            "
            checked
          /><span class="text-sm">UI/UX Design</span>
        </div>
        <div class="w-3/5 flex items-center gap-x-2">
          <div class="w-full inline-block border-2 border-blue-400 rounded-lg p-1">
            <div :style="{width: '50%'}" class="bar"></div>
          </div> <div class="text-sm">50%</div>
        </div>
      </router-link>
    </li>
  </ul>
</template>

<script>
export default {
  props: {
    FollowedSyllabus: {},
  },
};
</script>

<style scoped>
input#slider {
  -webkit-appearance: none;
  display: none;
}
.bar {
  height: 5px;
  border-radius: 5px;
  background-color: yellow;
}
</style>