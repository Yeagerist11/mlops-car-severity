
import joblib
import pandas as pd
from pathlib import Path

# Location of the saved model
MODEL_PATH = Path("models") / "car_severity_model.joblib"


def test_model_file_exists():
    """Check that the saved model file exists."""
    assert MODEL_PATH.exists()


def test_model_can_predict():
    """Check that the model loads and predicts correctly."""
    model = joblib.load(MODEL_PATH)

    sample = pd.DataFrame([
        {
            "impact_speed": 72,
            "damage_score": 8,
            "airbag_deployed": 1
        }
    ])

    prediction = model.predict(sample)

    assert len(prediction) == 1
    assert prediction[0] in ["Moderate", "Severe"]
