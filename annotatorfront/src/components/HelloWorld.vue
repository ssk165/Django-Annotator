<template>
  <div>
    <h1 v-if="token === null">Welcome to Annotator!</h1>
    <div v-for="item in items" :key="item.id">
      <div v-if="token !== null" class="card">
        <vuetify-audio :file="item.url" downloadable></vuetify-audio>
        <b-button
          type="submit"
          size="sm"
          variant="dark"
          @click="item.showExtra = !item.showExtra"
        >Add Annotation</b-button>
        <div v-show="item.showExtra">
          <b-form-textarea
            id="textarea-large"
            size="lg"
            v-model="item.annotation"
            placeholder="Enter Annotation after listening to audio!"
            :readonly="item.readonly"
          ></b-form-textarea>
          <div class="submitbutton">
            <b-button
              type="submit"
              size="md"
              variant="dark"
              @click="item.showExtra = !item.showExtra"
              v-show="item.editbutton"
            >Cancel</b-button>
            <b-button
              type="submit"
              size="md"
              variant="dark"
              @click="postAnnotation(item)"
              v-show="item.editbutton"
            >Submit</b-button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import "vuetify/dist/vuetify.min.css";
import "material-design-icons-iconfont/dist/material-design-icons.css";
import axios from "axios";

export default {
  name: "HelloWorld",
  components: {
    VuetifyAudio: () => import("vuetify-audio")
  },
  data() {
    return {
      token: localStorage.getItem("user-token") || null,
      items: [
        {
          url: require("../assets/audios/1.mp3"),
          id: "1",
          showExtra: false,
          readonly: false,
          annotation: "",
          editbutton: true
        },
        {
          url: require("../assets/audios/2.mp3"),
          id: "2",
          showExtra: false,
          readonly: false,
          annotation: "",
          editbutton: true
        },
        {
          url: require("../assets/audios/3.mp3"),
          id: "3",
          showExtra: false,
          readonly: false,
          annotation: "",
          editbutton: true
        },
        {
          url: require("../assets/audios/4.mp3"),
          id: "4",
          showExtra: false,
          readonly: false,
          annotation: "",
          editbutton: true
        },
        {
          url: require("../assets/audios/1.mp3"),
          id: "5",
          showExtra: false,
          readonly: false,
          annotation: "",
          editbutton: true
        },
        {
          url: require("../assets/audios/2.mp3"),
          id: "6",
          showExtra: false,
          readonly: false,
          annotation: "",
          editbutton: true
        },
        {
          url: require("../assets/audios/3.mp3"),
          id: "7",
          showExtra: false,
          readonly: false,
          annotation: "",
          editbutton: true
        },
        {
          url: require("../assets/audios/4.mp3"),
          id: "8",
          showExtra: false,
          readonly: false,
          annotation: "",
          editbutton: true
        }
      ],
      annotationData: []
    };
  },
  methods: {
    getAnnotation() {
      let axiosConfig = {
        headers: {
          Authorization: "Token " + this.token
        }
      };
      axios
        .get("http://127.0.0.1:8000/api/annotation/", axiosConfig)
        .then(res => {
          this.annotationData = res;
          console.log(this.annotationData);
          this.annotationData.data.forEach(element => {
            this.items.forEach(item => {
              if (item.id == element.integer) {
                if (element.annotation.length > 1) {
                  item.annotation = element.annotation;
                  item.readonly = true;
                  item.editbutton = false;
                }
              }
            });
          });
        })
        .catch(err => console.log(err));
    },
    postAnnotation(item) {
      let token = this.token;
      let axiosConfig = {
        headers: {
          Authorization: "Token " + token,
          "Content-Type": "application/json"
        }
      };
      let postData = new FormData();
      postData.set("user", 1);
      postData.set("integer", item.id);
      postData.set("annotation", item.annotation);
      axios
        .post("http://localhost:8000/api/annotation/", postData, axiosConfig)
        .then(() => {
          this.$router.go(0);
        })
        .catch(err => console.log(err));
    }
  },
  created() {
    this.getAnnotation();
  }
};
</script>

<style scoped>
.card {
  width: 500px;
  margin: auto;
  margin-bottom: 10px;
}

.submitbutton {
  display: flex;
  justify-content: space-around;
  width: 100%;
}
</style>
