<template>
    <div class ="buttonLand1" >
        {{ message }}
    </div>
</template>
<style>
    .buttonLand1 {
      display: flex; justify-content: center;align-items: center;
      padding-top: 10px;
      padding-bottom: 10px;
      width:160px;
      font-size: 15px;
      background-color:#1C8EFB;
      font-weight: bold;
      color:white;
      border-radius: 0.7em;
      opacity: 1;
      cursor: pointer;
    }

    /* on hover */
    .buttonLand1:hover {
      opacity: 0.6;
    }
    /*----- responsive managment zone... ------------------ */
    @media screen and (max-width: 440px) {
    }
</style>
<script>
export default {
  name: 'ButtonLand1',
  props: {
    message: String
  }
}
</script>
