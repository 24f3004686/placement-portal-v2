<template>

<div class="container py-5">

<div class="text-center mb-5">

<h1 class="display-4 fw-bold text-primary">

<i class="bi bi-mortarboard-fill me-2"></i>

Placement Portal

</h1>

<p class="lead text-muted">

Placement Management System

</p>

</div>

<div class="row g-4 mb-5">

<div class="col-md-3">

<div class="card shadow border-0 text-center p-4 h-100">

<i class="bi bi-people-fill display-5 text-primary"></i>

<h6 class="mt-3">Students</h6>

<h2>{{ stats.students }}</h2>

</div>

</div>

<div class="col-md-3">

<div class="card shadow border-0 text-center p-4 h-100">

<i class="bi bi-building display-5 text-success"></i>

<h6 class="mt-3">Companies</h6>

<h2>{{ stats.companies }}</h2>

</div>

</div>

<div class="col-md-3">

<div class="card shadow border-0 text-center p-4 h-100">

<i class="bi bi-briefcase-fill display-5 text-warning"></i>

<h6 class="mt-3">Jobs</h6>

<h2>{{ stats.jobs }}</h2>

</div>

</div>

<div class="col-md-3">

<div class="card shadow border-0 text-center p-4 h-100">

<i class="bi bi-file-earmark-check-fill display-5 text-danger"></i>

<h6 class="mt-3">Applications</h6>

<h2>{{ stats.applications }}</h2>

</div>

</div>

</div>

<div class="row g-4">

<div class="col-lg-8">

<ApplicationsChart/>

</div>

<div class="col-lg-4">

<StatusChart :stats="stats"/>

</div>

</div>

</div>

</template>

<script>

import axios from "axios"

import ApplicationsChart from "./charts/ApplicationsChart.vue"

import StatusChart from "./charts/StatusChart.vue"

export default{

components:{

ApplicationsChart,

StatusChart

},

data(){

return{

stats:{}

}

},

async mounted(){

const response=await axios.get(

"http://127.0.0.1:5000/public/dashboard"

)

this.stats=response.data

}

}

</script>
