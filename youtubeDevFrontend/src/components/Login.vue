<template>
  <div
    class="grid grid-cols-2 min-h-screen justify-items-center content-center"
  >
    <div class="container p-16 w-full">
        <HeaderSign title="Log In"/>
      <div class="mt-16">
        <FormSign page="login" btnTitle="Log in"></FormSign>
      </div>
    </div>
    <div></div>
  </div>
</template>

<script>
import FormSign from "./layout/register-login/FormSign.vue";
import HeaderSign from "./layout/register-login/HeaderSign.vue";
export default {
  components: {
    FormSign,
    HeaderSign,
  },
};
</script>

<style>
</style>