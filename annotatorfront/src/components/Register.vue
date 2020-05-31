<template>
  <div style="align:center">
    <h1>User Registration</h1>
    <b-form :style="{ width: 150 + 'px', margin: 'auto !important' }" @submit="CreateUser">
      <b-form-group id="username" label="Username:" label-for="username">
        <b-form-input
          id="username"
          type="username"
          v-model="username"
          required
          placeholder="Enter name"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="password" label="Password:" label-for="password">
        <b-form-input
          id="password"
          type="password"
          v-model="password"
          required
          placeholder="Enter Password"
        ></b-form-input>
      </b-form-group>
      <b-button type="submit" value="Submit" variant="outline-primary">Button</b-button>
    </b-form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "register",
  components: {},
  data() {
    return {
      username: null,
      password: null
    };
  },
  methods: {
    CreateUser() {
      console.log(this.username);
      axios
        .post("http://127.0.0.1:8000/api/users/", {
          username: this.username,
          password: this.password
        })
        .then(res => console.log(res))
        .catch(err => console.log(err));
      this.$router.push("/");
    }
  },

  created() {
    let token = localStorage.getItem("user-token") || null;
    if (token !== null) {
      this.$router.push("/");
    }
  }
};
</script>
