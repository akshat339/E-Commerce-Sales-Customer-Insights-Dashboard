import json
import pandas as pd

data = {
    "order_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "date": [
        "2026-01-05", "2026-01-12", "2026-02-03", "2026-02-18", "2026-03-01",
        "2026-03-15", "2026-03-22", "2026-04-02", "2026-04-10", "2026-04-25"
    ],
    "category": [
        "Electronics", "Apparel", "Home", "Electronics", "Apparel",
        "Home", "Electronics", "Apparel", "Electronics", "Home"
    ],
    "quantity": [1, 3, 2, 2, 4, 1, 1, 2, 3, 2],
    "unit_price": [15000, 1200, 3500, 22000, 950, 4200, 18500, 1600, 12000, 2800]
}

df = pd.DataFrame(data)

df["total_sales"] = df["quantity"] * df["unit_price"]
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.strftime("%b %Y")

total_revenue = int(df["total_sales"].sum())
total_orders = int(len(df))
avg_order_val = int(df["total_sales"].mean())

category_sales = df.groupby("category")["total_sales"].sum().to_dict()

monthly_sales = df.groupby("month", sort=False)["total_sales"].sum().to_dict()

dashboard_payload = {
    "kpis": {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "avg_order_value": avg_order_val
    },
    "category_breakdown": {
        "labels": list(category_sales.keys()),
        "values": list(category_sales.values())
    },
    "monthly_trend": {
        "labels": list(monthly_sales.keys()),
        "values": list(monthly_sales.values())
    }
}

with open("dashboard_data.json", "w") as f:
    json.dump(dashboard_payload, f, indent=4)

print("Analytics pipeline ran successfully: 'dashboard_data.json' generated.")
