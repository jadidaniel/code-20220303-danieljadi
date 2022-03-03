import bmi_calculator
import pandas as pd

# loading the random json data
loaded_data = pd.read_json('random_test_data.json')
# print(loaded_data)

bmi_calculator.bmi_main(loaded_data)
