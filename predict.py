
import joblib
import pandas as pd
from pathlib import Path

# 1. Find the saved model
model_path = Path("models") / "car_severity_model.joblib"

# 2. Load the trained model
model = joblib.load(model_path)

# 3. Prepare new accident details
new_accident = pd.DataFrame([
    {
        "impact_speed": 72,
        "damage_score": 8,
        "airbag_deployed": 1
    }
])

# 4. Predict the severity
prediction = model.predict(new_accident)

# 5. Display the result
print("Predicted accident severity:", prediction[0])
