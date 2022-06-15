<template>
  <div class="">
    <div class="flex">
      <div class="grid grid-cols-1 w-full">
        <div class="mt-2">
          <div class="md:flex sm:flex-wrap">
            <div class="lg:w-3/4 w-full">
              <FormSearch />
            </div>
            <div class="lg:w-1/4 sm:w-1/2 sm:mx-auto mt-2">
              <IconsProfil />
            </div>
          </div>
        </div>
        <div>
          <div class="md:flex sm:flex w-full my-5 gap-4">
            <div class="lg:w-3/4 pl-10 py-10">
              <h2 v-if="getUser.userType === 'member'" class="text-xl font-bold mb-1">Member {{getUser.profile.login}}</h2>
              <h2 v-if="getUser.userType === 'user'" class="text-xl font-bold mb-1">User {{getUser.profile.login}}</h2>
              <div class="w-full relative">
                <button class="bg h-fit w-full" @click="editProfile">
                  <img :src="getUser.profile.image_path" class="w-full" />
                </button>
                <div class="absolute top-24 left-10">
                  <button class="hover:opacity-80" @click="editProfile">
                    <img
                      :src="getUser.profile.profile_image"
                      class="h-28 border-8 border-white rounded-full"
                    />
                  </button>
                </div>
                <div
                  class="
                    border-2 border-t-0
                    relative
                    border-slate-300
                    p-5
                    pt-2
                    rounded-b-xl
                  "
                >
                  <div class="w-1/4 ml-48">
                    <button class="font-semibold mb-2">
                      <a href="http://">{{ getUser.profile.login }}</a>
                    </button>
                    <p class="text-sm mb-2">{{ getUser.profile.email }}</p>
                    <button
                      class="text-sm rounded-lg bg-amber-500 w-fit p-1 mb-5"
                    >
                      <a href="http://">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="16"
                          height="16"
                          fill="currentColor"
                          class="bi inline-block mr-1 bi-pin-map-fill"
                          viewBox="0 0 16 16"
                        >
                          <path
                            fill-rule="evenodd"
                            d="M3.1 11.2a.5.5 0 0 1 .4-.2H6a.5.5 0 0 1 0 1H3.75L1.5 15h13l-2.25-3H10a.5.5 0 0 1 0-1h2.5a.5.5 0 0 1 .4.2l3 4a.5.5 0 0 1-.4.8H.5a.5.5 0 0 1-.4-.8l3-4z"
                          />
                          <path
                            fill-rule="evenodd"
                            d="M4 4a4 4 0 1 1 4.5 3.969V13.5a.5.5 0 0 1-1 0V7.97A4 4 0 0 1 4 3.999z"
                          />
                        </svg>
                        Yaounde, CAMEROON
                      </a>
                    </button>
                    <div class="flex gap-x-3">
                      <a href="http://">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="16"
                          height="16"
                          fill="currentColor"
                          class="bi bi-github"
                          viewBox="0 0 16 16"
                        >
                          <path
                            d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"
                          />
                        </svg>
                      </a>
                      <a href="http://">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="16"
                          height="16"
                          fill="currentColor"
                          class="bi bi-linkedin"
                          viewBox="0 0 16 16"
                        >
                          <path
                            d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"
                          />
                        </svg>
                      </a>
                      <a href="http://">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="16"
                          height="16"
                          fill="currentColor"
                          class="bi bi-twitter"
                          viewBox="0 0 16 16"
                        >
                          <path
                            d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"
                          />
                        </svg>
                      </a>
                      <a href="http://">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="16"
                          height="16"
                          fill="currentColor"
                          class="bi bi-facebook"
                          viewBox="0 0 16 16"
                        >
                          <path
                            d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z"
                          />
                        </svg>
                      </a>
                    </div>
                  </div>
                  <div v-if="getUser.userType === 'member'" class="flex gap-x-1 absolute bottom-4 left-12">
                    <span class="inline-block mr-2">8.6</span>
                    <div v-for="i in 5" :key="i" class="inline-block">
                      <button class="inline-block">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="16"
                          height="16"
                          fill="#0077EA"
                          class="bi bi-star-fill"
                          viewBox="0 0 16 16"
                        >
                          <path
                            d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"
                          />
                        </svg>
                      </button>
                    </div>
                  </div>

                  <Edit title="Edit Profile" @button-click="editProfile"></Edit>
                </div>
              </div>
              <div v-if="getUser.userType === 'member'">
                <div class="mt-7 mb-0">
                  <div class="flex font-medium border-b-1 text-lg text-center">
                    <button
                      @click="viewChild = link"
                      class="w-1/4"
                      :class="viewChild == link ? 'link-active' : ''"
                      v-for="link in ListOfLinks"
                      :key="link"
                    >
                      <span>{{ link }}</span>
                    </button>
                  </div>
                </div>
                <div class="pl-10 py-10">
                  <Overview v-if="viewChild === 'Overview'" />
                  <FollowedSyllabus v-if="viewChild === 'FollowedSyllabus'" />
                  <Syllabus v-if="viewChild === 'Syllabus'" />
                  <NewSyllabus v-if="viewChild === 'NewSyllabus'" />
                </div>
              </div>
              <div  v-if="getUser.userType === 'user'" class="my-5 pb-1">
                <div class="p-10 border-2 rounded-lg">
                  <h3 class="font-bold text-xl my-2">Description</h3>
                  <p class="text-sm">Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate rem laboriosam est consectetur itaque porro, expedita adipisci, cupiditate, pariatur unde enim molestias architecto id quisquam aspernatur qui explicabo nobis eaque!</p>
                </div>
                <div class="px-10 py-2 my-5 border-2 rounded-lg h-54 overflow-auto">
                  <SyllabusList />
                </div>
              </div>
            </div>

            <div class="lg:w-1/4 sm:w-full">
              <div>
                <div class="md:col-span-3">
                  <div class="flex flex-col gap-y-4 mt-10">
                    <div v-if="getUser.userType === 'member'"  class="rounded-xl border-2 p-4">
                      <Statistics :stats="stats"></Statistics>
                    </div>
                    <div class="rounded-xl border-2 p-4 mb-5 relative">
                      <AdditonalDetails></AdditonalDetails>
                      <Edit></Edit>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import IconsProfil from "./layout/IconsProfil.vue";
