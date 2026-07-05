const button = document.getElementById("recommendButton");
const skillsInput = document.getElementById("skills");
const loading = document.getElementById("loading");
const results = document.getElementById("results");

button.addEventListener("click", async () => {

    results.innerHTML = "";

    loading.classList.remove("hidden");

    const skills = skillsInput.value
        .split(",")
        .map(skill => skill.trim())
        .filter(skill => skill.length > 0);

    if (skills.length < 3) {

        loading.classList.add("hidden");

        alert("Please enter at least 3 skills.");

        return;
    }

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/recommend",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },
                body:JSON.stringify({
                    skills: skills
                })
            }
        );

        const data = await response.json();

        displayRecommendations(data.recommendations);

    } catch (error) {
        alert("Unable to connect to the recommendation server.");

        console.error(error);
    } finally {
        loading.classList.add("hidden")
    }

});

function displayRecommendations(recommendations) {

    recommendations.forEach(recommendation =>{

        const card = document.createElement("div");

        card.className = "bg-slate-50 border rounded-lg p-5 shadow";

        card.innerHTML = `
            <h2 class="text-xl font-semibold">
                ${recommendation.job_role}
            </h2>
            <p class="text-gray-500">
                Match Score: ${(recommendation.score*100).toFixed(1)}%
            </p>
        `;

        results.appendChild(card);

        
    });
}