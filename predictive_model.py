
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# STEP 1: Load the cleaned dataset
df = pd.read_csv("books_cleaned.csv")

# STEP 2: Create an additional feature
df["Title_Length"] = df["Title"].fillna("").str.len()

# STEP 3: Select input features and target
features = [
    "Rating_Numeric",
    "Genre",
    "Stock_Quantity",
    "Title_Length"
]

X = df[features]
y = df["Price_GBP"]

# STEP 4: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# STEP 5: Prepare numerical and categorical features
numeric_features = [
    "Rating_Numeric",
    "Stock_Quantity",
    "Title_Length"
]

categorical_features = ["Genre"]

numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median"))
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(
        strategy="constant",
        fill_value="Unknown"
    )),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

# STEP 6: Build Linear Regression model
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# STEP 7: Train the model
model.fit(X_train, y_train)

# STEP 8: Predict prices
y_pred = model.predict(X_test)

# STEP 9: Evaluate model performance
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nLINEAR REGRESSION MODEL RESULTS")
print("--------------------------------")
print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print(f"Mean Absolute Error: £{mae:.2f}")
print(f"Mean Squared Error: {mse:.2f}")
print(f"Root Mean Squared Error: £{rmse:.2f}")
print(f"R-squared Score: {r2:.4f}")

# STEP 10: Save actual and predicted prices
results = pd.DataFrame({
    "Actual_Price": y_test.to_numpy(),
    "Predicted_Price": y_pred
})

results.to_csv("model_predictions.csv", index=False)

# STEP 11: Plot actual vs predicted prices
Path("graphs").mkdir(exist_ok=True)

plt.figure(figsize=(10, 6))
plt.scatter(
    y_test,
    y_pred,
    alpha=0.6
)

minimum = min(y_test.min(), y_pred.min())
maximum = max(y_test.max(), y_pred.max())

plt.plot(
    [minimum, maximum],
    [minimum, maximum],
    "r--",
    label="Perfect Prediction"
)

plt.xlabel("Actual Book Price (GBP)")
plt.ylabel("Predicted Book Price (GBP)")
plt.title("Actual vs Predicted Book Prices")
plt.legend()
plt.tight_layout()

plt.savefig(
    "graphs/actual_vs_predicted.png",
    dpi=300
)

plt.show()

print("\nModel training completed successfully!")
print("Predictions saved as model_predictions.csv")
print("Graph saved as graphs/actual_vs_predicted.png")
