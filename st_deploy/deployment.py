import pandas as pd
import streamlit as st
from joblib import load
from sklearn.metrics import accuracy_score

# model = load('sleep_model.joblib')

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'sleep_model.joblib')
model = load(model_path)


try:
  x_test = pd.read_csv('st_deploy/x_test.csv')
  y_test = pd.read_csv('st_deploy/y_test.csv')
  y_test = y_test.squeeze()
  show_accuracy = True
except:
  show_accuracy = False

st.set_page_config(page_title='How did you rest today?', layout='centered')

st.markdown(
    """
    <h1 style='text-align: center; font-size: 50px; color: #4CAF50;'>Sleep Quality Predictor</h1>
    """,
    unsafe_allow_html=True
)

st.markdown('Curious about your sleep quality? Just fill in a few details and let this app predict how well you’re sleeping!')

age = st.number_input("Age", min_value=0, max_value=120, value=25)

gender = st.selectbox("Gender", ["Male", "Female"])
gender_encoded = 0 if gender == "Male" else 1

sleep_start = st.number_input("Sleep Start Time (e.g., 22.5 for 10:30 PM)", min_value=0.0, max_value=24.0)
sleep_end = st.number_input("Sleep End Time (e.g., 6.5 for 6:30 AM)", min_value=0.0, max_value=24.0)

total_sleep = st.number_input("Total Sleep Hours", min_value=0.0, max_value=24.0)

exercise = st.number_input("Exercise (mins/day)", min_value=0, max_value=300)
caffeine = st.number_input("Caffeine Intake (mg)", min_value=0, max_value=1000)
screen_time = st.number_input("Screen Time Before Bed (mins)", min_value=0, max_value=300)

work_hours = st.number_input("Work Hours (hrs/day)", min_value=0.0, max_value=24.0)

productivity = st.slider("Productivity Score (1–10)", min_value=1, max_value=10, value=5)
mood = st.slider("Mood Score (1–10)", min_value=1, max_value=10, value=5)
stress = st.slider("Stress Level (1–10)", min_value=1, max_value=10, value=5)

nap_duration = st.number_input("Nap Duration (hours)", min_value=0.0, max_value=5.0)

room_environment = st.slider("Room Environment (1–10)", min_value=1, max_value=10, value=5)

input_data = [
    age,
    gender_encoded,
    sleep_start,
    sleep_end,
    total_sleep,
    exercise,
    caffeine,
    screen_time,
    work_hours,
    productivity,
    mood,
    stress,
    nap_duration,
    room_environment
]

if st.button("Predict Sleep Quality 😴"):
    input_df = pd.DataFrame([{
        'Age': age,
        'Gender': gender_encoded,
        'Sleep Start Time': sleep_start,
        'Sleep End Time': sleep_end,
        'Total Sleep Hours': total_sleep,
        'Exercise (mins/day)': exercise,
        'Caffeine Intake (mg)': caffeine,
        'Screen Time Before Bed (mins)': screen_time,
        'Work Hours (hrs/day)': work_hours,
        'Productivity Score': productivity,
        'Mood Score': mood,
        'Stress Level': stress,
        'Nap Duration': nap_duration,
        'Room Environment': room_environment
    }])

    prediction = model.predict(input_df)[0]

    st.success(f"🛌 Predicted Sleep Quality: {prediction}")

if show_accuracy:
        from sklearn.metrics import accuracy_score

        y_pred = model.predict(x_test)
        score = accuracy_score(y_test, y_pred)
        st.metric('Accuracy score:', f"{score:.2f}")
else:
        st.info('Test data not available to evaluate the model.')

import os


