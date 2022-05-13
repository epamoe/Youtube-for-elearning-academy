<template>
  <div>
    <h3 class="text-2xl my-3 font-semibold">Participants comment</h3>
    <div class="comment">
      <Comment></Comment>
      <Comment></Comment>
      <Comment></Comment>
      <Comment></Comment>
    </div>
  </div>
</template>

<script>
  import Comment from "../Comment.vue"
export default {
  components: {
    Comment
  }
}
</script>

<style>

</style>