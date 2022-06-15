<template>
  <div class="relative">
    <ul class="flex font-bold w-full bg-white absolute py-5  z-20 text-gray-500">
      <li class="pl-5 w-2/5">Title</li>
      <li class="text-center w-1/5">total followers</li>
      <li class="text-center w-1/5">Comment</li>
      <li class="text-center w-1/5">Note</li>
    </ul>
    <div class="border-2 border-slate-300 p-5 pt-2 overflow-auto rounded-xl">
      <table class="w-full h-48 table-auto m-2 text-sm" >
        <tbody>
          <tr v-for="i in 20" :key="i">
            <td class="w-2/5"><router-link :to="{name: 'Dashboard', params: {token: 'hqsj_54dfs8f5fh-@gdg15g4', id:'2'} }" href="/dashboard">Javascript advance course</router-link></td>
            <td class="w-1/5 text-center"><router-link :to="{name: 'Dashboard', params: {token: 'hqsj_54dfs8f5fh-@gdg15g4', id:'2'} }" href="/dashboard">102</router-link></td>
            <td class="w-1/5 text-center"><router-link :to="{name: 'Dashboard', params: {token: 'hqsj_54dfs8f5fh-@gdg15g4', id:'2'} }" href="/dashboard">5</router-link></td>
            <td class="w-1/5 text-center"><router-link :to="{name: 'Dashboard', params: {token: 'hqsj_54dfs8f5fh-@gdg15g4', id:'2'} }" href="/dashboard">3</router-link></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
  th, td {
    height: 50px;
  }
  div{
    height: 500px;
  }
  ul{
    width: 97%;
    left: 8px;
    top: 2px;
  }
</style>