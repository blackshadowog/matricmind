document.addEventListener("DOMContentLoaded", function () {

    // ==========================
    // Dashboard Search
    // ==========================

    const searchBox = document.getElementById("dashboardSearch");

    if (searchBox) {

        const sections = [
            {
                keywords: ["revenue", "sales", "income", "monthly"],
                id: "monthlyRevenue"
            },
            {
                keywords: ["customer", "customers"],
                id: "kpis"
            },
            {
                keywords: ["orders", "order", "status"],
                id: "ordersStatus"
            },
            {
                keywords: ["inventory", "stock"],
                id: "inventory"
            },
            {
                keywords: ["budget", "expense", "finance"],
                id: "budget"
            },
            {
                keywords: ["region", "country"],
                id: "salesRegion"
            },
            {
                keywords: ["product", "products", "top"],
                id: "topProducts"
            },
            {
                keywords: ["ai", "insight", "insights"],
                id: "aiInsights"
            },
            {
                keywords: ["summary"],
                id: "summary"
            },
            {
                keywords: ["dashboard", "home"],
                id: "hero"
            }
        ];

        searchBox.addEventListener("keypress", function (e) {

            if (e.key !== "Enter") return;

            const query = searchBox.value.trim().toLowerCase();

            if (!query) return;

            let found = false;

            sections.forEach(section => {

                if (section.keywords.some(word => query.includes(word))) {

                    const element = document.getElementById(section.id);

                    if (element) {

                        element.scrollIntoView({
                            behavior: "smooth",
                            block: "start"
                        });

                        element.style.transition = "0.4s";
                        element.style.boxShadow = "0 0 25px #3056d3";

                        setTimeout(() => {
                            element.style.boxShadow = "";
                        }, 2000);

                        found = true;
                    }
                }

            });

            if (!found) {
                alert("No matching dashboard section found.");
            }

        });

    }

    // ==========================
    // Dark Mode
    // ==========================

    const themeBtn = document.getElementById("theme-toggle");

    if (themeBtn) {

        themeBtn.addEventListener("click", () => {

            document.body.classList.toggle("dark-mode");

        });

    }

    // ==========================
    // Dashboard Toolbar
    // ==========================

    const dateElement = document.getElementById("currentDate");
    const timeElement = document.getElementById("currentTime");
    const lastUpdated = document.getElementById("lastUpdated");

    function updateClock() {

        const now = new Date();

        if (dateElement) {

            dateElement.innerHTML =
                `<i class="fa-solid fa-calendar-days"></i> ${now.toLocaleDateString()}`;

        }

        if (timeElement) {

            timeElement.innerHTML =
                `<i class="fa-solid fa-clock"></i> ${now.toLocaleTimeString()}`;

        }

    }

    updateClock();

    setInterval(updateClock, 1000);

    if (lastUpdated) {

        lastUpdated.innerHTML =
            `<i class="fa-solid fa-rotate"></i> Last Updated: Just Now`;

    }

    // ==========================
    // Refresh Button
    // ==========================

    const refreshBtn = document.getElementById("refreshDashboard");

    if (refreshBtn) {

        refreshBtn.addEventListener("click", () => {

            location.reload();

        });

    }

    // ==========================
    // Download Button
    // ==========================

    const downloadBtn = document.getElementById("downloadDashboard");

    if (downloadBtn) {

        downloadBtn.addEventListener("click", () => {

            window.print();

        });

    }

    // ==========================
    // Fullscreen Button
    // ==========================

    const fullscreenBtn = document.getElementById("fullscreenBtn");

    if (fullscreenBtn) {

        fullscreenBtn.addEventListener("click", () => {

            if (!document.fullscreenElement) {

                document.documentElement.requestFullscreen();

            } else {

                document.exitFullscreen();

            }

        });

    }
// ==========================
// Animated KPI Counters
// ==========================

const counters = document.querySelectorAll(".counter");

counters.forEach(counter => {

    const target = Number(counter.dataset.target);

    let count = 0;

    const increment = Math.max(target / 100, 1);

    function updateCounter() {

        if (count < target) {

            count += increment;

            counter.textContent = Math.floor(count).toLocaleString();

            requestAnimationFrame(updateCounter);

        } else {

            counter.textContent = target.toLocaleString();

        }

    }

    updateCounter();

});
});
// ==========================
// Download Dashboard Report
// ==========================

const downloadBtn = document.getElementById("downloadDashboard");

if (downloadBtn) {
    downloadBtn.addEventListener("click", () => {
        window.location.href = "/download-report";
    });
}