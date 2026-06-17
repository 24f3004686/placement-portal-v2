<template>

<div class="card shadow-lg border-0 rounded-4 p-4 mt-4">

    <h3 class="fw-bold mb-4">
        <i class="bi bi-file-earmark-person-fill me-2 text-primary"></i>
        ATS Resume Screener
    </h3>

    <!-- Resume -->

    <div class="mb-3">

        <label class="form-label fw-semibold">
            Resume Text
        </label>

        <textarea
            v-model="resume"
            rows="8"
            class="form-control"
            placeholder="Paste your resume here..."
        ></textarea>

    </div>

    <!-- Skills -->

    <div class="mb-3">

        <label class="form-label fw-semibold">
            Required Skills
        </label>

        <input
            v-model="skills"
            class="form-control"
            placeholder="Python, SQL, Flask, Vue, Docker"
        >

    </div>

    <button
        class="btn btn-primary"
        @click="analyzeResume"
    >

        <i class="bi bi-search me-2"></i>

        Analyze Resume

    </button>

    <!-- Results -->

    <div
        v-if="score !== null"
        class="mt-5"
    >

        <h4>

            ATS Score

            <span class="badge bg-success ms-2">

                {{ score }}%

            </span>

        </h4>

        <div class="progress mb-4" style="height:28px;">

            <div
                class="progress-bar progress-bar-striped progress-bar-animated"
                :style="{width: score + '%'}"
            >

                {{ score }}%

            </div>

        </div>

        <div class="row">

            <div class="col-md-6">

                <div class="card border-success">

                    <div class="card-body">

                        <h5 class="text-success">

                            <i class="bi bi-check-circle-fill me-2"></i>

                            Matched Skills

                        </h5>

                        <span
                            v-for="skill in matched"
                            :key="skill"
                            class="badge bg-success me-2 mb-2"
                        >

                            {{ skill }}

                        </span>

                    </div>

                </div>

            </div>

            <div class="col-md-6">

                <div class="card border-danger">

                    <div class="card-body">

                        <h5 class="text-danger">

                            <i class="bi bi-x-circle-fill me-2"></i>

                            Missing Skills

                        </h5>

                        <span
                            v-for="skill in missing"
                            :key="skill"
                            class="badge bg-danger me-2 mb-2"
                        >

                            {{ skill }}

                        </span>

                    </div>

                </div>

            </div>

        </div>

        <div class="alert alert-info mt-4">

            <strong>Recommendation :</strong>

            {{ recommendation }}

        </div>

    </div>

</div>

</template>

<script>

import axios from "axios"

export default{

data(){

return{

resume:"",

skills:"",

score:null,

matched:[],

missing:[]

}

},

computed:{

recommendation(){

if(this.score>=90) return "Excellent Match ⭐⭐⭐⭐⭐"

if(this.score>=70) return "Strong Match ⭐⭐⭐⭐"

if(this.score>=50) return "Average Match ⭐⭐⭐"

return "Weak Match ⭐"

}

},

methods:{

async analyzeResume(){

try{

const response=await axios.post(

"http://127.0.0.1:5000/ats/analyze",

{

resume:this.resume,

skills:this.skills

}

)

this.score=response.data.score

this.matched=response.data.matched

this.missing=response.data.missing

}

catch(error){

console.log(error)

alert("ATS Analysis failed")

}

}

}

}

</script>
