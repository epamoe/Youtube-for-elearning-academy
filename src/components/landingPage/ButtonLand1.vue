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
      box-shadow: 15px;
      background-color: #FDAA07;
      transition-duration: 500ms;
     transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    }
    /* hover:bg-[#FDAA07] hover:shadow-lg shadow-yellow-3 hover:border-transparent focus:outline-none transition easy-out duration-300*/
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
