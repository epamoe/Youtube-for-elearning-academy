<template>
    <div class ="buttonI0" @mouseenter="DispMenu='block'" @mouseleave="DispMenu='none'" >
      <div :style="{color:Color}" class="btIOMessage">
          {{ message }}
      </div>
      <div :style="{display:DispMenu}">
        <div>Logement étudian de particulier</div>
        <div> Résidence etudiant</div>
        <div>marché etudian en video</div>
      </div>
    </div>
</template>
<style>
    .buttonI0 {
        position: relative;
    }
    .btIOMessage {
      width:110px;
      font-size: 18px;
      padding: 5px;
      color: #0089BF;
      cursor: pointer;
      border-top: solid 4px;
    }
    .btIOMessage + div {
      position: absolute;
      padding: 10px;
      font-size: 16px;
      text-align: left;
      color:gray;
      box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
    }
    .btIOMessage + div > div {
      margin-bottom: 10px;
      cursor: pointer;
    }
    .btIOMessage + div > div:hover {
      color:#0089BF;
    }
  /*----- responsive managment zone... ------------------ */
    @media screen and (max-width: 440px) {
    }
</style>
<script>
export default {
  name: 'ButtonI0',
  props: {
    message: String,
    Color: {
      type: String,
      default: '#0089BF'
    },
    DispMenu: {
      type: String,
      default: 'none'
    }
  }
}
</script>
