<template>

<div class="container py-5">

  <!-- HEADER -->
  <div class="d-flex justify-content-between align-items-center mb-5">
    <div>
      <h1 class="fw-bold text-dark mb-1">
        <i class="bi bi-mortarboard-fill text-primary me-2"></i>
        Student Dashboard
      </h1>
      <p class="text-muted">
        Discover opportunities, manage your profile and track applications.
      </p>
    </div>
    <button class="btn btn-success px-4" @click="exportCSV">
      <i class="bi bi-download me-2"></i>
      Export CSV
    </button>
  </div>

  <!-- SUMMARY CARDS -->
  <div class="row g-4 mb-5">
    <div class="col-lg-4 col-md-6">
      <div class="card dashboard-card h-100">
        <div class="card-body text-center">
          <i class="bi bi-briefcase-fill display-4 text-warning mb-3"></i>
          <h6 class="text-muted">Available Jobs</h6>
          <h2>{{ jobs.length }}</h2>
        </div>
      </div>
    </div>

    <div class="col-lg-4 col-md-6">
      <div class="card dashboard-card h-100">
        <div class="card-body text-center">
          <i class="bi bi-file-earmark-check-fill display-4 text-primary mb-3"></i>
          <h6 class="text-muted">Applications</h6>
          <h2>{{ applications.length }}</h2>
        </div>
      </div>
    </div>

    <div class="col-lg-4 col-md-12">
      <div class="card dashboard-card h-100">
        <div class="card-body text-center">
          <i class="bi bi-bell-fill display-4 text-danger mb-3"></i>
          <h6 class="text-muted">Notifications</h6>
          <h2>{{ notifications.length }}</h2>
        </div>
      </div>
    </div>
  </div>

  <!-- NOTIFICATIONS -->
  <div v-if="notifications.length" class="card shadow-lg border-0 rounded-4 mb-5">
    <div class="card-body">
      <h4 class="fw-bold mb-4">
        <i class="bi bi-bell-fill text-warning me-2"></i>
        Notifications
      </h4>
      <div v-for="n in notifications" :key="n.id" class="alert alert-warning mb-3">
        <i class="bi bi-megaphone-fill me-2"></i>
        {{ n.message }}
      </div>
    </div>
  </div>

  <!-- PROFILE -->
  <div class="card shadow-lg border-0 rounded-4 mb-5">
    <div class="card-body p-4">
      <h3 class="fw-bold mb-4">
        <i class="bi bi-person-circle text-primary me-2"></i>
        My Profile
      </h3>
      <div class="row">
        <div class="col-md-6 mb-3">
          <label class="form-label fw-semibold">Branch</label>
          <input v-model="profile.branch" class="form-control shadow-sm" placeholder="Computer Science">
        </div>

        <div class="col-md-6 mb-3">
          <label class="form-label fw-semibold">CGPA</label>
          <input v-model="profile.cgpa" class="form-control shadow-sm" placeholder="9.20">
        </div>

        <div class="col-md-6 mb-3">
          <label class="form-label fw-semibold">Graduation Year</label>
          <input v-model="profile.graduation_year" class="form-control shadow-sm" placeholder="2027">
        </div>

        <div class="col-md-6 mb-3">
          <label class="form-label fw-semibold">Skills</label>
          <input v-model="profile.skills" class="form-control shadow-sm" placeholder="Python, Flask, Vue">
        </div>

        <div class="col-12 mb-4">
          <label class="form-label fw-semibold">Resume Link</label>
          <input v-model="profile.resume" class="form-control shadow-sm" placeholder="https://...">
        </div>
      </div>
      <button class="btn btn-primary px-4" @click="updateProfile">
        <i class="bi bi-floppy-fill me-2"></i>
        Update Profile
      </button>
    </div>
  </div>

  <!-- AVAILABLE JOBS -->
  <div class="card shadow-lg border-0 rounded-4 mb-5">
    <div class="card-body">
      <h3 class="fw-bold mb-4">
        <i class="bi bi-briefcase-fill text-success me-2"></i>
        Available Jobs
      </h3>
      <div class="table-responsive">
        <table class="table table-hover align-middle">
          <thead class="table-dark">
            <tr>
              <th>ID</th>
              <th>Job Title</th>
              <th>Skills</th>
              <th>Salary</th>
              <th>Apply</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="job in jobs" :key="job.id">
              <td>{{ job.id }}</td>
              <td class="fw-semibold">{{ job.title }}</td>
              <td>{{ job.skills_required }}</td>
              <td>{{ job.salary }}</td>
              <td>
                <button class="btn btn-success btn-sm rounded-pill" @click="applyJob(job.id)">
                  <i class="bi bi-send-fill me-1"></i>
                  Apply
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- MY APPLICATIONS -->
  <div class="card shadow-lg border-0 rounded-4">
    <div class="card-body">
      <div class="d-flex justify-content-between align-items-center mb-4">
        <h3 class="fw-bold">
          <i class="bi bi-file-earmark-check-fill text-primary me-2"></i>
          My Applications
        </h3>
        <span class="badge bg-primary fs-6 px-3 py-2">
          {{ applications.length }} Applications
        </span>
      </div>

      <div class="table-responsive">
        <table class="table table-hover align-middle">
          <thead class="table-dark">
            <tr>
              <th>Job</th>
              <th>Status</th>
              <th>Progress</th>
              <th>Interview</th>
              <th>Feedback</th>
              <th>Offer Letter</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="app in applications" :key="app.id">
              <!-- Job -->
              <td class="fw-semibold">
                <i class="bi bi-briefcase-fill text-primary me-2"></i>
                {{ app.job_title }}
              </td>

              <!-- Status -->
              <td>
                <span v-if="app.status==='Placed'" class="badge rounded-pill bg-success">
                  <i class="bi bi-award-fill me-1"></i>
                  Placed
                </span>
                <span v-else-if="app.status==='Offer'" class="badge rounded-pill bg-warning text-dark">
                  <i class="bi bi-envelope-fill me-1"></i>
                  Offer
                </span>
                <span v-else-if="app.status==='Rejected'" class="badge rounded-pill bg-danger">
                  <i class="bi bi-x-circle-fill me-1"></i>
                  Rejected
                </span>
                <span v-else-if="app.status==='Shortlisted'" class="badge rounded-pill bg-primary">
                  <i class="bi bi-check-circle-fill me-1"></i>
                  Shortlisted
                </span>
                <span v-else-if="app.status==='Selected'" class="badge rounded-pill bg-warning text-dark">
                  <i class="bi bi-star-fill me-1"></i>
                  Selected
                </span>
                <span v-else-if="app.status==='Interview Scheduled'" class="badge rounded-pill bg-info">
                  <i class="bi bi-calendar-event-fill me-1"></i>
                  Interview
                </span>
                <span v-else class="badge rounded-pill bg-secondary">
                  {{ app.status }}
                </span>
              </td>

              <!-- Progress -->
              <td style="min-width:180px;">
                <div class="progress" style="height:10px;">
                  <div class="progress-bar" :style="{
                    width:
                    app.status==='Applied' ? '20%' :
                    app.status==='Shortlisted' ? '40%' :
                    app.status==='Interview Scheduled' ? '60%' :
                    app.status==='Selected' ? '80%' :
                    app.status==='Offer' ? '90%' :
                    app.status==='Placed' ? '100%' :
                    '10%'
                  }">
                  </div>
                </div>
              </td>

              <!-- Interview -->
              <td>
                <span v-if="app.interview_date">
                  <i class="bi bi-calendar3 me-1 text-primary"></i>
                  {{ app.interview_date }}
                </span>
                <span v-else class="text-muted">—</span>
              </td>

              <!-- Feedback -->
              <td>
                <span v-if="app.feedback">{{ app.feedback }}</span>
                <span v-else class="text-muted">Waiting...</span>
              </td>

              <!-- Offer -->
              <td>
                <button v-if="app.status==='Selected' || app.status==='Offer' || app.status==='Placed'" 
                  class="btn btn-success btn-sm rounded-pill" @click="downloadOffer(app.id)">
                  <i class="bi bi-download me-1"></i>
                  Download
                </button>
                <span v-else class="text-muted">—</span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <ATSChecker />

</div> <!-- Close main container -->

</template>

<script>

import axios from "axios"
import ATSChecker from "./ATSChecker.vue"


export default {

  components: {
    ATSChecker
  },

  data() {

    return {

      profile: {},

      jobs: [],

      applications: [],

      notifications: []

    }

  },

  async mounted() {

    await this.loadProfile()

    await this.fetchJobs()

    await this.fetchApplications()

    await this.fetchNotifications()

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

    async fetchNotifications() {

      try {

        const token =
          localStorage.getItem("token")

        const headers = {

          Authorization:
            `Bearer ${token}`

        }

        const response =
          await axios.get(

            "http://127.0.0.1:5000/student/notifications",

            { headers }

          )

        this.notifications =
          response.data

        if (
          this.notifications.length > 0
        ) {

          alert(
            this.notifications[0].message
          )

        }

      }

      catch(error) {

        console.log(error)

      }

    },

    async exportCSV() {

      const token =
        localStorage.getItem("token")

      const headers = {

        Authorization:
          `Bearer ${token}`

      }

      await axios.post(
  
        "http://127.0.0.1:5000/student/export-csv",

        {},

        { headers }

      )

      alert(
        "CSV export started"
      )

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
