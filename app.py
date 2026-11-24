import streamlit as st
import pandas as pd
import joblib
model=joblib.load('house price.pkl')
scaler=joblib.load('scaler.pkl')
st.title('House price prediction App')
st.write('Enter the details to continue')
income=st.number_input('Avg Area income',min_value=0.0,value=1000000.0)
house_age=st.number_input('Avg area house age',min_value=0.0,value=50.00)
no_rooms=st.number_input('Avg area no of rooms',min_value=0.0,value=20.0)
no_bedrooms=st.number_input('Avg area no of bedrooms',min_value=0.0,value=10.0)
area_population=st.number_input('Avg area of population',min_value=0.0,value=1000000.0)
if st.button('Predict House Price'):

    input_data=pd.DataFrame({'Avg. Area Income':[income],
    'Avg. Area House Age':[house_age],
    'Avg. Area Number of Rooms':[no_rooms],
    'Avg. Area Number of Bedrooms':[no_bedrooms],
    'Area Population':[area_population]})
    scaled_data=scaler.transform(input_data)
    prediction=model.predict(scaled_data)
    predicted_value=prediction.item()
    st.success(f'Prediction {predicted_value:,.2f}')


