<template>
  <div class="home">
    <div class="flex justify-end mt-2">
      <button class="bg-blue-500 text-white hover:text-stone-950 hover:bg-amber-500 p-2 rounded-md"
        @click="this.modalIsHidden = !this.modalIsHidden">Create Post</button>
    </div>
    <div id="editProfile" aria-hidden="true" :class="{ hidden: modalIsHidden }"
      class="overflow-y-auto overflow-x-hidden fixed right-0 left-0 top-4 z-50 justify-center items-center md:h-full md:inset-x-1/4">
      <div class="relative px-4 w-full max-w-2xl h-full md:h-auto">
        <div class="relative bg-white rounded-lg shadow-lg border-2">
          <div class="flex justify-between items-start p-5 rounded-t border-b">
            <h3 class="text-xl font-semibold text-gray-900 lg:text-2xl dark:text-white">
              Create a Post
            </h3>
            <button type="button"
              class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center"
              data-modal-toggle="defaultModal" @click="this.modalIsHidden = !this.modalIsHidden">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd"
                  d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                  clip-rule="evenodd"></path>
              </svg>
            </button>
          </div>
          <form action="POST" enctype="multipart/form-data" @submit.prevent="createPost">
            <div class="p-6 space-y-6">
              <div>
                <div>
                  <label for="firstName" class="block mb-1 text-gray-600 font-medium">Title</label>
                  <input name="firstName" type="text"
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-teal-500 focus:ring focus:ring-teal-300 focus:ring-opacity-50"
                    v-model="this.post.title"
                    @keyup="updateSlug" />
                </div>
              </div>
              <div>
                <div>
                  <label for="firstName" class="block mb-1 text-gray-600 font-medium">Slug</label>
                  <input v-model="this.post.slug" name="firstName" type="text" placeholder="It is used for url to make readable to end users"
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-teal-500 focus:ring focus:ring-teal-300 focus:ring-opacity-50" />
                </div>
              </div>
              <div>
                <div>
                  <label for="formFile" class="block mb-1 text-gray-600 font-medium">Featured Image</label>
                  <input
                    class="mt-1 block w-full rounded-md border-gray-300 focus:border-teal-500 focus:ring focus:ring-teal-300 focus:ring-opacity-50"
                    type="file" id="formFile" accept="image/*" />
                </div>
              </div>
              <div>
                <label for="bio" class="block mb-1 text-gray-600 font-medium">Content</label>
                <textarea type="text"
                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-teal-500 focus:ring focus:ring-teal-300 focus:ring-opacity-50"
                  rows="5" />
              </div>
              <div>
                <label class="inline-flex items-center cursor-pointer">
                  <input type="checkbox" value="" class="sr-only peer">
                  <div
                    class="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600">
                  </div>
                  <span class="ms-3 text-sm font-medium text-gray-900 dark:text-gray-300">Publish</span>
                </label>
              </div>
              <div>
                <label class="inline-flex items-center cursor-pointer">
                  <input type="checkbox" value="" class="sr-only peer">
                  <div
                    class="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600">
                  </div>
                  <span class="ms-3 text-sm font-medium text-gray-900 dark:text-gray-300">Featured(Trending/Hot
                    Topic)</span>
                </label>
              </div>
            </div>

            <div class="flex items-center p-6 space-x-2 rounded-b border-t border-gray-200 dark:border-gray-600">
              <button data-modal-toggle="defaultModal" type="submit"
                class="text-white bg-teal-500 hover:bg-teal-700 focus:ring-4 focus:ring-teal-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center">
                Submit
              </button>
              <button data-modal-toggle="defaultModal" type="button"
                class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:ring-gray-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10"
                @click="this.modalIsHidden = !this.modalIsHidden">
                Cancel
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div class="flex flex-col place-items-center border-b-2">
      <img :src="'/uploads/' + this.postBySlug.featuredImage" class="w-full my-5" />
      <h1 class="text-center text-5xl font-extrabold mb-5">{{ this.postBySlug.title || null }}</h1>
      <p class="text-gray-500 text-lg mb-2">{{ formatDate(this.postBySlug.createdAt) }} - By {{
          this.postBySlug.user.username }}</p>
    </div>

    <div class="flex flex-wrap my-4">
      <div class="mr-5 text-sm font-medium"> Tags:</div>
      <router-link v-for="tag in this.postBySlug.tag" :key="tag.name"
        class="mr-5 text-sm font-medium uppercase text-teal-500 hover:underline hover:text-teal-7000"
        :to="`/tag/${tag.slug}`">
        {{ tag.name }}
      </router-link>
    </div>

    <!----Main content-->
    <div class="py-5 font-serif space-y-4">
      <!-- <div v-html="this.postBySlug.content"></div> -->
    </div>

    <!---Like, Comment and Share-->
    <div class="flex flex-wrap py-4 space-x-8 justify-center items-center text-xl">
      <div v-if="this.liked === true" @click="this.updateLike()">
        <i class="fa-solid fa-thumbs-up">
          <span class="font-sans font-semibold ml-1">
            {{ this.numberOfLikes }}
          </span>
        </i>
      </div>
      <div v-else @click="this.updateLike()">
        <i class="fa-solid fa-thumbs-up">
          <span class="font-sans font-semibold ml-1">
            {{ this.numberOfLikes }}
          </span>
        </i>
      </div>
      <div @click="this.toggleCommentSection()">
        <i class="fa-regular fa-comment-dots">
          <span class="font-sans font-semibold ml-1">
            {{ this.numberOfApprovedComments }}</span>
        </i>
      </div>
      <div id="socialShareIcon" @click="this.toggleSocialSharePopover()">
        <i class="fa-solid fa-share-nodes"></i>
      </div>
      <div id="socialShare">
        <div v-if="this.showSocialShare" class="flex space-x-2 drop-shadow-lg border-2 p-2">
          <i class="fa-brands fa-linkedin text-3xl text-gray-700 hover:text-teal-700"></i>
          <i class="fa-brands fa-facebook-square text-3xl text-gray-700 hover:text-teal-700"></i>
          <i class="fa-brands fa-twitter-square text-3xl text-gray-700 hover:text-teal-700"></i>
          <i class="fa-brands fa-google-plus-square text-3xl text-gray-700 hover:text-teal-700"></i>
          <i class="fa-brands fa-github-square text-3xl text-gray-700 hover:text-teal-700"></i>
          <i class="fa-brands fa-dev text-3xl text-gray-700 hover:text-teal-700"></i>
        </div>
      </div>
    </div>

    <!--Comment Section-->
    <!--Pass the approved comments and the post id to the comment component-->
    <comment-section-component v-if="this.approvedComments && this.showComment" :comments="this.approvedComments"
      :postID="this.postBySlug.id" :userID="this.userID"></comment-section-component>
  </div>
