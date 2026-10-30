
import joblib
import pandas as pd
from pathlib import Path

# Load the trained model
model_path = Path("models/car_severity_model.joblib")
model = joblib.load(model_path)

# Get accident details from the user
speed = float(input("Enter impact speed: "))
damage = int(input("Enter damage score (1-10): "))
airbag = int(input("Was the airbag deployed? (1 = Yes, 0 = No): "))

# Prepare input in the same format used during training
accident = pd.DataFrame([{
    "impact_speed": speed,
    "damage_score": damage,
    "airbag_deployed": airbag
}])

# Predict severity
prediction = model.predict(accident)

print("Predicted accident severity:", prediction[0])
