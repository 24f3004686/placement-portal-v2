<template>

<div class="card shadow border-0 rounded-4 p-4 h-100">

<h5 class="fw-bold mb-3">
Monthly Applications
</h5>

<Bar
:data="chartData"
:options="chartOptions"
/>

</div>

</template>

<script setup>

import {

Chart as ChartJS,
CategoryScale,
LinearScale,
BarElement,
Title,
Tooltip,
Legend

} from "chart.js"

import { Bar } from "vue-chartjs"

ChartJS.register(

CategoryScale,
LinearScale,
BarElement,
Title,
Tooltip,
Legend

)

const chartData = {

labels: [

"Jan",
"Feb",
"Mar",
"Apr",
"May",
"Jun"

],

datasets: [

{

label: "Applications",

data: [

12,
19,
8,
25,
32,
18

],

backgroundColor: "#0d6efd"

}

]

}

const chartOptions = {

responsive: true,

plugins: {

legend: {

display: false

}

}

}

</script>
