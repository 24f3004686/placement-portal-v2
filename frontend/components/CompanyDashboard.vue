<template>

<div class="container py-5">

  <!-- HEADER -->

  <div class="d-flex justify-content-between align-items-center mb-5">

    <div>

      <h1 class="fw-bold text-dark mb-1">

        <i class="bi bi-building-fill text-warning me-2"></i>

        Company Dashboard

      </h1>

      <p class="text-muted mb-0">

        Manage your job postings and recruit talented students.

      </p>

    </div>

    <span class="badge bg-warning text-dark px-4 py-2 fs-6 rounded-pill">

      <i class="bi bi-patch-check-fill me-2"></i>

      Recruiter Portal

    </span>

  </div>

  <!-- SUMMARY CARDS -->

  <div class="row g-4 mb-5">

    <div class="col-lg-4 col-md-6">

      <div class="card dashboard-card h-100">

        <div class="card-body text-center">

          <i class="bi bi-briefcase-fill display-4 text-warning mb-3"></i>

          <h6 class="text-muted">Jobs Posted</h6>

          <h2 class="fw-bold">{{ jobs.length }}</h2>

        </div>

      </div>

    </div>

    <div class="col-lg-4 col-md-6">

      <div class="card dashboard-card h-100">

        <div class="card-body text-center">

          <i class="bi bi-people-fill display-4 text-primary mb-3"></i>

          <h6 class="text-muted">Applications</h6>

          <h2 class="fw-bold">{{ applications.length }}</h2>

        </div>

      </div>

    </div>

    <div class="col-lg-4 col-md-12">

      <div class="card dashboard-card h-100">

        <div class="card-body text-center">

          <i class="bi bi-award-fill display-4 text-success mb-3"></i>

          <h6 class="text-muted">Placements</h6>

          <h2 class="fw-bold">

            {{ applications.filter(a => a.status === 'Placed').length }}

          </h2>

        </div>

      </div>

    </div>

  </div>

  <!-- CREATE JOB -->

  <div class="card shadow-lg border-0 rounded-4 mb-5">

    <div class="card-body p-4">

      <h3 class="fw-bold mb-4">

        <i class="bi bi-plus-circle-fill text-warning me-2"></i>

        Create New Job

      </h3>

      <div class="row">

        <div class="col-md-6 mb-3">

          <label class="form-label fw-semibold">

            Job Title

          </label>

          <input

            v-model="title"

            class="form-control shadow-sm"

            placeholder="Machine Learning Engineer"

          >

        </div>

        <div class="col-md-6 mb-3">

          <label class="form-label fw-semibold">

            Skills Required

          </label>

          <input

            v-model="skills_required"

            class="form-control shadow-sm"

            placeholder="Python, Flask, SQL"

          >

        </div>

        <div class="col-md-6 mb-3">

          <label class="form-label fw-semibold">

            Salary

          </label>

          <input

            v-model="salary"

            class="form-control shadow-sm"

            placeholder="12 LPA"

          >

        </div>

        <div class="col-md-6 mb-3">

          <label class="form-label fw-semibold">

            Benefits

          </label>

          <input

            v-model="benefits"

            class="form-control shadow-sm"

            placeholder="Health Insurance, Bonus"

          >

        </div>

      </div>

      <button

        class="btn btn-warning px-4 py-2"

        @click="createJob"

      >

        <i class="bi bi-plus-lg me-2"></i>

        Create Job

      </button>

    </div>

  </div>

  <!-- POSTED JOBS -->

  <div class="card shadow-lg border-0 rounded-4 mb-5">

    <div class="card-body">

      <h3 class="fw-bold mb-4">

        <i class="bi bi-briefcase-fill text-primary me-2"></i>

        Posted Jobs

      </h3>

      <div class="table-responsive">

        <table class="table table-hover align-middle">

          <thead class="table-dark">

            <tr>

              <th>ID</th>

              <th>Title</th>

              <th>Skills</th>

              <th>Salary</th>

              <th>Status</th>

              <th>Actions</th>

            </tr>

          </thead>

          <tbody>

            <tr
              v-for="job in jobs"
              :key="job.id"
            >

              <td>{{ job.id }}</td>

              <td class="fw-semibold">{{ job.title }}</td>

              <td>{{ job.skills_required }}</td>

              <td>{{ job.salary }}</td>

              <td>

                <span
                  v-if="job.status === 'Active'"
                  class="badge rounded-pill bg-success"
                >

                  <i class="bi bi-check-circle-fill me-1"></i>

                  Active

                </span>

                <span
                  v-else
                  class="badge rounded-pill bg-danger"
                >

                  <i class="bi bi-x-circle-fill me-1"></i>

                  Closed

                </span>

              </td>

              <td>

                <button
                  v-if="job.status === 'Active'"
                  class="btn btn-warning btn-sm me-2"
                  @click="closeJob(job.id)"
                >

                  <i class="bi bi-lock-fill"></i>

                </button>

                <button
                  v-else
                  class="btn btn-success btn-sm me-2"
                  @click="reopenJob(job.id)"
                >

                  <i class="bi bi-arrow-clockwise"></i>

                </button>

                <button
                  class="btn btn-danger btn-sm"
                  @click="deleteJob(job.id)"
                >

                  <i class="bi bi-trash-fill"></i>

                </button>

              </td>

            </tr>

          </tbody>

        </table>

      </div>

    </div>

  </div>

