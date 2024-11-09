import pickle
import streamlit as st 

with open('random_forest_model_numpy.pkl', 'rb') as file:
    loaded_numpy_model = pickle.load(file)

st.title('Prediksi Serangan Jantung')

col1,col2 = st.columns(2)
with col1:  
    age = st.text_input ('Input Usia                                    : ')
with col1:  
    sex = st.text_input ('Input Jenis Kelamin                           : ')
with col1:
    cp = st.text_input ('Input nilai Chest Pain Type                    : ')
with col1:
    trtbps = st.text_input ('Input nilai Resting Blood Pressure (trtbps): ')
with col1:
    chol = st.text_input ('Input nilai Cholesterol (chol)               : ')
with col1:
    fbs = st.text_input ('Input nilai Fasting Blood Sugar (fbs)         : ')
with col1:
    restecg = st.text_input ('Input nilai Resting ECG (restecg)         : ')
with col2:
    thalachh = st.text_input ('Input nilai Maximum Heart Rate (thalachh): ')
with col2:
    exng = st.text_input ('Input nilai Exercise-Induced Angina (exng)   : ')
with col2:
    oldpeak = st.text_input ('Input nilai ST Depression (oldpeak)       : ')
with col2:
    slp = st.text_input ('Input nilai Slope of ST Segment (slp)         : ')
with col2:
    caa = st.text_input ('Input nilai Number of Major Vessels (caa)     : ')
with col2:
    thall = st.text_input ('Input nilai Thalassemia (thall)             : ')


diagnosa = ''

if st.button('Test Prediksi Diabetes'):
    prediksi_diagnosa = loaded_numpy_model.predict([[age, sex, cp, trtbps, chol, fbs, restecg, exng, thalachh, oldpeak, slp, caa, thall]])

    if(prediksi_diagnosa[0] == 1):
        diagnosa = 'Pasien didiagnosa mengarah ke penyakit jantung'
    else:
        diagnosa = 'Pasien tidak terindikasi mengarah ke penyakit jantung'
    
    st.success(diagnosa)
