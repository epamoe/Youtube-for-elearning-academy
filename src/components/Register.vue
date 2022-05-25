<template>
  <div
    class="grid grid-cols-2 min-h-screen justify-items-center content-center"
  >
    <div class="container p-16 w-full">
      <HeaderSign title="Sign In" />
      <div class="mt-16">
        <FormSign
          @submit-form="register"
          page="register"
          btnTitle="Sign in"
        ></FormSign>
      </div>
    </div>
    <div></div>
  </div>
</template>

<script>
import FormSign from "./layout/register-login/FormSign.vue";
import HeaderSign from "./layout/register-login/HeaderSign.vue";
import { mapActions } from "vuex";
import { useRouter } from "vue-router";
import store from "../store/index";

export default {
  methods: {
    register(user) {
      store
        .dispatch("register", user)
        .then((res) => {
          if(res){
            this.router.push({name:'Login'})
          }
        });
      console.log(user);
    },
  },
  setup() {
    const router = useRouter();
    return {router};
  },
  components: {
    FormSign,
    HeaderSign,
  },
};
</script>

<style>
</style>