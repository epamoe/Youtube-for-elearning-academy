<template>
  <div>
    <h4 class="font-semibold">Statistics</h4>
    <div
      class="
        flex
        items-end
        border-l-4 border-b-4
        bg-
        border-black
        h-24
        gap-x-1
        px-1
      "
    >
      <div
        v-for="stat in stats"
        :key="stat.title"
        :class="`w-1/4 relative h-${stat.per}/5 bg-${stat.color}-600`"
      >
        <div class="absolute text-xs t-2">{{ (stat.per / 4) * 100 }}%</div>
      </div>
    </div>
    <ul class="p-0 mt-10">
      <li v-for="stat in stats" :key="stat" class="flex items-center">
        <button
          :class="`w-2 h-2 rounded-full bg-${stat.color}-600 inline-block mr-4`"
        ></button>
        <span class="text-sm">{{ stat.title }}</span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    statistics: Object,
  },
  setup() {
    const stats = [
      {
        color: "orange",
        per: 2,
        title: "SYLLABUS FOLLOW ",
      },
      {
        color: "green",
        per: 1,
        title: "VIDEOS COMMENT",
      },
      {
        color: "blue",
        per: 3,
        title: "VIDEOS SHARED",
      },
      {
        color: "red",
        per: 4,
        title: "VIDEOS LIKED",
      },
    ];
    return {
      stats,
    };
  },
};
</script>

<style>
.t-2 {
  top: -1rem;
}
</style>