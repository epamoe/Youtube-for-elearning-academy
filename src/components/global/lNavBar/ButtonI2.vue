<template>
    <div class ="buttonI2" >
      <img src = './images/label.svg'/>
      <div class="btI2Message">
          {{ message }}
      </div>
    </div>
</template>
<style>
    .buttonI2 {
        position: relative;
        width:120px;
    }
    .btI2Message {
      position:absolute;
      left: 0%;
      top:0%;
      display: flex; justify-content:center;align-items: center;
      width: 100%;
      height: 100%;
      font-size: 15px;
      color:#0089BF
    }
    .buttonI2 img {
      width: 100%;
      height: 100%;
    }
    /*----- responsive managment zone... ------------------ */
    @media screen and (max-width: 440px) {
    }
</style>
<script>
export default {
  name: 'ButtonI2',
  props: {
    message: String
  }
}
</script>
