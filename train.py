
import pandas as pd
import joblib
import mlflow

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

# 2. Convert the data into a DataFrame
df = pd.DataFrame(data)

# 3. Separate input features (X) and target (y)
X = df[["impact_speed", "damage_score", "airbag_deployed"]]
y = df["severity"]

# 4. Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# 5. Create the Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# 6. Create the directory for saving models
model_dir = Path("models")
model_dir.mkdir(exist_ok=True)

model_path = model_dir / "car_severity_model.joblib"

# 7. Set up the MLflow experiment
mlflow.set_experiment("Car Severity Classification")

# 8. Start an MLflow run
with mlflow.start_run() as run:

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, predictions)

    # Save the trained model
    joblib.dump(model, model_path)

    # 9. Log model parameters
    mlflow.log_param("model_type", "RandomForestClassifier")
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("random_state", 42)
    mlflow.log_param("test_size", 0.25)
    mlflow.log_param("training_samples", len(X_train))

    # 10. Log evaluation metrics
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("test_samples", len(X_test))

    # 11. Log the saved model file as an artifact
    mlflow.log_artifact(
        str(model_path),
        artifact_path="model_files"
    )

    # 12. Display results
    print("Model training completed!")
    print("Training examples:", len(X_train))
    print("Testing examples:", len(X_test))
    print("Model accuracy:", accuracy)
    print("Model saved successfully!")
    print("Saved model location:", model_path)
    print("MLflow experiment: Car Severity Classification")
    print("MLflow Run ID:", run.info.run_id)

print("Experiment tracking completed!")
