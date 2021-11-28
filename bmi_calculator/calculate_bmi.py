from warnings import warn
from typing import Tuple
import pandas as pd
from bmi_calculator.settings import JSON_INPUT_PATH, JSON_OUTPUT_PATH, BMI_RANGES, BMI_HEALTH_RISK


def calculate_bmi(weight: int, height: int) -> float:
    """
    calculate BMI given weight in kgs and height in cms
    :param weight: weight in kgs
    :param height: height in cms
    :return: BMI
    """
    if weight <= 0:
        warn("Weight can not take negative values.")
        return None
    elif height <= 0:
        warn("Height can not take negative values.")
        return None
    else:
        return round(float(weight) * 10000 / height ** 2, 1)


def get_bmi_range(bmi: float) -> str:
    """
    get the BMI range associated to the BMI value using the settings dict giving the match
    :param bmi: BMI value
    :return: BMI range
    """
    for bmi_range in BMI_RANGES:
        if bmi <= bmi_range["BMI upper limit"]:
            return bmi_range["BMI Category"]
    return None


def add_bmi_range(data_pd: pd.DataFrame) -> pd.DataFrame:
    """
    add in giving pandas dataframe with "bmi" column containing BMI values, a column with the BMI range and a column
    with the associated health risk
    :param data_pd: input dataframe with "bmi" column
    :return: output dataframe with 'BMICategory' and 'BMICategory' columns added
    """
    result_pd = data_pd.copy()
    result_pd["bmi"] = result_pd.apply(lambda r: calculate_bmi(r.WeightKg, r.HeightCm), axis=1)
    result_pd["BMICategory"] = result_pd["bmi"].map(get_bmi_range)
    result_pd["HealthRisk"] = result_pd["BMICategory"].map(BMI_HEALTH_RISK)
    return result_pd


def main():
    """
    read patients data from a json file
    add "bmi", 'BMICategory' and 'BMICategory' columns
    display the number of overweight people
    write resulting table in a json file
    """
    data_pd = pd.read_json(JSON_INPUT_PATH)
    data_pd = add_bmi_range(data_pd)
    print(f"Number of overweight people : {(data_pd['BMICategory'] == 'Overweight').sum()}")
    data_pd.to_json(JSON_OUTPUT_PATH, orient='records')


if __name__ == '__main__':
    main()
