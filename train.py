
import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Create a small practice dataset
data = {
    "impact_speed": [25, 30, 35, 40, 45, 50, 60, 65, 70, 75, 80, 85],
    "damage_score": [1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 9, 10],
    "airbag_deployed": [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    "severity": [
        "Moderate", "Moderate", "Moderate",
        "Moderate", "Moderate", "Moderate",
        "Severe", "Severe", "Severe",
        "Severe", "Severe", "Severe"
    ]
}

# 2. Convert the data into a table
df = pd.DataFrame(data)

# 3. Separate inputs (X) and answers (y)
X = df[["impact_speed", "damage_score", "airbag_deployed"]]
y = df["severity"]

# 4. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# 5. Create the machine learning model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# 6. Train the model
model.fit(X_train, y_train)

# 7. Predict severity for the test examples
predictions = model.predict(X_test)

# 8. Evaluate the predictions
accuracy = accuracy_score(y_test, predictions)

print("Model training completed!")
print("Number of training examples:", len(X_train))
print("Number of testing examples:", len(X_test))
print("Model accuracy:", accuracy)

# 9. Create the folder for saved models
model_dir = Path("models")
model_dir.mkdir(exist_ok=True)

# 10. Save the trained model
model_path = model_dir / "car_severity_model.joblib"
joblib.dump(model, model_path)

print("Model saved successfully!")
print("Saved model location:", model_path)