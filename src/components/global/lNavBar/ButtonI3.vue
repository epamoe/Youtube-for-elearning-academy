<template>
    <div class ="buttonI3" >
      <div class="btI3Message">
          {{ message }}
      </div>
      <div><img src = './images/triangle.svg'/></div>
    </div>
</template>
<style>
    .buttonI3 {
      display: flex;
      padding: 5px;
      padding-left: 15px;
      padding-right: 15px;
      font-size: 15px;
      background-color:#0089BF;
      color:white;
      border-radius: 0.4em;
      opacity: 1;
      cursor: pointer;
    }
    .btI3Message {
      margin-right: 5px
    }
    .btI3Message + div {
      display: flex; justify-content: center; align-items: center;
      width: 16px;
    }
    .buttonI3 img {
      width: 100%;
    }

    /* on hover */
    .buttonI3:hover {
      opacity: 0.6;
    }
    /*----- responsive managment zone... ------------------ */
    @media screen and (max-width: 440px) {
    }
</style>
<script>
export default {
  name: 'ButtonI3',
  props: {
    message: String
  }
}
</script>
