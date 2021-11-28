from unittest import TestCase
from pandas.testing import assert_frame_equal
import pandas as pd
from bmi_calculator.calculate_bmi import calculate_bmi, get_bmi_range, add_bmi_range


class TestTools(TestCase):
    def setUp(self):
        self.input_data_pd = pd.DataFrame(data=[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
                                                {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
                                                {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
                                                {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
                                                {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
                                                {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}])
        self.output_data_pd = pd.DataFrame(data=[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96, "bmi": 32.8,
                                                  "BMICategory": "Moderately obese", "HealthRisk": "Medium risk"},
                                                 {"Gender": "Male", "HeightCm": 161, "WeightKg": 85, "bmi": 32.8,
                                                  "BMICategory": "Moderately obese", "HealthRisk": "Medium risk"},
                                                 {"Gender": "Male", "HeightCm": 180, "WeightKg": 77, "bmi": 23.8,
                                                  "BMICategory": "Normal weight", "HealthRisk": "Low risk"},
                                                 {"Gender": "Female", "HeightCm": 166, "WeightKg": 62, "bmi": 22.5,
                                                  "BMICategory": "Normal weight", "HealthRisk": "Low risk"},
                                                 {"Gender": "Female", "HeightCm": 150, "WeightKg": 70, "bmi": 31.1,
                                                  "BMICategory": "Moderately obese", "HealthRisk": "Medium risk"},
                                                 {"Gender": "Female", "HeightCm": 167, "WeightKg": 82, "bmi": 29.4,
                                                  "BMICategory": "Overweight", "HealthRisk": "Enhanced risk"}])

    def test_calculate_bmi(self):
        self.assertEqual(calculate_bmi(10, 100), 10)
        self.assertEqual(calculate_bmi(2, 200), 0.5)
        self.assertEqual(calculate_bmi(0, 1), None)
        self.assertEqual(calculate_bmi(1, -1), None)

    def test_get_bmi_range(self):
        self.assertEqual(get_bmi_range(10), "Underweight")
        self.assertEqual(get_bmi_range(20), "Normal weight")
        self.assertEqual(get_bmi_range(29.9), "Overweight")
        self.assertEqual(get_bmi_range(33), "Moderately obese")
        self.assertEqual(get_bmi_range(39.9), "Severely obese")
        self.assertEqual(get_bmi_range(50), "Very severely obese")

    def test_add_bmi_range(self):
        assert_frame_equal(add_bmi_range(self.input_data_pd), self.output_data_pd)
