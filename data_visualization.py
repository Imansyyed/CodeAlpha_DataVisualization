import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("data/sample_-_superstore.xls")

# Create visualizations folder
import os
os.makedirs("visualizations", exist_ok=True)


# 1. Sales by Category
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
plt.bar(category_sales.index, category_sales.values)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualizations/sales_by_category.png")
plt.show()


# 2. Profit by Region
region_profit = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
plt.bar(region_profit.index, region_profit.values)
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.savefig("visualizations/profit_by_region.png")
plt.show()


# 3. Sales by Sub-Category
subcategory_sales = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
plt.barh(subcategory_sales.index, subcategory_sales.values)
plt.title("Sales by Sub-Category")
plt.xlabel("Total Sales")
plt.ylabel("Sub-Category")
plt.tight_layout()
plt.savefig("visualizations/sales_by_subcategory.png")
plt.show()


# 4. Monthly Sales Trend
df["Order Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Order Month")["Sales"].sum()

plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/monthly_sales_trend.png")
plt.show()


print("Data Visualization completed successfully!")