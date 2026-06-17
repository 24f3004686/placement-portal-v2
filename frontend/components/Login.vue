<template>

  <div class="container py-5">

    <div class="row justify-content-center">

      <div class="col-lg-5 col-md-7">

        <div class="card shadow-lg border-0 rounded-4 p-4">

          <!-- Header -->

          <div class="d-flex justify-content-between align-items-center mb-4">

            <button
              class="btn btn-outline-primary"
              @click="$emit('change-page', 'landing')"
            >
              <i class="bi bi-house-door-fill me-2"></i>
              Home
            </button>

            <h2 class="fw-bold m-0">
              Login
            </h2>

            <div style="width:90px"></div>

          </div>

          <!-- Email -->

          <div class="mb-3">

            <label class="form-label fw-semibold">

              Email

            </label>

            <input
              v-model="email"
              type="email"
              class="form-control"
              placeholder="Enter your email"
            >

          </div>

          <!-- Password -->

          <div class="mb-4">

            <label class="form-label fw-semibold">

              Password

            </label>

            <input
              v-model="password"
              type="password"
              class="form-control"
              placeholder="Enter your password"
            >

          </div>

          <!-- Login -->

          <button
            class="btn btn-primary w-100 py-2 fw-semibold"
            @click="login"
          >

            <i class="bi bi-box-arrow-in-right me-2"></i>

            Login

          </button>

          <!-- Register Links -->

          <hr class="my-4">

          <p class="text-center text-muted mb-3">

            New to Placement Portal?

          </p>

          <div class="d-grid gap-2">

            <button
              class="btn btn-outline-success"
              @click="$emit('change-page', 'student-register')"
            >
              <i class="bi bi-person-plus-fill me-2"></i>
              Student Registration
            </button>

            <button
              class="btn btn-outline-warning"
              @click="$emit('change-page', 'company-register')"
            >
              <i class="bi bi-building-add me-2"></i>
              Company Registration
            </button>

          </div>

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