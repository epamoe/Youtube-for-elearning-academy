<template>
   <div class="border-2 border-slate-300 rounded-lg p-10">
      <h5 class="text-xs">Image</h5>
     <form class="flex">
       <div class="border-1 relative border-slate-800 h-44 w-64 rounded-lg p-5">
           <input type="file" name="" class="file w-full h-full opacity-0 z-50">
           <div class="absolute w-full h-full ab-center">
            <div class="relative w-full  h-full">
              <div class="absolute center w-fit text-center">
               <button class="absolute btn-center">
                 <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-plus-circle" viewBox="0 0 16 16">
                    <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                    <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
                  </svg>
                </button>
                <img src="/images/Vector18.png" class="inline-block">
                <div class="text-xs left-0 tex-center mt-2">Drag and drop or upload picture</div>
              </div>
            </div>
          </div>
         </div>
       <div>
         
       </div>
     </form>
   </div>
</template>

<script>
  export default {
    data(){
      return {
        syllabus : {
          image: '',

        } ,
      }
    }
  }
</script>

<style scoped>
  .file{
    display: inline-block;
    border: 1px solid #999;
    padding: 5px 8px;
    outline: none;
    white-space: nowrap;
    -webkit-user-select: none;
    cursor: pointer;
    text-shadow: 1px 1px #fff;
    font-weight: 700;
    font-size: 10pt;
    position: absolute;
    top: 0;
    left: 0;
  }
  .ab-center{
    top: 0;
    left: 0;
  }
  .btn-center{
    top: calc(50% - 15px);
    left: calc(50% - 15px);
  }
  .center{
    top: calc(50% - 51.5px);
    left: calc(50% - 87px);
  }
</style>