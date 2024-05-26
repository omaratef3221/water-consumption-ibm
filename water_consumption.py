import streamlit as st

def calculate_water_consumption(family_size, activities_usage):
    """
    Calculate the total daily water consumption based on the number of family members and usage of different activities.
    
    :param family_size: int, number of family members
    :param activities_usage: dict, keys are activities and values are tuples of (frequency per day, duration or units if applicable)
    :return: float, total daily water consumption in liters
    """
    # Data structure as extracted from the Excel
    activities_data = {
        'Cooking Purposes': {'unit': 'Liter/Day', 'water_per_unit': 3},
        'Washing Dishes - Hand Wash': {'unit': 'Liter/Load', 'water_per_unit': 100},
        'Washing Dishes - Dish Washer': {'unit': 'Liter/Load', 'water_per_unit': 15},
        'General Cleaning': {'unit': 'Liter/Minute', 'water_per_unit': 20}
    }
    
    total_water = 0
    for activity, usage in activities_usage.items():
        freq_per_day, duration_or_units = usage
        water_per_unit = activities_data[activity]['water_per_unit']
        
        if activities_data[activity]['unit'] in ['Liter/Day']:
            total_water += water_per_unit * freq_per_day * family_size
        elif activities_data[activity]['unit'] in ['Liter/Load', 'Liter/Minute']:
            total_water += water_per_unit * freq_per_day * duration_or_units * family_size
    
    return total_water

def main():
    st.title("Daily Water Consumption Calculator")

    family_size = st.number_input("Enter the number of family members:", min_value=1, value=1, step=1)

    activities_usage = {}

    st.header("Usage of Various Household Activities")

    activities = [
        ('Cooking Purposes', 'How many times do you cook per day?'),
        ('Washing Dishes - Hand Wash', 'How many times do you wash dishes by hand per day?'),
        ('Washing Dishes - Dish Washer', 'How many times do you use the dishwasher per day?'),
        ('General Cleaning', 'How many minutes do you spend on general cleaning per day?')
    ]

    for activity, question in activities:
        freq_per_day = st.number_input(question, min_value=0, value=0, step=1, key=f"{activity}_frequency")
        if activity == 'General Cleaning':
            duration = st.number_input("How many minutes per session?", min_value=1, value=1, step=1, key=f"{activity}_duration")
        else:
            duration = 1  # default duration for other activities

        activities_usage[activity] = (freq_per_day, duration)

    if st.button("Calculate Total Water Consumption"):
        total_water = calculate_water_consumption(family_size, activities_usage)
        st.success(f"Total daily water consumption is {total_water} liters.")

if __name__ == '__main__':
    main()
