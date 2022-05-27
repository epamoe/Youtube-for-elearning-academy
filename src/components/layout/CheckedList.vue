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
      :class="rounded === 'true' ? 'rounded-full' : ''"
      checked
      v-if="check === '1'"
    />
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
      :class="rounded === 'true' ? 'rounded-full' : ''"
      v-if="check !== '1'"
    />
    <a href="htttp//:" @click.prevent="$emit('lessonVideo')" class="text-sm">{{ item }}</a>
  </div>
</template>

<script>
export default {
    props: {
        item: String,
        rounded: String,
        check: String,
    }
};
</script>

<style>
</style>