<template>
    <a href="http://localhost:3000/login">
      <div class ="buttonNav2" >
        {{ message }}
    </div>
    </a>
</template>
<style>
    .buttonNav2 {
      display: flex;
      padding: 5px;
      padding-left: 20px;
      padding-right: 20px;
      font-size: 15px;
      font-weight: bold;
      color:#000000;
      border-radius: 0.7em;
      opacity: 1;
      cursor: pointer;
    }

    /* on hover */
    .buttonNav2:hover {
      color:#1C8EFB;
    }
    /*----- responsive managment zone... ------------------ */
    @media screen and (max-width: 440px) {
    }
</style>
<script>
export default {
  name: 'ButtonNav2',
  props: {
    message: String
  }
}
</script>
