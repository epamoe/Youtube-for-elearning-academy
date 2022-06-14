<template>
<div class="global">
    <LPublication/>
</div>
</template>
<style>
  .global {
      margin: 100px;
  }
</style>
<script>
import LPublication from './lPublication/LPublication.vue'
export default {
  name: 'Global',
  components: {
    LPublication
  }
}
</script>
