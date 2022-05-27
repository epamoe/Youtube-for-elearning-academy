<template>
  <div
    class="grid grid-cols-2 min-h-screen justify-items-center content-center"
  >
    <div class="container p-16 w-full">
      <HeaderSign title="Log In" />
      <div class="mt-16">
        <FormSign
          @submit-form="log"
          page="login"
          btnTitle="Log in"
        ></FormSign>
      </div>
    </div>
    <div></div>
  </div>
</template>

<script>
import FormSign from "./layout/register-login/FormSign.vue";
import HeaderSign from "./layout/register-login/HeaderSign.vue";
import { mapActions } from 'vuex'
import { useRouter } from "vue-router";
export default {
  methods: {
    ...mapActions(["login"]),
    log(user) {
      this.login({username:user.login, password:user.password})
      this.$router.push({
          name: "Dashboard",
      });
    },
  },
  components: {
    FormSign,
    HeaderSign,
  },
  setup() {
    const router = useRouter();
    return {router};
  },
};
</script>

<style>
</style>