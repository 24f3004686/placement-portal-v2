<template>

  <div class="container mt-5">

    <h1 class="mb-4 text-danger fw-bold">
      Admin Dashboard
    </h1>


    <!-- STATS -->

    <div class="row mb-5">

      <div class="col-md-3">

        <div class="card shadow border-0 p-4 text-center rounded-4">

          <h5>Total Students</h5>

          <h2>{{ stats.students }}</h2>

        </div>

      </div>


      <div class="col-md-3">

        <div class="card shadow border-0 p-4 text-center rounded-4">

          <h5>Total Companies</h5>

          <h2>{{ stats.companies }}</h2>

        </div>

      </div>


      <div class="col-md-3">

        <div class="card shadow border-0 p-4 text-center rounded-4">

          <h5>Total Jobs</h5>

          <h2>{{ stats.jobs }}</h2>

        </div>

      </div>


      <div class="col-md-3">

        <div class="card shadow border-0 p-4 text-center rounded-4">

          <h5>Applications</h5>

          <h2>{{ stats.applications }}</h2>

        </div>

      </div>

    </div>


    <!-- COMPANIES -->

    <div class="card shadow border-0 p-4 mb-5 rounded-4">

      <h3 class="mb-4">
        Companies
      </h3>

      <table class="table table-hover">

        <thead>

          <tr>

            <th>ID</th>

            <th>Company Name</th>

            <th>Status</th>

            <th>Actions</th>

          </tr>

        </thead>

        <tbody>

          <tr
            v-for="company in companies"
            :key="company.id"
          >

            <td>{{ company.id }}</td>

            <td>{{ company.company_name }}</td>

            <td>

              <span
                v-if="company.approved"
                class="badge bg-success"
              >
                Approved
              </span>

              <span
                v-else
                class="badge bg-warning text-dark"
              >
                Pending
              </span>

            </td>

            <td>

              <button
                class="btn btn-success btn-sm me-2"
                @click="approveCompany(company.id)"
              >
                Approve
              </button>

              <button
                class="btn btn-danger btn-sm"
                @click="deleteCompany(company.id)"
              >
                Delete
              </button>

            </td>

          </tr>

        </tbody>

      </table>

    </div>


    <!-- STUDENTS -->

    <div class="card shadow border-0 p-4 rounded-4">

      <h3 class="mb-4">
        Students
      </h3>

      <table class="table table-hover">

        <thead>

          <tr>

            <th>ID</th>

            <th>Name</th>

          </tr>

        </thead>

        <tbody>

          <tr
            v-for="student in students"
            :key="student.id"
          >

            <td>{{ student.id }}</td>

            <td>{{ student.full_name }}</td>

          </tr>

        </tbody>

      </table>

    </div>

  </div>

</template>


<script>

import axios from "axios"

export default {

  data() {

    return {

      stats: {},

      companies: [],

      students: []

    }

  },

  async mounted() {

    await this.fetchDashboardData()

  },

  methods: {

    async fetchDashboardData() {

      try {

        const token = localStorage.getItem("token")

        const headers = {

          Authorization: `Bearer ${token}`

        }


        // STATS

        const statsResponse = await axios.get(

          "http://127.0.0.1:5000/admin/stats",

          { headers }

        )

        this.stats = statsResponse.data


        // COMPANIES

        const companiesResponse = await axios.get(

          "http://127.0.0.1:5000/admin/companies",

          { headers }

        )

        this.companies = companiesResponse.data


        // STUDENTS

        const studentsResponse = await axios.get(

          "http://127.0.0.1:5000/admin/students",

          { headers }

        )

        this.students = studentsResponse.data

      }

      catch(error) {

        console.log(error)

        alert("Failed to load dashboard")

      }

    },


    async approveCompany(id) {

      try {

        const token = localStorage.getItem("token")

        const headers = {

          Authorization: `Bearer ${token}`

        }

        await axios.put(

          `http://127.0.0.1:5000/admin/approve-company/${id}`,

          {},

          { headers }

        )

        alert("Company Approved")

        await this.fetchDashboardData()

      }

      catch(error) {

        console.log(error)

        alert("Approval failed")

      }

    },


    async deleteCompany(id) {

      try {

        const token = localStorage.getItem("token")

        const headers = {

          Authorization: `Bearer ${token}`

        }

        await axios.delete(

          `http://127.0.0.1:5000/admin/delete-company/${id}`,

          { headers }

        )

        alert("Company Deleted")

        await this.fetchDashboardData()

      }

      catch(error) {

        console.log(error)

        alert("Delete failed")

      }

    }

  }

}

</script>