<template>
  <div class="mb-5">
    <div class="flex flex-col gap-y-5">
      <div class="">
        <h5 class="text-sm p-0 ml-16 mb-1">Fai</h5>
        <div class="flex items-center gap-x-2">
          <img src="/images/fai.png" class="rounded-full h-10" />
          <div
            class="
              relative
              message-guess
              rounded-t-3xl rounded-br-3xl
              w-fit
              max-w-md
              p-3
              mt-0
              text-sm
            "
          >
            <p class="text-sm mb-4">Lorem ipsum dolor sit amet</p>
            <span class="block absolute right-3 bottom-1 text-gray-500"
              >10:38 am</span
            >
          </div>
        </div>
      </div>
      <div
        class="
          relative
          message-user
          rounded-t-3xl rounded-bl-3xl
          w-fit
          max-w-md
          self-end
          p-3
        "
      >
        <p class="text-sm mb-4">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus
          quos libero vero sapiente voluptatibus, iure laboriosam sint facere
          fugit qui. Cupiditate corporis, dolor dolores unde magnam rerum magni
          quaerat temporibus.
          <span class="block absolute right-1 bottom-1 text-gray-500"
            >10:38 am</span
          >
        </p>
      </div>
    </div>
    <form action="" class="flex gap-x-5 mt-24">
      <div class="textarea w-full">
        <textarea
          style="resize: none"
          class="form-textarea rounded-3xl w-full h-24"
          placeholder="enter your message"
        ></textarea>
      </div>
      <div class="button flex flex-col justify-around">
        <div>
          <button type="submit">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              fill="#F7990E"
              class="bi bi-send-fill"
              viewBox="0 0 16 16"
            >
              <path
                d="M15.964.686a.5.5 0 0 0-.65-.65L.767 5.855H.766l-.452.18a.5.5 0 0 0-.082.887l.41.26.001.002 4.995 3.178 3.178 4.995.002.002.26.41a.5.5 0 0 0 .886-.083l6-15Zm-1.833 1.89L6.637 10.07l-.215-.338a.5.5 0 0 0-.154-.154l-.338-.215 7.494-7.494 1.178-.471-.47 1.178Z"
              />
            </svg>
          </button>
        </div>
        <div>
          <button type="submit">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              fill="currentColor"
              class="bi bi-emoji-smile"
              viewBox="0 0 16 16"
            >
              <path
                d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"
              />
              <path
                d="M4.285 9.567a.5.5 0 0 1 .683.183A3.498 3.498 0 0 0 8 11.5a3.498 3.498 0 0 0 3.032-1.75.5.5 0 1 1 .866.5A4.498 4.498 0 0 1 8 12.5a4.498 4.498 0 0 1-3.898-2.25.5.5 0 0 1 .183-.683zM7 6.5C7 7.328 6.552 8 6 8s-1-.672-1-1.5S5.448 5 6 5s1 .672 1 1.5zm4 0c0 .828-.448 1.5-1 1.5s-1-.672-1-1.5S9.448 5 10 5s1 .672 1 1.5z"
              />
            </svg>
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
* {
  box-sizing: border-box;
}
.message-user {
  background: #fdaa0759;
}
h5 {
  color: #f7990e;
}
.message-guess {
  box-shadow: 0px 2px 4px 0px #00000040;
  background: #ffffff;
}
textarea {
  box-shadow: 0px 4px 4px 0px #00000040;
  border: 1px solid #dedede !important;
}
</style>