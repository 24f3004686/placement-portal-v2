<template>

  <!-- NAVBAR -->

  <nav class="navbar navbar-expand-lg navbar-dark bg-dark px-4">

    <a class="navbar-brand fw-bold" href="#">
      Placement Portal
    </a>

    <div class="navbar-nav ms-auto">

      <button
        class="btn btn-outline-light me-2"
        @click="currentPage = 'login'"
      >
        Login
      </button>

      <button
        class="btn btn-outline-info me-2"
        @click="currentPage = 'student-register'"
      >
        Student
      </button>

      <button
        class="btn btn-outline-warning me-2"
        @click="currentPage = 'company-register'"
      >
        Company
      </button>

      <button
        class="btn btn-danger"
        @click="logout"
      >
        Logout
      </button>

    </div>

  </nav>


  <!-- PAGES -->

  <Login
    v-if="currentPage === 'login'"
    @change-page="changePage"
  />

  <StudentRegister
    v-if="currentPage === 'student-register'"
  />

  <CompanyRegister
    v-if="currentPage === 'company-register'"
  />

  <AdminDashboard
    v-if="currentPage === 'admin'"
  />

  <StudentDashboard
    v-if="currentPage === 'student'"
  />

  <CompanyDashboard
    v-if="currentPage === 'company'"
  />

</template>

<script>

import Login from '../components/Login.vue'

import StudentRegister from '../components/StudentRegister.vue'

import CompanyRegister from '../components/CompanyRegister.vue'

import AdminDashboard from '../components/AdminDashboard.vue'

import StudentDashboard from '../components/StudentDashboard.vue'

import CompanyDashboard from '../components/CompanyDashboard.vue'

export default {

  components: {

    Login,
    StudentRegister,
    CompanyRegister,
    AdminDashboard,
    StudentDashboard,
    CompanyDashboard

  },

  data() {

    return {

      currentPage: "login"

    }

  },

  methods: {

    changePage(page) {

      this.currentPage = page

    },

    logout() {

      localStorage.removeItem("token")

      this.currentPage = "login"

      alert("Logged Out")

    }

  }

}

</script>

<style>

body {

  background: #f4f7fc;

  font-family: Arial, sans-serif;

}

</style>

