<template>
  <div class="inputSearchT">
    <div class="inputSearchTText">
      <div class="inputSearchTTextFirst">
        <img src="./loupe.svg"/>
        <input v-model="toSearch" type="text" placeholder="Find trainings">  
      </div>
    </div>
    <div class="inputSearchTButton">
      <button @click="search">
        Search
      </button>
    </div>
  </div>
</template>
<style src="./inputSearchT.css">
</style>
<script src="./inputSearchT.js">
</script>
