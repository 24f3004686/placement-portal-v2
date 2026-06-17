<template>

<div class="container py-5">

  <div class="d-flex justify-content-between align-items-center mb-4">

    <h1 class="fw-bold text-primary">
      <i class="bi bi-speedometer2 me-2"></i>
      Admin Dashboard
    </h1>

    <button
      class="btn btn-primary"
      @click="generateReport"
    >
      <i class="bi bi-download me-2"></i>
      Monthly Report
    </button>

  </div>

  <!-- Dashboard Cards -->

  <div class="row g-4 mb-5">

    <div class="col-lg-3 col-md-6">

      <div class="card dashboard-card shadow-sm border-0 h-100">

        <div class="card-body text-center">

          <i class="bi bi-mortarboard-fill display-4 text-primary mb-3"></i>

          <h6 class="text-muted">Students</h6>

          <h2>{{ stats.students }}</h2>

        </div>

      </div>

    </div>

    <div class="col-lg-3 col-md-6">

      <div class="card dashboard-card shadow-sm border-0 h-100">

        <div class="card-body text-center">

          <i class="bi bi-building display-4 text-success mb-3"></i>

          <h6 class="text-muted">Companies</h6>

          <h2>{{ stats.companies }}</h2>

        </div>

      </div>

    </div>

    <div class="col-lg-3 col-md-6">

      <div class="card dashboard-card shadow-sm border-0 h-100">

        <div class="card-body text-center">

          <i class="bi bi-briefcase-fill display-4 text-warning mb-3"></i>

          <h6 class="text-muted">Jobs</h6>

          <h2>{{ stats.jobs }}</h2>

        </div>

      </div>

    </div>

    <div class="col-lg-3 col-md-6">

      <div class="card dashboard-card shadow-sm border-0 h-100">

        <div class="card-body text-center">

          <i class="bi bi-file-earmark-check-fill display-4 text-danger mb-3"></i>

          <h6 class="text-muted">Applications</h6>

          <h2>{{ stats.applications }}</h2>

        </div>

      </div>

    </div>

  </div>

  <div class="row g-4 mb-5">
   
    <div class="col-lg-8">

      <ApplicationsChart />

    </div>

    <div class="col-lg-4">

      <StatusChart 
          :stats="placementStats"
      />

    </div>

  </div>

  <!-- Companies -->

  <div class="card shadow-lg border-0 rounded-4 mb-5">

    <div class="card-body">

      <div class="d-flex justify-content-between align-items-center mb-3">

        <h3>
          <i class="bi bi-building me-2"></i>
          Companies
        </h3>

        <input
          v-model="companySearch"
          class="form-control w-25"
          placeholder="Search company..."
        >

      </div>

      <table class="table table-hover align-middle">

        <thead class="table-light">

          <tr>

            <th>ID</th>

            <th>Company</th>

            <th>Status</th>

            <th>Actions</th>

          </tr>

        </thead>

        <tbody>

          <tr
            v-for="company in filteredCompanies"
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
                class="badge bg-warning"
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

  </div>

  <!-- Students -->

  <div class="card shadow-lg border-0 rounded-4">

    <div class="card-body">

      <div class="d-flex justify-content-between align-items-center mb-3">

        <h3>

          <i class="bi bi-people-fill me-2"></i>

          Students

        </h3>

        <input
          v-model="studentSearch"
          class="form-control w-25"
          placeholder="Search student..."
        >

      </div>

      <table class="table table-hover align-middle">

        <thead class="table-light">

          <tr>

            <th>ID</th>

            <th>Name</th>

            <th>Status</th>

            <th>Profile</th>

            <th>Actions</th>

          </tr>

        </thead>

        <tbody>

          <tr
            v-for="student in filteredStudents"
            :key="student.id"
          >

            <td>{{ student.id }}</td>

            <td>{{ student.full_name }}</td>

            <td>

              <span
                v-if="student.approved"
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
                class="btn btn-info btn-sm"
                @click="viewStudent(student)"
              >
                View Profile
              </button>

            </td>

            <td>

              <button
                class="btn btn-success btn-sm me-2"
                @click="approveStudent(student.id)"
              >
                Approve
              </button>

              <button
                class="btn btn-danger btn-sm"
                @click="deactivateStudent(student.id)"
              >
                Deactivate
              </button>

            </td>

          </tr>

        </tbody>

      </table>

    </div>

  </div>

</div>

</template>

<script>

import ApplicationsChart from "./charts/ApplicationsChart.vue"

import StatusChart from "./charts/StatusChart.vue"

import axios from "axios"

export default {

  components: {
    ApplicationsChart,
    StatusChart
  },

  data() {

    return {

      stats: {},

      companies: [],

      students: [],

      applications: [],

      companySearch: "",

      studentSearch: ""

    }

  },

  async mounted() {

    await this.fetchDashboardData()

  },

  computed: {

    filteredCompanies() {

      return this.companies.filter(company =>

        company.company_name
        .toLowerCase()
        .includes(this.companySearch.toLowerCase())

      )

    },

    placementStats() {

        return {

            placed: this.applications.filter(
                a => a.status === "Placed"
            ).length,

            selected: this.applications.filter(
                a => a.status === "Selected"
            ).length,

            rejected: this.applications.filter(
                a => a.status === "Rejected"
            ).length,

            pending: this.applications.filter(
                a =>
                    a.status === "Pending" ||
                    a.status === "Applied" ||
                    a.status === "Shortlisted"
            ).length

        }

    },

    filteredStudents() {

      return this.students.filter(student =>

        student.full_name
        .toLowerCase()
        .includes(this.studentSearch.toLowerCase())

      )

    }
 
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

        // APPLICATIONS

        const applicationsResponse = await axios.get(

            "http://127.0.0.1:5000/admin/applications",
            
            { headers }

        )

        this.applications = applicationsResponse.data

      }

      catch(error) {

        console.log(error)

        alert("Failed to load dashboard")

      }

    },

    async viewStudent(student) {

       alert(

              `Name: ${student.full_name}

              Branch: ${student.branch || "-"}

              CGPA: ${student.cgpa || "-"}

              Graduation Year: ${student.graduation_year || "-"}

              Skills: ${student.skills || "-"}

              Resume: ${student.resume || "-"}`

             )

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

    async approveStudent(id) {

      try {

        const token = localStorage.getItem("token")

        await axios.put(

          `http://127.0.0.1:5000/admin/approve-student/${id}`,

          {},

          {

            headers: {

              Authorization: `Bearer ${token}`

            }

          }

        )

        alert("Student approved")

        await this.fetchDashboardData()

      }

      catch(error) {

        console.log(error)

        alert("Approval failed")

      }

    },

    async deactivateStudent(id) {

      try {

        const token = localStorage.getItem("token")

        await axios.put(

          `http://127.0.0.1:5000/admin/deactivate-student/${id}`,

          {},

          {

            headers: {

              Authorization: `Bearer ${token}`

            }

          }

        )

        alert("Student deactivated")

        await this.fetchDashboardData()

      }

      catch(error) {

        console.log(error)

        alert("Operation failed")

      }

    },


    async generateReport() {

      const token =
        localStorage.getItem("token")

      const headers = {

       Authorization:
         `Bearer ${token}`

      }

      try {

        const response =
          await axios.post(

            "http://127.0.0.1:5000/admin/generate-report",

            {},

            { headers }

          )

        alert(
            response.data.message
        )

    }

    catch(error) {

      console.error(error)

      alert(
          "Report generation failed"
      )

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