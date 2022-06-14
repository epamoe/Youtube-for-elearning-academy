<template>
  <div class="Myprofile">
    <div class="profileMain">
        <div
          class="profileContent"
          :style="{ left:Position }"
        >
          <div class="profileCont">
            <div style="margin-right:5%"><Testimony/></div>
            <div style="margin-left:5%"><Testimony/></div>
          </div>
          <div class="profileCont">
            <div style="margin-right:5%"><Testimony/></div>
            <div style="margin-left:5%"><Testimony/></div>
          </div>
          <div class="profileCont">
            <div style="margin-right:5%"><Testimony/></div>
            <div style="margin-left:5%"><Testimony/></div>
          </div>
        </div>
      </div>
      <div class="myPUpground">
          <span @click="move(1)"><img src="./back.svg"/></span>
          <span @click="move(-1)"><img src="./next.svg"/></span>
      </div>
  </div>
</template>
<style src="./myProfile.css">
</style>
<script src="./myProfile.js">
</script>
