
import time
import sys
import httpx

url = "http://localhost:8000/predict"

payload = {
    "impact_speed": 60,
    "damage_score": 7,
    "airbag_deployed": 1
}

for attempt in range(1, 11):
    try:
        response = httpx.post(url, json=payload, timeout=5)
        response.raise_for_status()

        result = response.json()
        prediction = result.get("predicted_severity")

        if prediction:
            print(f"API Health Check Successful!")
            print(f"Predicted Severity: {prediction}")
            sys.exit(0)

        raise ValueError("Prediction was missing from API response")

    except Exception as error:
        print(f"Attempt {attempt}/10 failed: {error}")
        time.sleep(2)

print("API Health Check Failed!")
sys.exit(1)
