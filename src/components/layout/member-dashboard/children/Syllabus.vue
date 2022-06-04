<template>
  <div class="border-2 border-slate-800 p-10 rounded-lg syllabus overflow-auto ">
    <div v-for="i in 10" class="mb-5 text-sm border-2 p-4 border-slate-300 p-5 pt-2 rounded-lg relative">
      <div class="flex items-center m-5 gap-x-24">
        <div class="w-1/3 note">
          <div class="m-0 p-0 rounded-t-xl overflow-hidden">
            <img src="/images/dev-javascript.png">
          </div>
          <div class="bg-gray-100 shdw rounded-b-xl py-1 px-2">
            <div class="relative">
              <h5>Title</h5>
              <div class="text-center font-bold border-2 border-black p-2 rounded-lg">Javascript advance course</div>
            </div>
            <div class="relative mt-1">
              <h5>Description</h5>
              <div class="border-2 border-black p-2 rounded-lg">
                Lorem ipsum dolor sit amet,consectetur adipiscing elit. Lorem ipsum dolor sit amet,consectetur adipiscing elit.
              </div>
            </div>
          </div>
        </div>
        <div class="w-2/3 comment">
          <div class="relative">
            <h5>Followers and note</h5>
            <ul class="flex font-bold bg-white absolute py-2  z-20 rounded-lg">
                <li class="ml-3 w-3/4">User</li>
                <li class="text-center w-1/4">Note</li>
            </ul>
            <div class="border-2 border-black relative p-2 rounded-lg h-44 overflow-auto">
                <table class="w-full mt-10">
                  <tbody>
                    <tr v-for="i in 20" :key="i">
                      <td class="w-3/4">
                        <img src="/images/fai.png" class="rounded-full inline-block h-7 mr-2">
                        <span>Tchiaguia christophe</span>
                      </td>
                      <td class="w-1/4">
                        <div class="flex justify-center gap-x-1 bottom-4 left-12">
                          <div v-for="i in 5" :key="i" class="inline-block">
                            <button class="inline-block">
                              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#0077EA" class="bi bi-star-fill" viewBox="0 0 16 16">
                                <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                              </svg>
                            </button>
                          </div>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
            </div>
          </div>
          <div class="mt-2 relative">
            <h5>Comments per chapter</h5>  
            <ul class="flex font-bold w-full bg-white absolute py-2  z-20 rounded-lg">
                <li class="pl-2 w-3/5">User</li>
                <li class="text-center w-1/5">Chapiter</li>
                <li class="text-center w-1/5">lesson</li>
            </ul>
            <div class="border-2 border-black p-2 rounded-lg h-44  overflow-auto">
              <table class="w-full mt-10 relative">
                <tbody>
                  <tr v-for="i in 20" :key="i">
                    <td class="flex w-full">
                      <img src="/images/fai.png" class="rounded-full inline-block h-7 mr-2">
                      <div class="inline-block">
                        <span>Tchiaguia christophe</span>
                        <p>Lorem ipsum dolor sit amet,consectetur adipiscing elit. Lorem ipsum dolor sit amet,consectetur adipiscing elit.</p>
                      </div>
                    </td>
                    <td class="text-center text-center w-1/5">5</td>
                    <td class="text-center text-center w-1/5">2</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>      
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import Edit from '../Edit.vue'
</script>

<style scoped>
  .syllabus{
    height: 600px;
  }
  .shdw{
    box-shadow: 1px 4px 4px 0px #00000040;
  }
  div {
    font-size: 11px;
  }
  td{
    padding: 5px 0;
  }
  ul{
    width: 96%;
    top: 22px;
    left: 4px;
  }
</style>