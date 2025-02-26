import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height, unit_system):
    if unit_system == "Imperial (lbs, inches)":
        return (weight / (height ** 2)) * 703  # BMI formula for imperial system
    else:
        height_m = height / 100  # Convert cm to meters for metric system
        return weight / (height_m ** 2)  # BMI formula for metric system

# Function to determine BMI category
def bmi_category(bmi, gender, age):
    if age < 9:
        return "Child BMI Category", "For children, BMI varies with age. Please consult a doctor."
    if gender == "Male":
        if bmi < 16.0:
            return "Severely Underweight 🥄", "Increase calorie intake with high-protein and nutrient-rich foods."
        elif 16.0 <= bmi < 18.5:
            return "Underweight 🍎", "Consider adding more healthy fats and proteins to your diet."
        elif 18.5 <= bmi < 22.9:
            return "Healthy Weight ✅", "Great! Keep up a balanced diet and stay active."
        elif 23.0 <= bmi < 24.9:
            return "Slightly Overweight ⚠", "A slight reduction in calorie intake and regular exercise can help."
        elif 25.0 <= bmi < 27.9:
            return "Overweight 🍔", "Try to maintain a calorie deficit and incorporate physical activities."
        elif 28.0 <= bmi < 34.9:
            return "Obese (Class 1) 🚨", "Focus on a structured diet and exercise plan."
        elif 35.0 <= bmi < 39.9:
            return "Obese (Class 2) ⚠", "Consider consulting a healthcare provider for a personalized plan."
        else:
            return "Severely Obese (Class 3) ❌", "Professional medical intervention is recommended."

    elif gender == "Female":
        if bmi < 15.5:
            return "Severely Underweight 🥄", "Increase healthy fat and protein intake, and avoid skipping meals."
        elif 15.5 <= bmi < 18.5:
            return "Underweight 🍏", "Focus on nutrient-rich foods and strength-building exercises."
        elif 18.5 <= bmi < 21.9:
            return "Healthy Weight ✅", "You're maintaining a great balance! Keep it up."
        elif 22.0 <= bmi < 23.9:
            return "Slightly Overweight ⚠", "A minor lifestyle adjustment can help maintain optimal weight."
        elif 24.0 <= bmi < 26.9:
            return "Overweight 🍟", "Engaging in regular physical activity will help control weight gain."
        elif 27.0 <= bmi < 32.9:
            return "Obese (Class 1) 🚨", "Monitor your eating habits and engage in routine workouts."
        elif 33.0 <= bmi < 38.9:
            return "Obese (Class 2) ⚠", "A structured diet plan with expert guidance is advised."
        else:
            return "Severely Obese (Class 3) ❌", "Consider medical consultation for effective weight management."

# Streamlit UI
st.title("BMI Calculator 🏋‍♂")
st.write("Enter your details to calculate your Body Mass Index (BMI).")

col1, col2 = st.columns(2)
with col1:
   # Gender selection
    gender = st.radio("Select your gender:", ["Male", "Female"], horizontal=True)
with col2:
 # Unit system selection
    unit_system = st.radio("Choose your unit system:", ["Metric", "Imperial"], horizontal=True)

# Age input
col_age, _ = st.columns([4, 4])  
with col_age:
    age = st.number_input("Your Age (1 year or above) *", min_value=1, step=1)

# Weight and height input based on unit system
col1, col2 = st.columns(2)

if unit_system == "Metric":
    with col1:
        height = st.number_input("Your Height (cm) *", min_value=50.0, step=0.1)  
    with col2:
        weight = st.number_input("Your Weight (kg) *", min_value=1.0, step=0.1)
else:
    with col1:
        height = st.number_input("Your Height (inches) *", min_value=20.0, step=0.1)
    with col2:
        weight = st.number_input("Your Weight (lbs) *", min_value=5.0, step=0.1)

# Calculate BMI when button is clicked
if st.button("Calculate BMI"):
    if weight > 0 and height > 0 and age > 0:
        bmi = calculate_bmi(weight, height, unit_system)
        category, suggestion = bmi_category(bmi, gender, age)

        # Display Results
        st.subheader(f"Your BMI: {bmi:.2f}")
        st.success(f"Category: {category}")
        st.info(suggestion)
    else:
        st.error("Please enter valid values for weight, height, and age.")
