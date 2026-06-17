<template>

<div class="card shadow border-0 rounded-4 p-4 h-100">

<h5 class="fw-bold mb-3">
Placement Status
</h5>

<Pie :data="chartData" />

</div>

</template>

<script setup>

import { computed } from "vue"

import {
Chart as ChartJS,
ArcElement,
Tooltip,
Legend
} from "chart.js"

import { Pie } from "vue-chartjs"

ChartJS.register(
ArcElement,
Tooltip,
Legend
)

const props = defineProps({

stats: {

type: Object,

required: true

}

})

const chartData = computed(() => ({

labels: [

"Placed",

"Selected",

"Rejected",

"Pending"

],

datasets: [

{

data: [

props.stats.placed,

props.stats.selected,

props.stats.rejected,

props.stats.pending

],

backgroundColor: [

"#198754",

"#0d6efd",

"#dc3545",

"#ffc107"

]

}

]

}))

</script>