<template>
  <div>
    <h3 class="text-2xl my-3 font-semibold">Participants comment</h3>
    <div class="comment" v-for="comment in getTraining.comments" :key="comment.id">
      <Comment :comment="comment" ></Comment>
    </div>
  </div>
</template>

<script>
  import Comment from "../Comment.vue"
  import {mapGetters} from 'vuex'
export default {
  components: {
    Comment
  },
  computed: {
    ...mapGetters(['getTraining']),
  }
}
</script>

<style>

</style>