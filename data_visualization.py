
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Load the cleaned dataset
df = pd.read_csv("books_cleaned.csv")

# Create folder to save graphs
output_folder = Path("graphs")
output_folder.mkdir(exist_ok=True)

# Set visual style
sns.set_theme(style="whitegrid")

# GRAPH 1: Distribution of book prices
plt.figure(figsize=(10, 6))
sns.histplot(
    data=df,
    x="Price_GBP",
    bins=20,
    kde=True
)
plt.title("Distribution of Book Prices")
plt.xlabel("Price (GBP)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig(output_folder / "price_distribution.png", dpi=300)
plt.show()

# GRAPH 2: Number of books by star rating
plt.figure(figsize=(10, 6))
sns.countplot(
    data=df,
    x="Rating_Numeric",
    order=[1, 2, 3, 4, 5]
)
plt.title("Number of Books by Star Rating")
plt.xlabel("Star Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig(output_folder / "rating_distribution.png", dpi=300)
plt.show()

# GRAPH 3: Average price by genre (top 10)
top_genres = df["Genre"].value_counts().head(10).index

genre_prices = (
    df[df["Genre"].isin(top_genres)]
    .groupby("Genre")["Price_GBP"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 7))
sns.barplot(
    x=genre_prices.values,
    y=genre_prices.index
)
plt.title("Average Book Price by Genre (10 Most Common Genres)")
plt.xlabel("Average Price (GBP)")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig(output_folder / "genre_prices.png", dpi=300)
plt.show()

# GRAPH 4: Relationship between rating and price
plt.figure(figsize=(10, 6))
sns.boxplot(
    data=df,
    x="Rating_Numeric",
    y="Price_GBP",
    order=[1, 2, 3, 4, 5]
)
plt.title("Book Prices Across Star Ratings")
plt.xlabel("Star Rating")
plt.ylabel("Price (GBP)")
plt.tight_layout()
plt.savefig(output_folder / "price_vs_rating.png", dpi=300)
plt.show()

# Print descriptive statistics
print("\nBOOK PRICE STATISTICS")
print(df["Price_GBP"].describe())

print("\nAVERAGE PRICE BY RATING")
print(df.groupby("Rating_Numeric")["Price_GBP"].mean())

print("\nTOP 10 GENRES BY NUMBER OF BOOKS")
print(df["Genre"].value_counts().head(10))

print("\nAll four graphs saved successfully!")
