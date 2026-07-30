from backend.database import load_all_tables


def get_dashboard_metrics():
    tables = load_all_tables()

    orders = tables["orders"]
    order_items = tables["order_items"]
    customers = tables["customers"]
    products = tables["products"]
    returns = tables["returns"]
    inventory = tables["inventory"]
    budgets = tables["budgets"]
    expenses = tables["expenses"]

    # ==========================
    # KPI Metrics
    # ==========================

    total_revenue = (
        order_items["quantity"] *
        order_items["unit_price"]
    ).sum()

    total_budget = budgets["allocated_amount"].sum()

    total_expense = expenses["amount"].sum()

    low_stock = (
        inventory["quantity_in_stock"] < 20
    ).sum()

    budget_usage = 0

    if total_budget > 0:
        budget_usage = round(
            (total_expense / total_budget) * 100,
            1
        )

    return {
        "Total Orders": len(orders),
        "Total Customers": len(customers),
        "Total Products": len(products),
        "Total Returns": len(returns),
        "Total Revenue": round(total_revenue, 2),

        # New Metrics
        "Low Stock": int(low_stock),
        "Budget Usage": budget_usage,
        "Total Expense": round(total_expense, 2),
        "Total Budget": round(total_budget, 2),
    }


# ==========================================
# AI Insights
# ==========================================

def generate_ai_insights():

    metrics = get_dashboard_metrics()

    insights = []

    # Revenue
    revenue = metrics["Total Revenue"]

    if revenue >= 100000:
        insights.append({
            "icon": "🟢",
            "title": "Revenue",
            "message": f"Revenue reached ₹{revenue:,.0f}.",
            "recommendation": "Excellent business performance. Maintain the current growth strategy."
        })
    else:
        insights.append({
            "icon": "🟡",
            "title": "Revenue",
            "message": f"Revenue reached ₹{revenue:,.0f}.",
            "recommendation": "Increase marketing campaigns to improve revenue."
        })

    # Customers
    customers = metrics["Total Customers"]

    if customers >= 100:
        insights.append({
            "icon": "🟢",
            "title": "Customers",
            "message": f"{customers} customers registered.",
            "recommendation": "Customer acquisition is healthy."
        })
    else:
        insights.append({
            "icon": "🟡",
            "title": "Customers",
            "message": f"{customers} customers registered.",
            "recommendation": "Focus on customer acquisition."
        })

    # Inventory
    low_stock = metrics["Low Stock"]

    if low_stock == 0:
        insights.append({
            "icon": "🟢",
            "title": "Inventory",
            "message": "Inventory levels are healthy.",
            "recommendation": "No immediate action required."
        })
    else:
        insights.append({
            "icon": "🔴",
            "title": "Inventory",
            "message": f"{low_stock} products are running low on stock.",
            "recommendation": "Restock low inventory items."
        })

    # Budget
    budget = metrics["Budget Usage"]

    if budget < 80:
        insights.append({
            "icon": "🟢",
            "title": "Budget",
            "message": f"{budget}% of budget utilized.",
            "recommendation": "Budget utilization is healthy."
        })
    else:
        insights.append({
            "icon": "🔴",
            "title": "Budget",
            "message": f"{budget}% of budget utilized.",
            "recommendation": "Review expenses to avoid overspending."
        })

    return insights