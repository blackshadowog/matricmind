import os
from flask import Flask, render_template

from backend.analytics import (
    get_dashboard_metrics,
    generate_ai_insights
)

from backend.charts import (
    monthly_revenue_chart,
    top_products_chart,
    sales_by_region_chart,
    order_status_chart,
    inventory_chart,
    budget_vs_expense_chart,
)

# ==========================================
# Flask Configuration
# ==========================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
)

# ==========================================
# Dashboard Route
# ==========================================

@app.route("/")
def home():

    # KPI Metrics
    metrics = get_dashboard_metrics()

    # AI Insights
    ai_insights = generate_ai_insights()

    # Render Dashboard
    return render_template(
        "dashboard.html",

        # KPI Cards
        metrics=metrics,

        # AI Insights
        ai_insights=ai_insights,

        # Plotly Charts
        monthly_revenue_chart=monthly_revenue_chart(),
        top_products_chart=top_products_chart(),
        sales_by_region_chart=sales_by_region_chart(),
        order_status_chart=order_status_chart(),
        inventory_chart=inventory_chart(),
        budget_vs_expense_chart=budget_vs_expense_chart(),
    )

# ==========================================
# Run Flask
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)