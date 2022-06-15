<template>
    <div class ="buttonNav1" >
        {{ message }}
    </div>
</template>
<style>
    .buttonNav1 {
      display: flex;
      padding: 10px;
      padding-left: 20px;
      padding-right: 20px;
      font-size: 13px;
      background-color:#1C8EFB;
      font-weight: bold;
      color:white;
      border-radius: 0.7em;
      opacity: 1;
      cursor: pointer;
    }

    /* on hover */
    .buttonNav1:hover { 
      box-shadow: 15px;
      background-color: #FDAA07;
      transition-duration: 500ms;
      transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    }
    /*----- responsive managment zone... ------------------ */
    @media screen and (max-width: 440px) {
    }
</style>
<script>
export default {
  name: 'ButtonNav1',
  props: {
    message: String
  }
}
</script>
