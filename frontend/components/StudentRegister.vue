<template>

  <div class="container py-5">

    <div class="row justify-content-center">

      <div class="col-lg-6 col-md-8">

        <div class="card shadow-lg border-0 rounded-4 p-4">

          <!-- Header -->

          <div class="d-flex justify-content-between align-items-center mb-4">

            <button
              class="btn btn-outline-primary"
              @click="$emit('change-page', 'login')"
            >
              <i class="bi bi-arrow-left me-2"></i>
              Back to Login
            </button>

            <h2 class="fw-bold m-0">
              Student Register
            </h2>

            <div style="width:140px"></div>

          </div>

          <!-- Full Name -->

          <div class="mb-3">

            <label class="form-label fw-semibold">
              Full Name
            </label>

            <input
              v-model="full_name"
              class="form-control"
              placeholder="Enter your full name"
            >

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
              placeholder="Create a password"
            >

          </div>

          <!-- Register -->

          <button
            class="btn btn-success w-100 py-2 fw-semibold"
            @click="register"
          >
            <i class="bi bi-person-plus-fill me-2"></i>
            Register
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

      full_name: "",
      email: "",
      password: ""

    }

  },

  methods: {

    async register() {

      try {

        const response = await axios.post(

          "http://127.0.0.1:5000/auth/student/register",

          {

            full_name: this.full_name,
            email: this.email,
            password: this.password

          }

        )

        alert(response.data.message)

      }

      catch(error) {

        alert(error.response.data.message)

      }

    }

  }

}

</script>