<!-- APPLICATIONS -->

<!-- APPLICATIONS -->

<div class="card shadow-lg border-0 rounded-4 mb-5">

  <div class="card-body">

    <!-- Header -->

    <div class="d-flex justify-content-between align-items-center flex-wrap mb-4">

      <h3 class="fw-bold mb-3 mb-lg-0">

        <i class="bi bi-people-fill text-primary me-2"></i>

        Received Applications

      </h3>

      <div class="d-flex gap-2 flex-wrap">

        <button
          class="btn btn-success"
          @click="exportCSV"
        >

          <i class="bi bi-file-earmark-spreadsheet me-2"></i>

          CSV

        </button>

        <button
          class="btn btn-danger"
          @click="downloadPDF"
        >

          <i class="bi bi-file-earmark-pdf me-2"></i>

          PDF

        </button>

        <button
          class="btn btn-warning"
          @click="downloadHTML"
        >

          <i class="bi bi-filetype-html me-2"></i>

          HTML

        </button>

      </div>

    </div>

    <!-- Applications Table -->

    <div class="table-responsive">

      <table class="table table-hover align-middle">

        <thead class="table-dark">

          <tr>

            <th>Student</th>

            <th>Job</th>

            <th>Status</th>

            <th>Interview</th>

            <th>Feedback</th>

            <th style="min-width:420px">
              Recruitment Actions
            </th>

            <th>Profile</th>

          </tr>

        </thead>

        <tbody>

          <tr
            v-for="app in applications"
            :key="app.application_id"
          >

            <!-- Student -->

            <td class="fw-semibold">

              <i class="bi bi-person-circle text-primary me-2"></i>

              {{ app.student_name }}

            </td>

            <!-- Job -->

            <td>

              {{ app.job_title }}

            </td>

            <!-- Status -->

            <td>

              <span
                class="badge rounded-pill"
                :class="{
                  'bg-primary': app.status==='Applied',
                  'bg-info': app.status==='Interview Scheduled',
                  'bg-success': app.status==='Placed',
                  'bg-warning text-dark': app.status==='Selected',
                  'bg-danger': app.status==='Rejected',
                  'bg-secondary': app.status==='Shortlisted'
                }"
              >

                {{ app.status }}

              </span>

            </td>

            <!-- Interview -->

            <td>

              <input

                v-model="app.interview_date"

                type="date"

                class="form-control shadow-sm"

              >

            </td>

            <!-- Feedback -->

            <td>

              <input

                v-model="app.feedback"

                class="form-control shadow-sm"

                placeholder="Add feedback"

              >

            </td>

            <!-- Actions -->

            <td>

              <div class="d-flex flex-wrap gap-2">

                <button

                  class="btn btn-primary btn-sm rounded-pill"

                  @click="scheduleInterview(app)"

                >

                  <i class="bi bi-calendar-event me-1"></i>

                  Interview

                </button>

                <button

                  class="btn btn-info btn-sm rounded-pill"

                  @click="addFeedback(app)"

                >

                  <i class="bi bi-chat-left-text me-1"></i>

                  Feedback

                </button>

                <button

                  class="btn btn-success btn-sm rounded-pill"

                  @click="updateStatus(app.application_id,'Shortlisted')"

                >

                  <i class="bi bi-check2-circle me-1"></i>

                  Shortlist

                </button>

                <button

                  class="btn btn-warning btn-sm rounded-pill"

                  @click="updateStatus(app.application_id,'Selected')"

                >

                  <i class="bi bi-star-fill me-1"></i>

                  Select

                </button>

                <button

                  class="btn btn-secondary btn-sm rounded-pill"

                  @click="offer(app.application_id)"

                >

                  <i class="bi bi-envelope-check me-1"></i>

                  Offer

                </button>

                <button

                  class="btn btn-dark btn-sm rounded-pill"

                  @click="placed(app.application_id)"

                >

                  <i class="bi bi-award-fill me-1"></i>

                  Placed

                </button>

                <button

                  class="btn btn-danger btn-sm rounded-pill"

                  @click="updateStatus(app.application_id,'Rejected')"

                >

                  <i class="bi bi-x-circle-fill me-1"></i>

                  Reject

                </button>

              </div>

            </td>

            <!-- Profile -->

            <td>

              <button

                class="btn btn-outline-primary btn-sm rounded-pill"

                @click="viewStudent(app)"

              >

                <i class="bi bi-person-vcard me-1"></i>

                Profile

              </button>

            </td>

          </tr>

        </tbody>

      </table>

    </div>

    <ATSChecker />

  </div>

