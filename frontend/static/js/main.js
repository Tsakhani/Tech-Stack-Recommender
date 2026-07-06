
const API_URL = "http://127.0.0.1:8000/recommend";

let skills = [];

const skillInput = document.getElementById("skillInput");
const addSkillButton = document.getElementById("addSkill");
const skillsContainer = document.getElementById("skillsContainer");

const recommendButton = document.getElementById("recommendButton");

const loading = document.getElementById("loading");

const results = document.getElementById("results");

const resultsSection = document.getElementById("resultsSection");

const emptyState = document.getElementById("emptyState");


// =====================================================
// Initialise
// =====================================================

document.addEventListener("DOMContentLoaded", () => {

    skillInput.focus();

});


// =====================================================
// Add Skill
// =====================================================

function addSkill() {

    const skill = skillInput.value.trim();

    if (skill === "") return;

    if (skills.includes(skill)) {

        alert("Skill already added.");

        return;

    }

    skills.push(skill);

    renderSkills();

    skillInput.value = "";

    skillInput.focus();

}


// =====================================================
// Render Skill Chips
// =====================================================

function renderSkills() {

    skillsContainer.innerHTML = "";

    skills.forEach((skill, index) => {

        const chip = document.createElement("div");

        chip.className =
            "flex items-center gap-3 bg-cyan-500/20 border border-cyan-500/40 text-cyan-300 rounded-full px-4 py-2 transition hover:scale-105";

        chip.innerHTML = `

            <span>${skill}</span>

            <button
                onclick="removeSkill(${index})"
                class="text-red-400 hover:text-red-300 text-sm">

                ✕

            </button>

        `;

        skillsContainer.appendChild(chip);

    });

}


// =====================================================
// Remove Skill
// =====================================================

function removeSkill(index) {

    skills.splice(index, 1);

    renderSkills();

}


// =====================================================
// Button Events
// =====================================================

addSkillButton.addEventListener("click", addSkill);

skillInput.addEventListener("keypress", function(event){

    if(event.key === "Enter"){

        event.preventDefault();

        addSkill();

    }

});


// =====================================================
// Recommendation Request
// =====================================================

recommendButton.addEventListener("click", async () => {

    if (skills.length < 3) {

        alert("Please enter at least three skills.");

        return;

    }

    emptyState.classList.add("hidden");

    resultsSection.classList.add("hidden");

    loading.classList.remove("hidden");

    recommendButton.disabled = true;

    recommendButton.innerHTML = "Analysing...";

    try {

        const response = await fetch(API_URL, {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                skills: skills

            })

        });

        if (!response.ok) {

            throw new Error("Recommendation API returned an error.");

        }

        const data = await response.json();

        loading.classList.add("hidden");

        recommendButton.disabled = false;

        recommendButton.innerHTML = "✨ Find My Career";

        displayRecommendations(data.recommendations);

    }

    catch(error){

        console.error(error);

        loading.classList.add("hidden");

        recommendButton.disabled = false;

        recommendButton.innerHTML = "✨ Find My Career";

        alert("Unable to connect to recommendation server.");

    }

});


// =====================================================
// Display Recommendations
// =====================================================

function displayRecommendations(recommendations){

    results.innerHTML = "";

    resultsSection.classList.remove("hidden");

    recommendations.forEach((recommendation, index) => {

        const percentage = Math.round(recommendation.score * 100);

        const card = document.createElement("div");

        card.className =
            "bg-card border border-slate-800 rounded-3xl p-8 shadow-2xl hover:-translate-y-2 hover:border-cyan-400 transition duration-300 animate-slideUp";

        card.style.animationDelay = `${index * 0.15}s`;

        card.innerHTML = `

            <div class="flex justify-between items-center">

                <div>

                    <h2 class="text-3xl font-bold">

                        ${recommendation.job_role}

                    </h2>

                    <p class="text-cyan-400 mt-2">

                        Excellent Match

                    </p>

                </div>

                <div class="text-right">

                    <h1 class="text-5xl font-extrabold">

                        ${percentage}%

                    </h1>

                </div>

            </div>

            <hr class="my-6 border-slate-700">

            <div>

                <h3 class="font-semibold mb-3">

                    Skills Used

                </h3>

                <div class="flex flex-wrap gap-2">

                    ${skills.map(skill => `

                        <span class="bg-slate-800 px-3 py-2 rounded-full text-sm">

                            ${skill}

                        </span>

                    `).join("")}

                </div>

            </div>

            <div class="mt-8">

                <div class="flex justify-between mb-2">

                    <span>

                        AI Confidence

                    </span>

                    <span>

                        ${percentage}%

                    </span>

                </div>

                <div class="w-full bg-slate-700 rounded-full h-4">

                    <div
                        class="bg-gradient-to-r from-cyan-400 to-indigo-500 h-4 rounded-full"
                        style="width:${percentage}%">

                    </div>

                </div>

            </div>

        `;

        results.appendChild(card);

    });

}

