<template>

  <div class="container mt-5">

    <h1 class="text-primary fw-bold mb-4">
      Student Dashboard
    </h1>

    <!-- PROFILE -->

    <div class="card shadow p-4 mb-5">

      <h3>My Profile</h3>

      <input
        v-model="profile.branch"
        class="form-control mb-3"
        placeholder="Branch"
      >

      <input
        v-model="profile.cgpa"
        class="form-control mb-3"
        placeholder="CGPA"
      >

      <input
        v-model="profile.graduation_year"
        class="form-control mb-3"
        placeholder="Graduation Year"
      >

      <input
        v-model="profile.skills"
        class="form-control mb-3"
        placeholder="Skills"
      >

      <input
        v-model="profile.resume"
        class="form-control mb-3"
        placeholder="Resume Link"
      >

      <button
        class="btn btn-primary"
        @click="updateProfile"
      >
        Update Profile
      </button>

    </div>

    <!-- AVAILABLE JOBS -->

    <div class="card shadow p-4 mb-5">

      <h3 class="mb-3">
        Available Jobs
      </h3>

      <table class="table">

        <thead>

          <tr>

            <th>ID</th>

            <th>Title</th>

            <th>Skills</th>

            <th>Salary</th>

            <th>Apply</th>

          </tr>

        </thead>

        <tbody>

          <tr
            v-for="job in jobs"
            :key="job.id"
          >

            <td>{{ job.id }}</td>

            <td>{{ job.title }}</td>

            <td>{{ job.skills_required }}</td>

            <td>{{ job.salary }}</td>

            <td>

              <button
                class="btn btn-success btn-sm"
                @click="applyJob(job.id)"
              >
                Apply
              </button>

            </td>

          </tr>

        </tbody>

      </table>

    </div>

    <!-- APPLICATIONS -->

    <div class="card shadow p-4">

      <h3 class="mb-3">
        My Applications
      </h3>

      <table class="table">

        <thead>

          <tr>

            <th>Job Title</th>

            <th>Status</th>

            <th>Interview Date</th>

            <th>Feedback</th>

            <th>Offer Letter</th>

          </tr>

        </thead>

        <tbody>

          <tr
            v-for="app in applications"
            :key="app.id"
          >

            <td>{{ app.job_title }}</td>

            <td>

              <span
                v-if="app.status === 'Placed'"
                class="badge bg-success"
              >
                Placed
              </span>

              <span
                v-else-if="app.status === 'Offer'"
                class="badge bg-warning text-dark"
              >
                Offer
              </span>

              <span
                v-else-if="app.status === 'Rejected'"
                class="badge bg-danger"
              >
                Rejected
              </span>

              <span
                v-else-if="app.status === 'Shortlisted'"
                class="badge bg-primary"
              >
                Shortlisted
              </span>

              <span
                v-else
                class="badge bg-info"
              >
                {{ app.status }}
              </span>

            </td>

            <td>

              {{ app.interview_date || "-" }}

            </td>

            <td>

              {{ app.feedback || "-" }}

            </td>

            <td>

              <button
                v-if="
                  app.status === 'Selected' ||
                  app.status === 'Offer' ||
                  app.status === 'Placed'
                "
                class="btn btn-success btn-sm"
                @click="downloadOffer(app.id)"
              >
                Offer Letter
              </button>

              <span v-else>
                -
              </span>

            </td>

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

      profile: {},

      jobs: [],

      applications: []

    }

  },

  async mounted() {

    await this.loadProfile()

    await this.fetchJobs()

    await this.fetchApplications()

  },

  methods: {

    async loadProfile() {

      const token = localStorage.getItem("token")

      const headers = {

        Authorization: `Bearer ${token}`

      }

      const response = await axios.get(

        "http://127.0.0.1:5000/student/profile",

        { headers }

      )

      this.profile = response.data

    },

    async updateProfile() {

      const token = localStorage.getItem("token")

      const headers = {

        Authorization: `Bearer ${token}`

      }

      await axios.put(

        "http://127.0.0.1:5000/student/profile",

        this.profile,

        { headers }

      )

      alert("Profile Updated")

    },

    async fetchJobs() {

      const token = localStorage.getItem("token")

      const headers = {

        Authorization: `Bearer ${token}`

      }

      const response = await axios.get(

        "http://127.0.0.1:5000/student/jobs",

        { headers }

      )

      this.jobs = response.data

    },

    async applyJob(jobId) {

      const token = localStorage.getItem("token")

      const headers = {

        Authorization: `Bearer ${token}`

      }

      try {

        await axios.post(

          `http://127.0.0.1:5000/student/apply/${jobId}`,

          {},

          { headers }

        )

        alert("Application Submitted")

        await this.fetchApplications()

      }

      catch(error) {

        alert("Already Applied")

      }

    },

    async fetchApplications() {

      const token = localStorage.getItem("token")

      const headers = {

        Authorization: `Bearer ${token}`

      }

      const response = await axios.get(

        "http://127.0.0.1:5000/student/applications",

        { headers }

      )

      this.applications = response.data

    },

    async downloadOffer(id) {

      try {

        const token = localStorage.getItem("token")

        const headers = {

          Authorization: `Bearer ${token}`

        }

        const response = await axios.get(

          `http://127.0.0.1:5000/student/offer-letter/${id}`,

          { headers }

        )

        alert(
          JSON.stringify(
            response.data,
            null,
            2
          )
        )

      }

      catch(error) {

        alert("Offer Letter Not Available")

      }

    }

  }

}

</script>
