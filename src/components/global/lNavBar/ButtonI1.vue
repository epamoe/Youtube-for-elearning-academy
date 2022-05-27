<template>
    <div class ="buttonI1" >
      <img src = './images/label1.svg'/>
      <div :style="{color:Color}" class="btI1Message">
          {{ message }}
      </div>
    </div>
</template>
<style>
    .buttonI1 {
        position: relative;
        width:120px;
    }
    .btI1Message {
      position:absolute;
      left: 0%;
      top:0%;
      display: flex; justify-content:center;align-items: center;
      width: 100%;
      height: 100%;
      font-size: 15px;
    }
    .buttonI1 img {
      width: 100%;
      height: 100%;
    }
    /*----- responsive managment zone... ------------------ */
    @media screen and (max-width: 440px) {
    }
</style>
<script>
export default {
  name: 'ButtonI1',
  props: {
    message: String,
    Color: {
      type: String,
      default: 'white'
    }
  }
}
</script>
