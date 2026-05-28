```vue
<template>

  <div class="container mt-5">

    <h1 class="text-warning fw-bold mb-4">
      Company Dashboard
    </h1>


    <!-- CREATE JOB -->

    <div class="card shadow border-0 p-4 rounded-4 mb-5">

      <h3 class="mb-4">
        Post New Job
      </h3>

      <input
        v-model="title"
        class="form-control mb-3"
        placeholder="Job Title"
      >

      <input
        v-model="skills_required"
        class="form-control mb-3"
        placeholder="Skills Required"
      >

      <input
        v-model="salary"
        class="form-control mb-3"
        placeholder="Salary"
      >

      <input
        v-model="benefits"
        class="form-control mb-3"
        placeholder="Benefits"
      >

      <button
        class="btn btn-warning"
        @click="createJob"
      >
        Create Job
      </button>

    </div>


    <!-- JOB LIST -->

    <div class="card shadow border-0 p-4 rounded-4">

      <h3 class="mb-4">
        Posted Jobs
      </h3>

      <table class="table table-hover">

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

          <tr
            v-for="job in jobs"
            :key="job.id"
          >

            <td>{{ job.id }}</td>

            <td>{{ job.title }}</td>

            <td>{{ job.skills_required }}</td>

            <td>{{ job.salary }}</td>

            <td>

              <span
                v-if="job.status === 'Active'"
                class="badge bg-success"
              >
                Active
              </span>

              <span
                v-else
                class="badge bg-danger"
              >
                Closed
              </span>

            </td>

            <td>

              <button
                v-if="job.status === 'Active'"
                class="btn btn-warning btn-sm me-2"
                @click="closeJob(job.id)"
              >
                Close
              </button>

              <button
                v-else
                class="btn btn-success btn-sm me-2"
                @click="reopenJob(job.id)"
              >
                Reopen
              </button>

              <button
                class="btn btn-danger btn-sm"
                @click="deleteJob(job.id)"
              >
                Delete
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

      jobs: []

    }

  },

  async mounted() {

    await this.fetchJobs()

  },

  methods: {

    async fetchJobs() {

      try {

        const token = localStorage.getItem("token")

        const headers = {

          Authorization: `Bearer ${token}`

        }

        const response = await axios.get(

          "http://127.0.0.1:5000/company/jobs",

          { headers }

        )

        this.jobs = response.data

      }

      catch(error) {

        console.log(error)

      }

    },


    async createJob() {

      try {

        const token = localStorage.getItem("token")

        const headers = {

          Authorization: `Bearer ${token}`

        }

        await axios.post(

          "http://127.0.0.1:5000/company/create-job",

          {

            title: this.title,

            skills_required: this.skills_required,

            salary: this.salary,

            benefits: this.benefits

          },

          { headers }

        )

        alert("Job Created Successfully")

        this.title = ""

        this.skills_required = ""

        this.salary = ""

        this.benefits = ""

        await this.fetchJobs()

      }

      catch(error) {

        console.log(error)

        alert("Failed to create job")

      }

    },


    async closeJob(id) {

      try {

        const token = localStorage.getItem("token")

        const headers = {

          Authorization: `Bearer ${token}`

        }

        await axios.put(

          `http://127.0.0.1:5000/company/close-job/${id}`,

          {},

          { headers }

        )

        await this.fetchJobs()

      }

      catch(error) {

        console.log(error)

      }

    },


    async reopenJob(id) {

      try {

        const token = localStorage.getItem("token")

        const headers = {

          Authorization: `Bearer ${token}`

        }

        await axios.put(

          `http://127.0.0.1:5000/company/reopen-job/${id}`,

          {},

          { headers }

        )

        await this.fetchJobs()

      }

      catch(error) {

        console.log(error)

      }

    },


    async deleteJob(id) {

      try {

        const token = localStorage.getItem("token")

        const headers = {

          Authorization: `Bearer ${token}`

        }

        await axios.delete(

          `http://127.0.0.1:5000/company/delete-job/${id}`,

          { headers }

        )

        await this.fetchJobs()

      }

      catch(error) {

        console.log(error)

      }

    }

  }

}

</script>
```
