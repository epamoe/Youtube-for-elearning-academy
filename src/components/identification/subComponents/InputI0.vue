<template>
<div class="inputI0">
  <span>{{name}} <span style="color:red;font-size:16px">*</span></span>
  <div class="inputZone">
  <input
      v-bind:placeholder = "placeholder"
      v-bind:type ="typeData"
      v-bind:max ="max"
      v-bind:min ="min"
      v-bind:pattern ="pattern"
      v-model="message"
      />
    <div @click="textVisible" :style="{display:eyeDisplay}" ><EyeCross ref="eye" /></div>
  </div>
</div>
</template>
<style>
  .inputI0 {
    display: flex;
    flex-direction: column;
    font-weight: bold;
  }
  .inputI0 span {
    margin-bottom: 3px;
  }
  .inputI0 input {
      box-sizing: border-box;
      background-color: transparent;
      padding: 10px;
      width: 100%;
      font-size: 14px;
      border: solid 2px black;
      border-radius: 0.6em;
      padding-left: 25px;
      color: rgb(70,70,70);
  }
  .inputI0 input:focus {
      border-color:#1C8EFB;
      border-width: 2px;
  }
  .inputI0 .inputZone {
    width: 400px;
    position: relative;
  }
  .inputI0 .inputZone div {
    position: absolute;
    right:0px;
    margin-right: 20px;
    top:50%;
    margin-top: -10px;
    width: 20px;
    height: 20px;
  }

  /*----- responsive managment zone... ------------------ */
  @media screen and (max-width: 440px) {
      .inputI0 {
          width: 90%;
      }
  }
</style>
<script>
import EyeCross from './eyeCross/EyeCross.vue'
export default {
  name: 'InputI0',
  components: {
    EyeCross
  },
  props: {
    placeholder: String,
    type: String,
    max: Number,
    min: Number,
    pattern: String,
    name: String
  },
  data () {
    return {
      message: '',
      eyeDisplay: 'none',
      typeData: this.type
    }
  },
  methods: {
    textVisible () {
      this.$refs.eye.clicked()
      this.typeData = (this.typeData === 'password') ? 'text' : 'password'
    }
  },
  mounted () {
    if (this.typeData === 'password') this.eyeDisplay = 'block'
  }
}
</script>
