<template>
  <form action="">
      <div class="" v-if="page === 'register' ">
          <Input type="text" title="Name" placeholder="Enter your Name"></Input>
          <Input type="email" title="Email" placeholder="Enter your Email"></Input>
          <Input type="password" title="Password" placeholder="Enter your Password"></Input>
          <Input type="password" title="Confirm Password" placeholder="Confirm your Password"></Input>
          <div class="flex justify-between items-center">
              <div>
                  <CheckedList item="Keep loged in"/>
              </div>
              <div>
                  <a href="http://" class="text-blue-500">Forgot password?</a>
              </div>
          </div>
          <SubmitButton :title="btnTitle"/>
      </div>
      <div class="" v-if="page !== 'register' ">
          <Input type="text" title="Login" placeholder="Enter your login"></Input>
          <Input type="password" title="Password" placeholder="Enter your Password"></Input>
          <div class="flex justify-between items-center">
              <div>
                  <CheckedList item="Keep loged in"/>
              </div>
              <div>
                  <a href="http://" class="text-blue-500">Forgot password?</a>
              </div>
          </div>
          <SubmitButton :title="btnTitle"/>
      </div>
  </form>
</template>

<script>
    import Input from "./Input.vue"
    import SubmitButton from "./SubmitButton.vue"
    import CheckedList from "../CheckedList.vue"
export default {
    props: {
        page: String,
        btnTitle: String,
    },
    components: {
        Input,
        SubmitButton,
        CheckedList,
    }
};
</script>

<style>

</style>