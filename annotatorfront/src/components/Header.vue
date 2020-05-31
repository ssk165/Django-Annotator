<template>
  <div class>
    <b-navbar toggleable="lg" type="warning" variant="dark" class="full-width">
      <b-navbar-brand class="text-white" href="#">Annotator</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-navbar-nav class="ml-auto">
        <b-nav-form @submit.prevent="login" v-if="token == null">
          <b-form-input
            id="username"
            size="sm"
            class="mr-sm-2"
            v-model="username"
            placeholder="username"
            name="username"
          ></b-form-input>
          <b-form-input
            id="password"
            size="sm"
            class="mr-sm-2"
            placeholder="password"
            type="password"
            v-model="password"
            name="password"
          ></b-form-input>

          <b-button size="sm" class="my-2 my-sm-0" type="submit" variant="dark">Login</b-button>
        </b-nav-form>
        <b-nav-form @submit.prevent="logout" v-if="token !== null">
          <b-button type="submit" size="sm" class="my-2 ml-2" variant="dark">Logout</b-button>
        </b-nav-form>
        <b-nav-form @submit.prevent="register" v-if="token === null">
          <b-button
            :to="{ name: 'register' }"
            type="submit"
            size="sm"
            class="my-2 ml-2"
            variant="dark"
          >Register</b-button>
        </b-nav-form>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
// @ is an alias to /src

import axios from "axios";

export default {
  name: "Header",
  components: {},
  data() {
    return {
      username: "",
      password: "",
      token: localStorage.getItem("user-token") || null
    };
  },
  methods: {
    login() {
      axios
        .post("http://127.0.0.1:8000/auth/", {
          username: this.username,
          password: this.password
        })
        .then(resp => {
          this.token = resp.data.token;
          console.log(this.token);
          localStorage.setItem("user-token", resp.data.token);
          this.$router.go(0);
        })
        .catch(() => {
          localStorage.removeItem("user-token");
        });
    },
    logout() {
      localStorage.removeItem("user-token");
      this.token = null;
      this.$router.go(0);
    },
    register() {
      console.log("Router");
    }
  },
  created() {
    this.token = localStorage.getItem("user-token") || null;
  }
};
</script>

<style>
.full-width .card-header-tabs {
  margin-right: -21px;
  margin-left: -21px;
}

.full-width .nav-tabs .nav-item {
  margin-bottom: -1px;
  flex-grow: 1;
  text-align: center;
}
</style>