</div>

</div>

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

      title: "",

      skills_required: "",

      salary: "",

      benefits: "",

      jobs: [],

      applications: []

    }

  },

async mounted() {

await this.fetchJobs()

await this.fetchApplications()

},

methods: {

getHeaders() {

return {

Authorization:
`Bearer ${localStorage.getItem("token")}`

}

},

async fetchJobs() {

const response = await axios.get(
"http://127.0.0.1:5000/company/jobs",
{
headers: this.getHeaders()
}
)

this.jobs = response.data

},

async downloadPDF() {

  const token =
    localStorage.getItem("token")

  const response =
    await axios.get(

      "http://127.0.0.1:5000/company/download-report/pdf",

      {
        responseType: "blob",

        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }

    )

},


async downloadPDF() {

  const token =
    localStorage.getItem("token")

  const response =
    await axios.get(

      "http://127.0.0.1:5000/company/download-report/html",

      {
        responseType: "blob",

        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }

    )

},


async fetchApplications() {

const response = await axios.get(
"http://127.0.0.1:5000/company/applications",
{
headers: this.getHeaders()
}
)

this.applications = response.data

},

async createJob() {

await axios.post(
"http://127.0.0.1:5000/company/create-job",
{
title: this.title,
skills_required: this.skills_required,
salary: this.salary,
benefits: this.benefits
},
{
headers: this.getHeaders()
}
)

await this.fetchJobs()

},

async closeJob(id) {

await axios.put(
`http://127.0.0.1:5000/company/close-job/${id}`,
{},
{
headers: this.getHeaders()
}
)

await this.fetchJobs()

},

async reopenJob(id) {

await axios.put(
`http://127.0.0.1:5000/company/reopen-job/${id}`,
{},
{
headers: this.getHeaders()
}
)

await this.fetchJobs()

},

async deleteJob(id) {

await axios.delete(
`http://127.0.0.1:5000/company/delete-job/${id}`,
{
headers: this.getHeaders()
}
)

await this.fetchJobs()

},

async scheduleInterview(app) {

await axios.put(
`http://127.0.0.1:5000/company/schedule-interview/${app.application_id}`,
{
interview_date: app.interview_date
},
{
headers: this.getHeaders()
}
)

alert("Interview Scheduled")

},

async addFeedback(app) {

await axios.put(
`http://127.0.0.1:5000/company/feedback/${app.application_id}`,
{
feedback: app.feedback
},
{
headers: this.getHeaders()
}
)

alert("Feedback Added")

},

async offer(id) {

  await axios.put(

    `http://127.0.0.1:5000/company/offer/${id}`,

    {},

    {
      headers: this.getHeaders()
    }

  )

  await this.fetchApplications()

},

async placed(id) {

  await axios.put(

    `http://127.0.0.1:5000/company/placed/${id}`,

    {},

    {
      headers: this.getHeaders()
    }

  )

  await this.fetchApplications()

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

async exportCSV() {

  const token =
    localStorage.getItem("token")

  const headers = {

    Authorization:
      `Bearer ${token}`

  }

  try {

    const response =
      await axios.post(

        "http://127.0.0.1:5000/company/export-csv",

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
      "Export failed"
    )

  }

},

async updateStatus(id,status) {

await axios.put(
`http://127.0.0.1:5000/company/update-status/${id}`,
{
status: status
},
{
headers: this.getHeaders()
}
)

await this.fetchApplications()

}

}

}

</script>

