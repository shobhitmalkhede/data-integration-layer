import pandas as pd

# Mock dataset
data = {
    "user_id": "12345",
    "metrics": [
        {"date": "2024-11-22", "steps": 8500, "heart_rate": 75, "sleep_hours": 6.5, "hrv": 45},
        {"date": "2024-11-21", "steps": 9500, "heart_rate": 72, "sleep_hours": 7.2, "hrv": 50}
    ]
}

# Convert the data into a DataFrame (like a table)
metrics = pd.DataFrame(data["metrics"])

# Save the normalized data as a JSON file
metrics.to_json("health_metrics_normalized.json", orient="records", indent=4)

print("\nData has been saved to health_metrics_normalized.json!")