import FormSearch from "./layout/FormSearch.vue";
import Edit from "./layout/member-dashboard/Edit.vue";
import Statistics from "./layout/member-dashboard/Statistics.vue";
import SyllabusList from "./layout/member-dashboard/SyllabusList.vue";
import AdditonalDetails from "./layout/member-dashboard/AdditonalDetails.vue";
import FollowedSyllabus from "./layout/member-dashboard/children/FollowedSyllabus.vue";
import NewSyllabus from "./layout/member-dashboard/children/NewSyllabus.vue";
import Overview from "./layout/member-dashboard/children/Overview.vue";
import Syllabus from "./layout/member-dashboard/children/Syllabus.vue";
import { mapGetters, mapActions } from "vuex";

const stats = [
  {
    color: "orange",
    per: 2,
    title: "SYLLABUS FOLLOW ",
  },
  {
    color: "green",
    per: 1,
    title: "VIDEOS COMMENT",
  },
  {
    color: "blue",
    per: 3,
    title: "VIDEOS SHARED",
  },
  {
    color: "red",
    per: 4,
    title: "VIDEOS LIKED",
  },
];

const ListOfLinks = ["Overview", "FollowedSyllabus", "Syllabus", "NewSyllabus"];
const col = ListOfLinks.length;
export default {
  data() {
    return {
      viewChild: "Overview",
    };
  },
  components: {
    IconsProfil,
    FormSearch,
    Edit,
    Statistics,
    AdditonalDetails,
    Overview,
    FollowedSyllabus,
    Syllabus,
    NewSyllabus,
    SyllabusList,
  },
  setup() {
    return {
      ListOfLinks,
      col,
      stats,
    };
  },
  methods: {
    ...mapActions(["getProfile"]),
    editProfile() {
      console.log("profile edit ...");
    },
  },
  created() {
    this.getProfile();
  },
  mounted() {
    this.getProfile();
  },
  computed: {
    ...mapGetters(["getUser"]),
  },
};
</script>

<style>
</style>