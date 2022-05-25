<template>
  <form action="" @submit.prevent="$emit('submitForm', user)">
    <div class="" v-if="page === 'register'">
      <Input
        @change-input="login"
        type="text"
        title="Login"
        placeholder="Enter your login"
      ></Input>
      <Input
        @change-input="email"
        type="email"
        title="Email"
        placeholder="Enter your Email"
      ></Input>
      <Input
        type="password"
        title="Password"
        placeholder="Enter your Password"
        @change-input="password"
      ></Input>
      <Input
        type="password"
        title="Confirm Password"
        placeholder="Confirm your Password"
        @change-input="passwordConfirm"
      ></Input>
      <div class="flex justify-between items-center">
        <div>
          <CheckedList item="Keep loged in" />
        </div>
        <div>
          <a href="http://" class="text-blue-500">Forgot password?</a>
        </div>
      </div>
      <SubmitButton :title="btnTitle" />
    </div>
    <div class="" v-if="page !== 'register'">
      <Input
        @change-input="login"
        type="text"
        title="Login"
        placeholder="Enter your login"
      ></Input>
      <Input
        type="password"
        title="Password"
        placeholder="Enter your Password"
        @change-input="password"
      ></Input>
      <div class="flex justify-between items-center">
        <div>
          <CheckedList item="Keep loged in" />
        </div>
        <div>
          <a href="http://" class="text-blue-500">Forgot password?</a>
        </div>
      </div>
      <SubmitButton :title="btnTitle" />
    </div>
  </form>
</template>

<script>
import Input from "./Input.vue";
import SubmitButton from "./SubmitButton.vue";
import CheckedList from "../CheckedList.vue";

export default {
  props: {
    page: String,
    btnTitle: String,
  },
  data() {
    return {
      user: {
        login: "",
        email: "",
        password: "",
        confirm_password: "",
      },
    };
  },
  components: {
    Input,
    SubmitButton,
    CheckedList,
  },
  methods: {
    login(login) {
      this.user.login = login;
    },
    email(email) {
      this.user.email = email;
    },
    password(password) {
      this.user.password = password;
    },
    passwordConfirm(confirm_password) {
      this.user.confirm_password = confirm_password;
    },
  },
};
</script>

<style>
</style>