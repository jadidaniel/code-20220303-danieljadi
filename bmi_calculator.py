import pandas as pd

# given input data
input_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
              {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
              {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
              {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
              {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
              {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

# print(input_data)
# print(type(input_data))

'''
given Table information:

BMI Category        BMI Range (kg/m2)      Health risk

Underweight          18.4 and below         Malnutrition risk
Normal weight        18.5 - 24.9            Low risk
Overweight           25 - 29.9              Enhanced risk
Moderately obese     30 - 34.9              Medium risk
Severely obese       35 - 39.9              High risk
Very severely obese  40 and above           Very high risk
'''

# defining the function to categorize the bmi category based on the bmi range calculated.
def bmi_category(bmi_range):
    if bmi_range <= 18.4:
        return 'Underweight'
    elif 18.5 < bmi_range < 24.9:
        return 'Normal weight'
    elif 25 < bmi_range < 29.9:
        return 'Overweight'
    elif 30 < bmi_range < 34.9:
        return 'Moderately obese'
    elif 35 < bmi_range < 39.9:
        return 'Severely obese'
    else:
        return 'Very severely obese'

# defining the function to categorize the health risk based on the bmi range calculated.
def health_risk_category(bmi_range):
    if bmi_range <= 18.4:
        return 'Malnutrition risk'
    elif 18.5 < bmi_range < 24.9:
        return 'Low risk'
    elif 25 < bmi_range < 29.9:
        return 'Enhanced risk'
    elif 30 < bmi_range < 34.9:
        return 'Medium risk'
    elif 35 < bmi_range < 39.9:
        return 'High risk'
    else:
        return 'Very high risk'


def bmi_main(input_data):
    data = pd.DataFrame.from_dict(input_data)
    # calculating the BMI using the formula BMI(kg/m2) = mass(kg) / height(m)2
    # and also converting the height variable from centimeter to meter
    data["BMI(kg/m2)"] = round((data["WeightKg"] / (data["HeightCm"] / 100)), 2)

    # Creating the BMI Category column and adding it to the main data frame
    data['BMI_Category'] = data['BMI(kg/m2)'].apply(bmi_category)

    # Creating the Health risk column and adding it to the main data frame
    data['Health_Risk'] = data['BMI(kg/m2)'].apply(health_risk_category)
    print(data, '\n')

    # Total number of Overweight people
    count_overweight = sum(map(lambda x: 25 < x < 29.9, data['BMI(kg/m2)']))
    print("The total number of over weight people are:", count_overweight)

    count_overweight_general = sum(map(lambda x: x > 25, data['BMI(kg/m2)']))
    print("The total number of over weight people in a general context are:", count_overweight_general)

    ''' Observation: From the above analysis, I can clearly say that there are no persons who are Over weight 
    (BMI range 25 - 29.9). If this is scaled to high volume data then we can find the count it. But, if we are 
    interested to find the over weight persons in general without the BMI range then the count of over weight 
    people are 6 '''


if __name__ == "__main__":
    bmi_main(input_data)

