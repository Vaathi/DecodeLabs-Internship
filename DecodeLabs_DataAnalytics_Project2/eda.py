import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==================================================
# DecodeLabs Project 2 - Exploratory Data Analysis
# ==================================================

print("=" * 60)
print("DECODELABS - PROJECT 2")
print("EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 60)

# Load Dataset
df = pd.read_excel("cleaned_dataset.xlsx")

# Create graphs folder
os.makedirs("graphs", exist_ok=True)

# ==================================================
# Dataset Information
# ==================================================

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nRows and Columns:")
print(df.shape)

# ==================================================
# Missing Values
# ==================================================

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)
print(df.isnull().sum())

# ==================================================
# Duplicate Check
# ==================================================

print("\nDuplicate Rows:", df.duplicated().sum())
print("Duplicate Order IDs:", df["OrderID"].duplicated().sum())

# ==================================================
# Descriptive Statistics
# ==================================================

print("\n" + "=" * 60)
print("DESCRIPTIVE STATISTICS")
print("=" * 60)

print(df.describe())

# ==================================================
# Mean
# ==================================================

print("\nMEAN")
print(df.mean(numeric_only=True))

# ==================================================
# Median
# ==================================================

print("\nMEDIAN")
print(df.median(numeric_only=True))

# ==================================================
# Mode
# ==================================================

print("\nMODE")
print(df.mode().iloc[0])

# ==================================================
# Revenue Analysis
# ==================================================

print("\n" + "=" * 60)
print("REVENUE")
print("=" * 60)

print("Total Revenue :", round(df["TotalPrice"].sum(), 2))
print("Average Revenue :", round(df["TotalPrice"].mean(), 2))

# ==================================================
# Top Products
# ==================================================

print("\nTop Selling Products")

top_products = df["Product"].value_counts()

print(top_products)

# ==================================================
# Payment Methods
# ==================================================

print("\nPayment Methods")

print(df["PaymentMethod"].value_counts())

# ==================================================
# Order Status
# ==================================================

print("\nOrder Status")

print(df["OrderStatus"].value_counts())

# ==================================================
# Referral Source
# ==================================================

print("\nReferral Source")

print(df["ReferralSource"].value_counts())

# ==================================================
# Monthly Sales
# ==================================================

df["Month"] = df["Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["TotalPrice"].sum()

print("\nMonthly Sales")

print(monthly_sales)

# ==================================================
# Correlation
# ==================================================

print("\nCorrelation Matrix")

numeric_df = df.select_dtypes(include=["number"])

print(numeric_df.corr())

# ==================================================
# Graph 1 Histogram
# ==================================================

plt.figure(figsize=(8,5))
plt.hist(df["TotalPrice"], bins=20)
plt.title("Total Price Distribution")
plt.xlabel("Total Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("graphs/totalprice_histogram.png")
plt.close()

# ==================================================
# Graph 2 Boxplot
# ==================================================

plt.figure(figsize=(8,5))
plt.boxplot(df["TotalPrice"])
plt.title("Total Price Boxplot")
plt.ylabel("Total Price")
plt.tight_layout()
plt.savefig("graphs/totalprice_boxplot.png")
plt.close()

# ==================================================
# Graph 3 Top Products
# ==================================================

plt.figure(figsize=(10,5))
top_products.plot(kind="bar")
plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("graphs/top_products.png")
plt.close()

# ==================================================
# Graph 4 Payment Method
# ==================================================

plt.figure(figsize=(8,5))
df["PaymentMethod"].value_counts().plot(kind="bar")
plt.title("Payment Methods")
plt.xlabel("Payment Method")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("graphs/payment_method.png")
plt.close()

# ==================================================
# Graph 5 Order Status
# ==================================================

plt.figure(figsize=(8,5))
df["OrderStatus"].value_counts().plot(kind="bar")
plt.title("Order Status")
plt.xlabel("Status")
plt.ylabel("Orders")
plt.tight_layout()
plt.savefig("graphs/order_status.png")
plt.close()

# ==================================================
# Graph 6 Monthly Sales
# ==================================================

plt.figure(figsize=(10,5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.savefig("graphs/monthly_sales.png")
plt.close()

# ==================================================
# Graph 7 Correlation Heatmap
# ==================================================

plt.figure(figsize=(8,6))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("graphs/correlation_heatmap.png")
plt.close()

# ==================================================
# Outlier Detection
# ==================================================

Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["TotalPrice"] < lower)
    | (df["TotalPrice"] > upper)
]

print("\nOutliers Found:", len(outliers))

# ==================================================
# Final Summary
# ==================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print(f"Total Records : {len(df)}")
print(f"Total Columns : {len(df.columns)}")
print(f"Missing Values : {df.isnull().sum().sum()}")
print(f"Duplicate Rows : {df.duplicated().sum()}")
print(f"Outliers : {len(outliers)}")

print("\nGraphs saved successfully in 'graphs' folder.")

print("\nPROJECT 2 COMPLETED SUCCESSFULLY")
print("=" * 60)