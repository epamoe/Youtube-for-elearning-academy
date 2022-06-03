<template>
  <div class="p-5">
    <iframe
      class="w-full aspect-video"
      width="935"
      height="315"
      :src="videos[0].link"
    ></iframe>
    <input type="range" name="" id="" class="w-full" />
    <div class="flex justify-between items-center">
      <div class="col-span-2">
        <div class="flex gap-2">
          <div>
            <button title="icon">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-arrow-repeat"
                viewBox="0 0 16 16"
              >
                <path
                  d="M11.534 7h3.932a.25.25 0 0 1 .192.41l-1.966 2.36a.25.25 0 0 1-.384 0l-1.966-2.36a.25.25 0 0 1 .192-.41zm-11 2h3.932a.25.25 0 0 0 .192-.41L2.692 6.23a.25.25 0 0 0-.384 0L.342 8.59A.25.25 0 0 0 .534 9z"
                />
                <path
                  fill-rule="evenodd"
                  d="M8 3c-1.552 0-2.94.707-3.857 1.818a.5.5 0 1 1-.771-.636A6.002 6.002 0 0 1 13.917 7H12.9A5.002 5.002 0 0 0 8 3zM3.1 9a5.002 5.002 0 0 0 8.757 2.182.5.5 0 1 1 .771.636A6.002 6.002 0 0 1 2.083 9H3.1z"
                />
              </svg>
            </button>
          </div>
          <div class="mx-2">
            <button>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="20"
                height="20"
                fill="currentColor"
                class="bi bi-volume-up-fill"
                viewBox="0 0 16 16"
              >
                <path
                  d="M11.536 14.01A8.473 8.473 0 0 0 14.026 8a8.473 8.473 0 0 0-2.49-6.01l-.708.707A7.476 7.476 0 0 1 13.025 8c0 2.071-.84 3.946-2.197 5.303l.708.707z"
                />
                <path
                  d="M10.121 12.596A6.48 6.48 0 0 0 12.025 8a6.48 6.48 0 0 0-1.904-4.596l-.707.707A5.483 5.483 0 0 1 11.025 8a5.483 5.483 0 0 1-1.61 3.89l.706.706z"
                />
                <path
                  d="M8.707 11.182A4.486 4.486 0 0 0 10.025 8a4.486 4.486 0 0 0-1.318-3.182L8 5.525A3.489 3.489 0 0 1 9.025 8 3.49 3.49 0 0 1 8 10.475l.707.707zM6.717 3.55A.5.5 0 0 1 7 4v8a.5.5 0 0 1-.812.39L3.825 10.5H1.5A.5.5 0 0 1 1 10V6a.5.5 0 0 1 .5-.5h2.325l2.363-1.89a.5.5 0 0 1 .529-.06z"
                />
              </svg>
            </button>
          </div>
          <div>
            <button>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="20"
                height="20"
                fill="currentColor"
                class="bi bi-stop-fill"
                viewBox="0 0 16 16"
              >
                <path
                  d="M5 3.5h6A1.5 1.5 0 0 1 12.5 5v6a1.5 1.5 0 0 1-1.5 1.5H5A1.5 1.5 0 0 1 3.5 11V5A1.5 1.5 0 0 1 5 3.5z"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>
      <div class="col-span-2">
        <div class="flex gap-2">
          <div>
            <button>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="20"
                height="20"
                fill="currentColor"
                class="bi bi-skip-start-fill"
                viewBox="0 0 16 16"
              >
                <path
                  d="M4 4a.5.5 0 0 1 1 0v3.248l6.267-3.636c.54-.313 1.232.066 1.232.696v7.384c0 .63-.692 1.01-1.232.697L5 8.753V12a.5.5 0 0 1-1 0V4z"
                />
              </svg>
            </button>
          </div>
          <div class="mx-2">
            <button>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="20"
                height="20"
                fill="currentColor"
                class="bi bi-pause-fill"
                viewBox="0 0 16 16"
              >
                <path
                  d="M5.5 3.5A1.5 1.5 0 0 1 7 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5zm5 0A1.5 1.5 0 0 1 12 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5z"
                />
              </svg>
            </button>
          </div>
          <div>
            <button>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="20"
                height="20"
                fill="currentColor"
                class="bi bi-skip-end-fill"
                viewBox="0 0 16 16"
              >
                <path
                  d="M12.5 4a.5.5 0 0 0-1 0v3.248L5.233 3.612C4.693 3.3 4 3.678 4 4.308v7.384c0 .63.692 1.01 1.233.697L11.5 8.753V12a.5.5 0 0 0 1 0V4z"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>
      <div class="col-span-2">
        <div class="flex gap-2">
          <div>
            <button>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-music-note-list"
                viewBox="0 0 16 16"
              >
                <path
                  d="M12 13c0 1.105-1.12 2-2.5 2S7 14.105 7 13s1.12-2 2.5-2 2.5.895 2.5 2z"
                />
                <path fill-rule="evenodd" d="M12 3v10h-1V3h1z" />
                <path
                  d="M11 2.82a1 1 0 0 1 .804-.98l3-.6A1 1 0 0 1 16 2.22V4l-5 1V2.82z"
                />
                <path
                  fill-rule="evenodd"
                  d="M0 11.5a.5.5 0 0 1 .5-.5H4a.5.5 0 0 1 0 1H.5a.5.5 0 0 1-.5-.5zm0-4A.5.5 0 0 1 .5 7H8a.5.5 0 0 1 0 1H.5a.5.5 0 0 1-.5-.5zm0-4A.5.5 0 0 1 .5 3H8a.5.5 0 0 1 0 1H.5a.5.5 0 0 1-.5-.5z"
                />
              </svg>
            </button>
          </div>
          <div class="mx-2">
            <button>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-heart-fill"
                viewBox="0 0 16 16"
              >
                <path
                  fill-rule="evenodd"
                  d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"
                />
              </svg>
            </button>
          </div>
          <div>
            <button>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-chat-left-fill"
                viewBox="0 0 16 16"
              >
                <path
                  d="M2 0a2 2 0 0 0-2 2v12.793a.5.5 0 0 0 .854.353l2.853-2.853A1 1 0 0 1 4.414 12H14a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="my-3">
      <h2 class="text-2xl font-semibold my-4">Related Videos</h2>
      <div class="grid lg:grid-cols-4 md:grid-cols-2 sm:grid-cols-2 gap-x-4">
        <div v-for="video in videos.filter(video => video.id !== '1')" :key="video.id">
          <iframe
            class="w-full aspect-video"
            width="935"
            height="100"
            :src="video.link"
          ></iframe>
          <a href="http://"><p>lorem ipsum</p></a>
          <span class="text-xs">5|10 min</span>
        </div>
      </div>
    </div>
    <div class="mt-5 mb-0">
      <RouterLink :ListOfLinks="ListOfLinks" :col="col"></RouterLink>
    </div>
  </div>
  <div class="px-5 pb-1">
    <router-view></router-view>
  </div>
</template>

<script>
import RouterLink from "../RouterLink.vue";

const ListOfLinks = ["Presentation", "Chat", "Testimonies", "Links"];
const col = ListOfLinks.length;
export default {
  props: {
    videos: Object,
  },
  data() {
    return {
      showBar: false,
      showBar1: false,
      videosListTemp: [],
      videosList: [],
    };
  },
  setup() {
    return {
      ListOfLinks,
      col,
    };
  },
  components: {
    RouterLink,
  },
  methods: {},
};
</script>

<style>
.flex.font-medium.text-lg .router-link-exact-active {
  position: relative;
}
.flex.font-medium.text-lg .router-link-exact-active::after {
  content: "";
  display: block;
  width: 100%;
  background-color: #fdaa07;
  height: 1.5px;
  transition: all ease-in-out;
  animation: slide-bar 0.5s;
  position: absolute;
  bottom: -1px;
}

.grid a {
  border-bottom: 1.5px solid rgb(196, 194, 194);
}

/* .bar-bottom-enter-from,
  .bar-bottom-leave-to {
    width: 0;
  } */

@keyframes slide-bar {
  from {
    width: 0;
  }
  to {
    width: 100%;
  }
}
</style>