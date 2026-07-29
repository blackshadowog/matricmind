import pandas as pd
import plotly.express as px
from database import load_all_tables


# ==========================================
# Monthly Revenue Chart
# ==========================================
def monthly_revenue_chart():

    tables = load_all_tables()

    orders = tables["orders"].copy()

    orders["created_at"] = pd.to_datetime(orders["created_at"])

    monthly_sales = (
        orders.groupby(
            orders["created_at"].dt.to_period("M")
        )["total_amount"]
        .sum()
        .reset_index()
    )

    monthly_sales["created_at"] = monthly_sales["created_at"].astype(str)

    fig = px.line(
        monthly_sales,
        x="created_at",
        y="total_amount",
        markers=True,
        title="Monthly Revenue"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Month",
        yaxis_title="Revenue",
        height=500,
    )

    return fig.to_html(
        full_html=False,
        include_plotlyjs="cdn"
    )


# ==========================================
# Top Selling Products
# ==========================================
def top_products_chart():

    tables = load_all_tables()

    products = tables["products"].copy()
    order_items = tables["order_items"].copy()

    order_items["Sales"] = (
        order_items["quantity"] *
        order_items["unit_price"]
    )

    merged = order_items.merge(
        products,
        left_on="product_id",
        right_on="id"
    )

    top_products = (
        merged.groupby("name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top_products,
        x="name",
        y="Sales",
        color="Sales",
        text_auto=True,
        title="Top 10 Selling Products"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Product",
        yaxis_title="Revenue",
        height=500,
    )

    return fig.to_html(
        full_html=False,
        include_plotlyjs=False
    )


# ==========================================
# Sales by Region
# ==========================================
def sales_by_region_chart():

    tables = load_all_tables()

    orders = tables["orders"].copy()

    region_sales = (
        orders.groupby("region")["total_amount"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        region_sales,
        names="region",
        values="total_amount",
        hole=0.45,
        title="Sales by Region"
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
    )

    return fig.to_html(
        full_html=False,
        include_plotlyjs=False
    )
# ==========================================
# Orders by Status
# ==========================================
def order_status_chart():

    tables = load_all_tables()

    orders = tables["orders"].copy()

    status = (
        orders.groupby("status")
        .size()
        .reset_index(name="count")
    )

    fig = px.bar(
        status,
        x="status",
        y="count",
        color="count",
        text_auto=True,
        title="Orders by Status"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Status",
        yaxis_title="Number of Orders",
        height=500,
    )

    return fig.to_html(
        full_html=False,
        include_plotlyjs=False
    )


# ==========================================
# Inventory Stock
# ==========================================
def inventory_chart():

    tables = load_all_tables()

    inventory = tables["inventory"].copy()

    fig = px.bar(
        inventory,
        x="product_id",
        y="quantity_in_stock",
        color="quantity_in_stock",
        text_auto=True,
        title="Inventory Stock"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Product ID",
        yaxis_title="Quantity in Stock",
        height=500,
    )

    return fig.to_html(
        full_html=False,
        include_plotlyjs=False
    )


# ==========================================
# Budget vs Expense
# ==========================================
def budget_vs_expense_chart():

    tables = load_all_tables()

    budgets = tables["budgets"].copy()
    expenses = tables["expenses"].copy()

    total_budget = budgets["allocated_amount"].sum()
    total_expense = expenses["amount"].sum()

    comparison = pd.DataFrame({
        "Type": ["Budget", "Expense"],
        "Amount": [total_budget, total_expense]
    })

    fig = px.bar(
        comparison,
        x="Type",
        y="Amount",
        color="Type",
        text_auto=True,
        title="Budget vs Expense"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Category",
        yaxis_title="Amount",
        height=500,
    )

    return fig.to_html(
        full_html=False,
        include_plotlyjs=False
    )