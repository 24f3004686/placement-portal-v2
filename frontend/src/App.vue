<template>

  <!-- NAVBAR -->

  <nav class="navbar navbar-expand-lg navbar-dark shadow-sm custom-navbar sticky-top">

    <div class="container">

      <!-- Logo -->

      <a
        class="navbar-brand fw-bold fs-4 d-flex align-items-center"
        href="#"
      >
        <i class="bi bi-mortarboard-fill me-2 text-warning"></i>
        Placement Portal
      </a>

      <!-- Mobile Toggle -->

      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbar"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- Navbar -->

      <div
        class="collapse navbar-collapse"
        id="navbar"
      >

        <ul class="navbar-nav ms-auto align-items-lg-center">

          <!-- LANDING PAGE -->

          <template v-if="currentPage === 'landing'">

            <li class="nav-item mx-1">

              <button
                class="btn btn-primary nav-btn"
                @click="changePage('login')"
              >
                <i class="bi bi-box-arrow-in-right me-1"></i>
                Login
              </button>

            </li>

            <li class="nav-item mx-1">

              <button
                class="btn btn-outline-light nav-btn"
                @click="changePage('student-register')"
              >
                <i class="bi bi-person-plus-fill me-1"></i>
                Student Register
              </button>

            </li>

            <li class="nav-item mx-1">

              <button
                class="btn btn-outline-warning nav-btn"
                @click="changePage('company-register')"
              >
                <i class="bi bi-building-add me-1"></i>
                Company Register
              </button>

            </li>

          </template>

          <!-- ADMIN -->

          <template v-if="currentPage === 'admin'">

            <li class="nav-item me-3">

              <span class="navbar-text text-white fw-semibold">

                <i class="bi bi-speedometer2 me-2"></i>

                Admin Dashboard

              </span>

            </li>

          </template>

          <!-- STUDENT -->

          <template v-if="currentPage === 'student'">

            <li class="nav-item me-3">

              <span class="navbar-text text-white fw-semibold">

                <i class="bi bi-person-workspace me-2"></i>

                Student Dashboard

              </span>

            </li>

          </template>

          <!-- COMPANY -->

          <template v-if="currentPage === 'company'">

            <li class="nav-item me-3">

              <span class="navbar-text text-white fw-semibold">

                <i class="bi bi-building me-2"></i>

                Company Dashboard

              </span>

            </li>

          </template>

          <!-- LOGOUT -->

          <li
            v-if="
              currentPage === 'admin' ||
              currentPage === 'student' ||
              currentPage === 'company'
            "
            class="nav-item"
          >

            <button
              class="btn btn-danger logout-btn"
              @click="logout"
            >

              <i class="bi bi-box-arrow-right me-1"></i>

              Logout

            </button>

          </li>

        </ul>

      </div>

    </div>

  </nav>

  <!-- PAGES -->

  <LandingDashboard
    v-if="currentPage === 'landing'"
  />

  <Login
    v-if="currentPage === 'login'"
    @change-page="changePage"
  />

  <StudentRegister
    v-if="currentPage === 'student-register'"
    @change-page="changePage"
  />

  <CompanyRegister
    v-if="currentPage === 'company-register'"
    @change-page="changePage"
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

import LandingDashboard from "../components/LandingDashboard.vue"

export default {

  components: {

    Login,
    StudentRegister,
    CompanyRegister,
    AdminDashboard,
    StudentDashboard,
    LandingDashboard,
    CompanyDashboard

  },

  data() {

    return {

      currentPage: "landing"

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

