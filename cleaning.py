import pandas as pd

print("=" * 50)
print("DATA ANALYTICS PROJECT 1")
print("=" * 50)

# Load dataset
df = pd.read_excel("dataset.xlsx")

# Dataset Information
print("\nRows and Columns:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())
print("Duplicate Order IDs:", df["OrderID"].duplicated().sum())

# -----------------------------
# Data Cleaning
# -----------------------------

# Fill missing CouponCode values
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

# Remove duplicate rows
df = df.drop_duplicates()

# Remove duplicate Order IDs
df = df.drop_duplicates(subset="OrderID")

# Standardize text columns
text_columns = [
    "Product",
    "ShippingAddress",
    "PaymentMethod",
    "OrderStatus",
    "ReferralSource"
]

for col in text_columns:
    df[col] = df[col].str.strip().str.title()

# Save cleaned dataset
df.to_excel("cleaned_dataset.xlsx", index=False)

# -----------------------------
# Final Verification
# -----------------------------

print("\nFinal Missing Values:")
print(df.isnull().sum())

print("\nFinal Duplicate Rows:", df.duplicated().sum())
print("Final Duplicate Order IDs:", df["OrderID"].duplicated().sum())

print("\n✅ Dataset cleaned successfully!")
print("✅ Cleaned file saved as cleaned_dataset.xlsx")