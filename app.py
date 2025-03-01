import streamlit as st
import pickle
import os
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Multiple Disease Prediction", layout="wide", page_icon="🏥")

working_dir = os.path.dirname(os.path.abspath(__file__))

# Load Models
heart_disease_model = pickle.load(open(f'{working_dir}/models/heart.pkl', 'rb'))
kidney_disease_model = pickle.load(open(f'{working_dir}/models/kidney.pkl', 'rb'))

# Sidebar Menu
with st.sidebar:
    selected = option_menu("Multiple Disease Prediction",
                ['Heart Disease Prediction',
                 'Kidney Disease Prediction'],
                 menu_icon='hospital-fill',
                 icons=['heart', 'droplet'],
                 default_index=0,
                 styles={
                     "container": {"padding": "5px"},
                     "nav-link-selected": {"background-color": "#ff4b4b"},
                     "icon": {"color": "white"}
                 })

# Function for styled result box
def display_result(message, success=True):
    color = "#4CAF50" if success else "#FF4B4B"
    st.markdown(f'<div style="background-color:{color}; padding: 15px; border-radius: 8px; text-align: center; font-size:18px; font-weight:bold; color:white;">{message}</div>', unsafe_allow_html=True)

if selected == 'Heart Disease Prediction':
    st.title("\U0001F493 Heart Disease Prediction")
    st.subheader("Enter the details below:")

    with st.form("heart_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            age = st.number_input("Age", min_value=1, max_value=120, step=1)
            trestbps = st.number_input("Resting Blood Pressure")
            fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", [0, 1])
            oldpeak = st.number_input("ST Depression Induced by Exercise")
        
        with col2:
            sex = st.radio("Sex", [0, 1])
            chol = st.number_input("Serum Cholesterol in mg/dl")
            restecg = st.radio("Resting Electrocardiographic results", [0, 1, 2])
            slope = st.radio("Slope of peak exercise ST segment", [0, 1, 2])
            
        with col3:
            cp = st.radio("Chest Pain Type", [0, 1, 2, 3])
            thalach = st.number_input("Maximum Heart Rate Achieved")
            exang = st.radio("Exercise Induced Angina", [0, 1])
            ca = st.number_input("Major vessels colored by fluoroscopy", min_value=0, max_value=4, step=1)
            thal = st.radio("Thalassemia", [0, 1, 2, 3])

        submitted = st.form_submit_button("Predict Heart Disease", use_container_width=True)
        
        if submitted:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            prediction = heart_disease_model.predict([user_input])
            if prediction[0] == 1:
                display_result("This person is likely to have heart disease", success=False)
            else:
                display_result("This person is not likely to have heart disease")

if selected == 'Kidney Disease Prediction':
    st.title("\U0001F4A7 Kidney Disease Prediction")
    st.subheader("Enter the details below:")

    with st.form("kidney_form"):
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            age = st.number_input("Age", min_value=1, max_value=120, step=1)
            red_blood_cells = st.radio("Red Blood Cells", [0, 1])
            blood_glucose_random = st.number_input("Blood Glucose Random")
            packed_cell_volume = st.number_input("Packed Cell Volume")
            coronary_artery_disease = st.radio("Coronary Artery Disease", [0, 1])

        with col2:
            blood_pressure = st.number_input("Blood Pressure")
            pus_cell = st.radio("Pus Cell", [0, 1])
            blood_urea = st.number_input("Blood Urea")
            white_blood_cell_count = st.number_input("White Blood Cell Count")
            appetite = st.radio("Appetite", [0, 1])

        with col3:
            specific_gravity = st.number_input("Specific Gravity")
            pus_cell_clumps = st.radio("Pus Cell Clumps", [0, 1])
            serum_creatinine = st.number_input("Serum Creatinine")
            red_blood_cell_count = st.number_input("Red Blood Cell Count")
            peda_edema = st.radio("Pedal Edema", [0, 1])

        with col4:
            albumin = st.number_input("Albumin")
            bacteria = st.radio("Bacteria", [0, 1])
            sodium = st.number_input("Sodium")
            hypertension = st.radio("Hypertension", [0, 1])
            anemia = st.radio("Anemia", [0, 1])

        with col5:
            sugar = st.number_input("Sugar")
            potassium = st.number_input("Potassium")
            haemoglobin = st.number_input("Haemoglobin")
            diabetes_mellitus = st.radio("Diabetes Mellitus", [0, 1])
        
        submitted = st.form_submit_button("Predict Kidney Disease", use_container_width=True)

        if submitted:
            user_input = [age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell, pus_cell_clumps, 
                          bacteria, blood_glucose_random, blood_urea, serum_creatinine, sodium, potassium, haemoglobin, 
                          packed_cell_volume, white_blood_cell_count, red_blood_cell_count, hypertension, diabetes_mellitus, 
                          coronary_artery_disease, appetite, peda_edema, anemia]
            prediction = kidney_disease_model.predict([user_input])
            if prediction[0] == 1:
                display_result("The person has kidney disease", success=False)
            else:
                display_result("The person does not have kidney disease")
