<template>
  <div class="mb-5">
    <div class="rounded-xl mt-5 border-2 px-10 py-3 relative">
      <h4 class="text-md font-semibold">Description</h4>
      <p class="text-sm my-5">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ex, laboriosam
        dolorem harum autem natus ducimus ipsa animi facere ab? Facilis aperiam
        ex consectetur esse sint vero quod. Quas, suscipit quaerat.
      </p>
      <p class="text-sm">
        Quo enim, dicta eligendi iure, accusamus incidunt illo earum corrupti
        non optio velit repellat. Laudantium qui corrupti provident impedit illo
        minus fuga!
      </p>
      <Edit></Edit>
    </div>
    <div class="rounded-xl mt-3 border-2 px-10 py-3 relative">
      <h4 class="text-md font-semibold">Mini Portfolio</h4>
      <div class="flex">
        <div class="w-1/4">
          <CheckedList
            :item="item"
            v-for="item in listOfTopics"
            :key="item"
            rounded="true"
          ></CheckedList>
        </div>
        <div class="w-1/4">
          <CheckedList
            :item="item"
            v-for="item in listOfTopics"
            :key="item"
            rounded="true"
          ></CheckedList>
        </div>
      </div>
      <Edit></Edit>
    </div>
  </div>
</template>

<script>
import Edit from "../Edit.vue";
import CheckedList from "../../CheckedList.vue";

const listOfTopics = [
  "on Ubuntu",
  "on Mac",
  "on Windows",
  "visual studio",
  "Hello world",
];

export default {
  components: {
    Edit,
    CheckedList,
  },
  setup() {
    return {
      listOfTopics,
    };
  },
};
</script>

<style>
</style>