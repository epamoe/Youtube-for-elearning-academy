<template>
  <div class="py-2">
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
      "
      :class="rounded ? 'rounded-full' : ''"
    />
    <span class="text-sm">{{ item }}</span>
  </div>
</template>

<script>
export default {
    props: {
        item: String,
        rounded: Boolean
    }
};
</script>

<style>
</style>