<template>

  <div class="container mt-5">

    <h2 class="mb-4">Company Register</h2>

    <input
      v-model="company_name"
      class="form-control mb-3"
      placeholder="Company Name"
    >

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
      class="btn btn-success"
      @click="register"
    >
      Register
    </button>

  </div>

</template>

<script>

import axios from "axios"

export default {

  data() {

    return {

      company_name: "",
      email: "",
      password: ""

    }

  },

  methods: {

    async register() {

      try {

        const response = await axios.post(

          "http://127.0.0.1:5000/auth/company/register",

          {

            company_name: this.company_name,
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