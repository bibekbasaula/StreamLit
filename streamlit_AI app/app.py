import streamlit as st
import numpy as np
from model import predict_diabetes

st.title('Diabetes Prediction App')
st.write('Check your diabetes here')

glucose = st.number_input('Enter Glucose',0,500)
dfp = st.number_input('DFP',0,15)
age = st.number_input('Age',10,100)

if st.button('Predict'):
    to_predict = np.array([[glucose, dfp, age]])
    result = predict_diabetes(to_predict)

    print(result)

    if result[0] == 0:
        st.success('No Diabetes')
        st.balloons()
    else:
        st.warning('Diabetes predicted')