</template>

<script>
import { POST_BY_SLUG } from "@/queries";
import CommentSectionComponent from "@/components/CommentSection.vue";
import { UPDATE_POST_LIKE } from "@/mutations";
import { createPopper } from "@popperjs/core";

export default {
  name: "PostView",
  components: { CommentSectionComponent },

  data() {
    return {
      // this is temporary
      postBySlug: {
        title: null,
        featuredImage: null,
        user: {
          username: null
        }
      },
      // postBySlug: null, // this is original needs to check later
      modalIsHidden: true,
      post:{
        title:null,
        slug:null,
        featuredImage:null,
        content: null,
        isPublished:null,
        isFeatured:null
      },
      comments: null,
      liked: false,
      numberOfLikes: 0,
      userID: null,
      showComment: false,
      showSocialShare: false
    }
  },
  computed: {
    approvedComments() {
      // return this.comments.filter((comment) => comment.isApproved);
    },
    numberOfApprovedComments() {
      // return Objects.keys(this.approvedComments).length;
    }
  },

  async created() {
    try {
      const post = await this.$apollo.query({
        query: POST_BY_SLUG,
        variables: {
          // slug:this.$route.params.slug,
          slug: "hello"
        }
      });
      console.log("asfasdfasdfasdf")
      this.postBySlug = post.data.postBySlug;
      this.comments = post.data.postBySlug.commentSet;

      // Check if the current user has liked the post
      // Get the current user id
      this.userID = JSON.parse(localStorage.getItem("user")).id;

      // Find if the current user has liked the post
      let likedUsers = this.postBySlug.likes;

      for (let likedUser in likedUsers) {
        if (likedUsers[likedUser].id === this.userID) {
          this.liked = true;
        }
      }

      // Get the number of likes
      this.numberOfLikes = parseInt(this.postBySlug.numberOfLikes)
    } catch (error) {
      console.log(error.message)
    }
  },
  mounted() {
    const socialShareIcon = document.querySelector("#socialShareIcon");
    const socialShare = document.querySelector("#socialShare");
    createPopper(socialShareIcon, socialShare, {
      placement: "right",
      modifiers: [
        {
          name: "offset",
          options: {
            offset: [-10, 20],
          },
        },
      ],
    });
  },

  methods: {
    createPost(){
    },
    updateSlug(event){
      console.log("asdfasdfasfasfasdf")
      console.log(event.keyCode) // 189 for - and 32 for space
      if(event.keyCode === 32){
        console.log("space is clicked")
        this.post.slug=(this.post.title).trim()
      }else{
        this.post.slug=this.post.title
      }
      
    },
    formatDate(x) {
      let date = new Date(x);
      var month = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
      ][date.getMonth()];
      return month + " " + date.getDate() + ", " + date.getFullYear();
    },
    updateLike() {
      if (this.liked === true) {
        this.numberOfLikes = this.numberOfLikes - 1;
      } else {
        this.numberOfLikes = this.numberOfLikes + 1;
      }
      this.liked = !this.liked;

      this.$apollo.mutate({
        mutation: UPDATE_POST_LIKE,
        variables: {
          postID: this.postBySlug.id,
          userID: this.userID,
        },
      });
    },
    toggleCommentSection() {
      this.showComment = !this.showComment;
    },
    toggleSocialSharePopover() {
      this.showSocialShare = !this.showSocialShare;
    },
  },
}
</script>