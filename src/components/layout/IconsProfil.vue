<template>
  <div class="flex gap-x-10 justify-between items-center">
    <div class="font-normal" v-if="!connect">become a member</div>
    <div class="">
      <a href="http://"
        ><img src="/images/drapeaux-francais-anglais-1.png" class="inline"
      /></a>
      Fr
    </div>
    <div class="relative">
      <a href="http://">
        <svg
          width="23"
          height="23"
          viewBox="0 0 23 23"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          xmlns:xlink="http://www.w3.org/1999/xlink"
        >
          <rect width="23" height="23" fill="url(#pattern0)" />
          <defs>
            <pattern
              id="pattern0"
              patternContentUnits="objectBoundingBox"
              width="1"
              height="1"
            >
              <use xlink:href="#image0_71_45" transform="scale(0.0104167)" />
            </pattern>
            <image
              id="image0_71_45"
              width="96"
              height="96"
              xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAABmJLR0QA/wD/AP+gvaeTAAAC2ElEQVR4nO3dzWoTYRTG8b9FUykVhSoK2diFiB9bcavLLvQOdKOIBS0ICuKqSwUVRK/GuhEsxlZU8A68gzYWN7FxkQQkmo+ZzDln3pnnBwcKTfK+73lmJjPNkIKIiIiIiEj5zQNrQAv42a8WcL//OzHUBL4B3RH1tf8YMTDP+Ob/HYL2BANrTG7+oO4FzbHSPjF9AB+D5lhpbaYPoB00x8wORE8gg27GxyextrnoCdRdKgEcz/GcpcJnUTNHgVXgA9Bh+uP/oDrAe+AOcMR57kk7CTynd4Wbtemjahd4BpxwXEdyDgEPyXa2k7V2gAfAQac1JWMZ2MSu8cO1BZxxWVkCrmG71Y/bG1Yc1ldqd8n3BltUdYBb5qssqVVgn7jmD2ofuG281tJZIXbL/9+ecN10xSVylphj/qTapQZvzA3gC/HNHlXb9E6HK+sJ8U2eVI/MVh+sCewR3+BJ1QZOGfXgH55/jHsMLDiOl9ciFdwLloBfxG/d09YecMykE0O89oCbwGGnsYqwANyInkSRPhO/VWetlkknAjQpxxVv1vqNw5uxxyHoKol8PjtkDrjiMYi1Sw5jWLlsPYBHAOcdxrByznoAjwBOO4xhZdl6AI8AUv4cNs/dGJl4BJDC1e8oi9YDeJyddB3GsGTao1RuzKosBRBMAQRTAMEUQDAFEEwBBFMAwRRAMAUQTAEEUwDBFEAwBRBMAQRTAMEUQDAFEEwBBFMAwRRAMAUQTAEEsw5g3fj1PTyNnkBe68Tf419UJRdClZqfXAhVbH4yIVS5+aUPoQ7NL20IdWp+6UKoY/MLC6GIe9+7BbxGymbqoa6EgymAYApARERERprlKy53AuabSQpnQT+CnusihQA2Znju28JmUWMXyf8fNFL+qpxSeUP2AF6FzLSiGsA7pm/+BhX/CuIIDeA14w9HHXpbvppv6ALwEvhO7xS13f/5BTrmi4iIiIhIAv4AGFMdm4j3fMUAAAAASUVORK5CYII="
            />
          </defs>
        </svg>
      </a>

      <div class="absolute bottom-0 right-0">
        <svg
          width="10"
          height="10"
          viewBox="0 0 40 40"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <circle cx="20" cy="20" r="20" fill="#FDAA07" />
        </svg>
      </div>
    </div>
    <div class="relative">
      <button @click="showUserInfo"><img src="/images/women.png" style="height: 40px" /></button>
      <div class="absolute bottom-1 right-0">
        <svg
          width="10"
          height="10"
          viewBox="0 0 40 40"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <circle cx="20" cy="20" r="20" fill="#FDAA07" />
        </svg>
      </div>
      <div class="absolute bg-gray-100 rounded px-5 py-2 w-fit top-12 right-2 text-sm z-50" v-if="userInformation">
        <ul>
          <li class="mb-2"><a href="http://">profile</a></li>
          <li class="mb-2"><a href="http://">profile</a></li>
          <hr class="my-2"/>
          <li><a href="http://" @click.prevent="out">logOut</a></li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      connect: true,
      userInformation: false
    }
  },
  methods: {
    ...mapActions(["logOut"]),
    out() {
      this.logOut();
      this.$router.push({
        name: 'Login'
      })
    },
    showUserInfo() {
      this.userInformation = !this.userInformation;
    },
  },
};
</script>

<style>
</style>