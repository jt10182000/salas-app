import streamlit as st


st.header('PREDICTION SOURCE CODE 👨‍⚕️')
st.subheader('This python code is implemented for Streamlit')
st.code(''' 
 # Notes
# do a "pip install streamlit" first 
# to run on terminal issue this command
# python -m streamlit run streamlit_test.py

import streamlit as st
import pickle
from nltk.classify import NaiveBayesClassifier

filename = '/content/employee_attrition.sav'
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)

st.title("👨‍⚕️Employee Attrition Predictor")
st.subheader("Enter details to predict whether an employee will leave in the next 2 years:")

# User inputs for employee attrition prediction
education_input = st.selectbox("Education Level: ", ["Bachelors", "Masters", "PhD", "High School"])
joining_year_input = st.slider("Year of Joining: ", 2000, 2023, 2015)
city_input = st.selectbox("City: ", ["New York", "San Francisco", "Chicago", "Los Angeles", "Boston"])
payment_tier_input = st.selectbox("Payment Tier: ", [1, 2, 3])
age_input = st.slider("Age: ", 18, 70, 30)
gender_input = st.selectbox("Gender: ", ["Male", "Female"])
ever_benched_input = st.selectbox("Ever Benched: ", ["Yes", "No"])
experience_in_current_domain_input = st.slider("Experience in Current Domain (years): ", 0, 40, 5)

# Function to make a prediction
def predict_attrition(education, joining_year, city, payment_tier, age, gender, ever_benched, experience_in_current_domain):
    # Features function to convert inputs into a dictionary format expected by the model
    def features(education, joining_year, city, payment_tier, age, gender, ever_benched, experience_in_current_domain):
        return {
            'education': education,
            'joining_year': joining_year,
            'city': city,
            'payment_tier': payment_tier,
            'age': age,
            'gender': gender,
            'ever_benched': ever_benched,
            'experience_in_current_domain': experience_in_current_domain
        }

    # Apply features function to user inputs
    test_data = features(education, joining_year, city, payment_tier, age, gender, ever_benched, experience_in_current_domain)


    # Use the model to get the predicted attrition category
    prediction = loaded_model.classify(test_data)
    return prediction

# Display button and result
if st.button('Predict'):
    predicted_category = predict_attrition(education_input, joining_year_input, city_input, payment_tier_input, age_input, gender_input, ever_benched_input, experience_in_current_domain_input)
    st.text("The predicted attrition category based on the given details is:")
    st.text_area(label="", value=str(predicted_category), height=100)

''')