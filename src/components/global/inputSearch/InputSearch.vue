<template>
  <div class="inputSearch">
    <div class="inputSearchText">
      <div class="inputSearhTextFirst">
        <div><img style="width:15px" src="./loupe.svg"/></div>
        <input v-model="toSearch" type="text" placeholder="Find trainings">  
      </div>
      <div>
        <select placeholder="Categories"> 
          <option style="display:none">trainings</option>
          <option>Something1</option>
        </select>
        <img src="./arrow.svg"/>
      </div>
    </div>
    <div class="inputSearchButton">
      <button @click="search">
        Search
      </button>
    </div>
  </div>
</template>
<style src="./inputSearch.css">
</style>
<script src="./inputSearch.js">
</script>
