<template>

<div class="container mt-5">

<h1 class="text-warning fw-bold mb-4">
Company Dashboard
</h1>

<!-- CREATE JOB -->

<div class="card shadow border-0 p-4 rounded-4 mb-5">

<h3 class="mb-4">Post New Job</h3>

<input v-model="title" class="form-control mb-3" placeholder="Job Title">

<input v-model="skills_required" class="form-control mb-3" placeholder="Skills Required">

<input v-model="salary" class="form-control mb-3" placeholder="Salary">

<input v-model="benefits" class="form-control mb-3" placeholder="Benefits">

<button class="btn btn-warning" @click="createJob">
Create Job
</button>

</div>

<!-- JOBS -->

<div class="card shadow border-0 p-4 rounded-4 mb-5">

<h3 class="mb-4">Posted Jobs</h3>

<table class="table">

<thead>
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

<tr v-for="job in jobs" :key="job.id">

<td>{{ job.id }}</td>
<td>{{ job.title }}</td>
<td>{{ job.skills_required }}</td>
<td>{{ job.salary }}</td>

<td>
<span
v-if="job.status==='Active'"
class="badge bg-success">
Active
</span>

<span
v-else
class="badge bg-danger">
Closed
</span>
</td>

<td>

<button
v-if="job.status==='Active'"
class="btn btn-warning btn-sm me-2"
@click="closeJob(job.id)">
Close
</button>

<button
v-else
class="btn btn-success btn-sm me-2"
@click="reopenJob(job.id)">
Reopen
</button>

<button
class="btn btn-danger btn-sm"
@click="deleteJob(job.id)">
Delete
</button>

</td>

</tr>

</tbody>

</table>

</div>

<!-- APPLICATIONS -->

<div class="card shadow border-0 p-4 rounded-4">

<h3 class="mb-4">
Received Applications
</h3>

<table class="table">

<thead>

<tr>

<th>Student</th>

<th>Job</th>

<th>Status</th>

<th>Interview Date</th>

<th>Feedback</th>

<th>Actions</th>

<th>Profile</th>

</tr>

</thead>

<tbody>

<tr
v-for="app in applications"
:key="app.application_id"
>

<td>{{ app.student_name }}</td>

<td>{{ app.job_title }}</td>

<td>{{ app.status }}</td>

<td>
<input
v-model="app.interview_date"
type="date"
class="form-control"
/>
</td>

<td>
<input
v-model="app.feedback"
class="form-control"
placeholder="Feedback"
/>
</td>

<td>

<button
class="btn btn-primary btn-sm me-1"
@click="scheduleInterview(app)"
>
Interview
</button>

<button
class="btn btn-info btn-sm me-1"
@click="addFeedback(app)"
>
Feedback
</button>

<button
class="btn btn-success btn-sm me-1"
@click="updateStatus(app.application_id,'Shortlisted')"
>
Shortlist
</button>

<button
class="btn btn-warning btn-sm me-1"
@click="updateStatus(app.application_id,'Selected')"
>
Select
</button>

<button
class="btn btn-danger btn-sm"
@click="updateStatus(app.application_id,'Rejected')"
>
Reject
</button>

<button
  class="btn btn-secondary btn-sm me-1"
  @click="offer(app.application_id)"
>
  Offer
</button>

<button
  class="btn btn-dark btn-sm"
  @click="placed(app.application_id)"
>
  Placed
</button>

</td>

<td>

  <button
    class="btn btn-info btn-sm"
    @click="viewStudent(app)"
  >
    View Profile
  </button>

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

