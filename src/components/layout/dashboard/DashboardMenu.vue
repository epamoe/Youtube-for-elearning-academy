<template>
    <div class="flex flex-col h-full justify-between pt-3">
      <div class="relative px-6">
        <a href="http://"><h2 class="text-xl mb-14 mt-3">Dashboard</h2></a>
        <ul>
          <li class="mb-3">
            <a href="/member-dashboard" class="text-white">profile</a>
          </li>
          <li class="mb-3">
            <a href="/member-dashboard" class="text-white">update profile</a>
          </li>
          <li class="mb-3">
            <a href="/member-dashboard" class="text-white">delete profile</a>
          </li>
        </ul>
      </div>
      <div class="self-center">
        <img src="/images/personcomputer.png" class="p-0 m-0" />
      </div>
    </div>
</template>

<script>
export default {};
</script>
<style>
.grid a {
  border: none;
}
</style>