import os
from flask import (
    Flask,
    render_template,
    send_file,
    request,
    jsonify,
    redirect,
    url_for,
    session,
)

from backend.analytics import (
    business_chat,
    get_dashboard_metrics,
    generate_ai_insights,
)

from backend.report_generator import generate_dashboard_report

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

app.secret_key = "metricmind_secret_key"

# ==========================================
# Login Page
# ==========================================

@app.route("/")
def login():
    return render_template("login.html")


# ==========================================
# Dashboard
# ==========================================

@app.route("/dashboard", methods=["POST"])
def dashboard():

    email = request.form.get("email")
    password = request.form.get("password")

    # Demo Login - Accept Any Email & Password

    session["user"] = email

    metrics = get_dashboard_metrics()
    ai_insights = generate_ai_insights()

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
# Download PDF Report
# ==========================================

@app.route("/download-report")
def download_report():

    if "user" not in session:
        return redirect(url_for("login"))

    metrics = get_dashboard_metrics()
    insights = generate_ai_insights()

    pdf = generate_dashboard_report(
        metrics,
        insights
    )

    return send_file(
        pdf,
        as_attachment=True,
        download_name="MetricMind_Report.pdf",
        mimetype="application/pdf",
    )


# ==========================================
# AI Chat
# ==========================================

@app.route("/chat", methods=["POST"])
def chat():

    if "user" not in session:
        return jsonify({
            "answer": "Please login first."
        })

    data = request.get_json()

    question = data.get("message", "").lower()

    advanced_answer = business_chat(question)

    if advanced_answer:
        return jsonify({
            "answer": advanced_answer
        })

    metrics = get_dashboard_metrics()

    if "revenue" in question:
        answer = f"📈 Total Revenue: ₹{metrics['Total Revenue']:,.2f}"

    elif "customer" in question:
        answer = f"👥 Total Customers: {metrics['Total Customers']}"

    elif "product" in question:
        answer = f"📦 Total Products: {metrics['Total Products']}"

    elif "return" in question:
        answer = f"↩ Total Returns: {metrics['Total Returns']}"

    elif "budget" in question:
        answer = f"💰 Budget Usage: {metrics['Budget Usage']}%"

    elif "summary" in question:
        answer = (
            f"Dashboard Summary:\n\n"
            f"Revenue: ₹{metrics['Total Revenue']:,.2f}\n"
            f"Customers: {metrics['Total Customers']}\n"
            f"Products: {metrics['Total Products']}\n"
            f"Returns: {metrics['Total Returns']}\n"
            f"Budget Usage: {metrics['Budget Usage']}%"
        )

    else:
        answer = (
            "Sorry, I couldn't understand that.\n\n"
            "Try asking:\n"
            "• Show revenue\n"
            "• Total customers\n"
            "• Products\n"
            "• Returns\n"
            "• Summary"
        )

    return jsonify({
        "answer": answer
    })


# ==========================================
# Logout
# ==========================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


# ==========================================
# Run Flask
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)