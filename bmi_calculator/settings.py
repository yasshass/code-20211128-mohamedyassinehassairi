import os
from decouple import config

JSON_INPUT_PATH = config('JSON_INPUT_PATH', default=os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))), os.path.join("data", "data.json")))

JSON_OUTPUT_PATH = config('JSON_OUTPUT_PATH', default=os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))), os.path.join("data", "output_data.json")))

BMI_RANGES = [{"BMI Category": "Underweight", "BMI upper limit": 18.4},
              {"BMI Category": "Normal weight", "BMI upper limit":  24.9},
              {"BMI Category": "Overweight", "BMI upper limit":  29.9},
              {"BMI Category": "Moderately obese", "BMI upper limit":  34.9},
              {"BMI Category": "Severely obese", "BMI upper limit":  39.9},
              {"BMI Category": "Very severely obese", "BMI upper limit":  1000}
              ]

BMI_HEALTH_RISK = {"Underweight": "Malnutrition risk",
                   "Normal weight": "Low risk",
                   "Overweight": "Enhanced risk",
                   "Moderately obese": "Medium risk",
                   "Severely obese": "High risk",
                   "Very severely obese": "Very high risk"}
