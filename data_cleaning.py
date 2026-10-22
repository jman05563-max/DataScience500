
import pandas as pd

# Load the raw dataset
df = pd.read_csv("books_raw.csv")

print("Original dataset shape:", df.shape)

# Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Remove duplicate books based on product URL
df = df.drop_duplicates(subset=["Product_URL"])

# Clean text columns
text_columns = ["Title", "Rating", "Availability", "Genre"]

for column in text_columns:
    df[column] = df[column].astype("string").str.strip()

# Convert prices to numeric values
df["Price_GBP"] = pd.to_numeric(
    df["Price_GBP"], errors="coerce"
)

# Convert ratings from words to numbers
rating_mapping = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating_Numeric"] = df["Rating"].map(rating_mapping)

# Convert stock quantities to numbers
df["Stock_Quantity"] = pd.to_numeric(
    df["Stock_Quantity"], errors="coerce"
)

# Standardise availability status
df["Availability"] = df["Availability"].str.strip()

# Replace missing genre values
df["Genre"] = df["Genre"].fillna("Unknown")

# Remove rows without valid price or rating
df = df.dropna(subset=["Price_GBP", "Rating_Numeric"])

# Remove invalid prices and ratings
df = df[
    (df["Price_GBP"] > 0) &
    (df["Rating_Numeric"].between(1, 5))
].copy()

# Keep missing stock quantities as unknown
# rather than incorrectly assuming zero stock

# Save cleaned dataset
df.to_csv("books_cleaned.csv", index=False)

print("\nCleaned dataset shape:", df.shape)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nFirst five cleaned records:")
print(df.head())

print("\nData cleaning completed successfully!")
print("Cleaned dataset saved as books_cleaned.csv")
