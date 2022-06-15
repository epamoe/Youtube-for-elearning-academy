<template>
  <form class="formRequest">
    <div class="formRequestField">
      <span class="formRequestF"><span>Nom <span style="color:#FDAA07;">*</span>  </span></span>
      <input class="focus:outline-none focus:ring-offset-2" type="text" placeholder="Enter your name">
    </div>
    <div class="formRequestField">
      <span class="formRequestF"><span>Email <span style="color:#FDAA07;">*</span></span></span>
      <input class="focus:outline-none focus:ring-offset-2" type="text" placeholder="Enter your E-mail">
    </div>
    <div class="formRequestField">
      <span class="formRequestF"><span>Message <span style="color:#FDAA07;">*</span></span></span>
      <textarea class="focus:outline-none focus:ring-offset-2 rounded-md h-20 text-sm py-1 px-2" placeholder="Enter your request"></textarea>
    </div>
    <div class="formRequestButton">
      <button class=" hover:bg-indigo-500 hover:shadow-lg shadow-yellow-3 hover:border-transparent focus:outline-none transition easy-out duration-300">Send</button>
    </div>
  </form>
</template>
<style src="./formRequest.css">
</style>
<script src="./formRequest.js">
</script>
