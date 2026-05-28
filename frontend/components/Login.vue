<template>

  <div class="container">

    <div class="row justify-content-center">

      <div class="col-md-6">

        <div class="card shadow-lg mt-5 p-4 border-0 rounded-4">

          <h2 class="text-center mb-4 fw-bold">
            Login
          </h2>

          <input
            v-model="email"
            class="form-control mb-3"
            placeholder="Email"
          >

          <input
            v-model="password"
            type="password"
            class="form-control mb-3"
            placeholder="Password"
          >

          <button
            class="btn btn-primary w-100"
            @click="login"
          >
            Login
          </button>

        </div>

      </div>

    </div>

  </div>

</template>

<script>

import axios from "axios"

export default {

  data() {

    return {

      email: "",
      password: ""

    }

  },

  methods: {

    async login() {

      try {

        const response = await axios.post(

          "http://127.0.0.1:5000/auth/login",

          {

            email: this.email,
            password: this.password

          }

        )

        localStorage.setItem(
          "token",
          response.data.token
        )

        const role = response.data.role

        alert("Login Successful")

        if(role === "admin") {

          this.$emit("change-page", "admin")

        }

        else if(role === "student") {

          this.$emit("change-page", "student")

        }

        else if(role === "company") {

          this.$emit("change-page", "company")

        }

      }

      catch(error) {

        alert(error.response.data.message)

      }

    }

  }

}

</script>