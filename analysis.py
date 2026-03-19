import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("train.csv")

print(data.head())
print(data.info())
print("shape \n ",data.shape)
print("columns \n ",data.columns)

data = data.dropna()
print(data.isnull().sum())

# total Sales/ total revenue
print("total sales ", data["Sales"].sum())

# find which product category sells the most.
category_sales= data.groupby("Category")["Sales"].sum()

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.show()

# Which products generate the most revenue?

top_products = data.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

top_products.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Total Sales")

plt.show()

# How sales change over time

data["Order Date"]= pd.to_datetime(data["Order Date"], dayfirst=True)
data["YearMonth"] = data["Order Date"].dt.to_period("M")    #Extract Year-Month
monthly_Sales = data.groupby("YearMonth")["Sales"].sum()

monthly_Sales.plot()

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.show()

# Which region generates the most revenue

region_sales = data.groupby("Region")["Sales"].sum()

region_sales.plot()

plt.show()