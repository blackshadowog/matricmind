from backend.database import load_all_tables


def get_dashboard_metrics():
    tables = load_all_tables()

    orders = tables["orders"]
    order_items = tables["order_items"]
    customers = tables["customers"]
    products = tables["products"]
    returns = tables["returns"]

    # Calculate total revenue
    total_revenue = (
        order_items["quantity"] * order_items["unit_price"]
    ).sum()

    return {
        "Total Orders": len(orders),
        "Total Customers": len(customers),
        "Total Products": len(products),
        "Total Returns": len(returns),
        "Total Revenue": round(total_revenue, 2),
    }


if __name__ == "__main__":
    metrics = get_dashboard_metrics()

    print("\n===== MetricMind Dashboard =====")
    for key, value in metrics.items():
        print(f"{key}: {value}")