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

});