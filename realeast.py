import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
import seaborn as sns
import streamlit as st
import joblib

# Load the model
model = joblib.load('realeast.pkl')

data = pd.read_csv('realest.csv')
df = data.copy()


st.markdown("<h1 style='text-align: center; font-family: helvetica; color: #1F4172;'>House Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='margin: -30px; color: #F11A7B; text-align: center; font-family: cursive'> BUILT BY Matini The Data Guy </h4>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.image('pngwing.com.png', width=350, use_column_width=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<p>A house prediction project involves using data analysis and machine learning to predict the prices or other factors related to houses. It uses historical data about houses, like their location, size, and features, to make these predictions. It can be helpful for real estate professionals and individuals looking to buy or sell a house.</p>", 
             unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.dataframe(data, use_container_width=True)

st.sidebar.image('pngwing1.com.png', caption='Welcome User')

st.markdown("<br>", unsafe_allow_html=True)
st.dataframe(data, use_container_width=True)

input_choice = st.sidebar.radio('Choose your input type', ['Slider Input', 'Number Input'])

if input_choice == 'Slider Input':
    Bedroom = st.sidebar.slider('Average Bedroom', data['Bedroom'].min(), data['Bedroom'].max())
    Space = st.sidebar.slider('Average Space', data['Space'].min(), data['Space'].max())
    Room = st.sidebar.slider('Average Room', data['Room'].min(), data['Room'].max())
    Lot = st.sidebar.slider('Area Lot', data['Lot'].min(), data['Lot'].max()) 
    Tax = st.sidebar.slider('Average Tax', data['Tax'].min(), data['Tax'].max())
    Bathroom = st.sidebar.slider('Average Bathroom', data['Bathroom'].min(), data['Bathroom'].max())
    Garage = st.sidebar.slider('Average Garage', data['Garage'].min(), data['Garage'].max())
else:
    Bedroom = st.sidebar.number_input('Average Bedroom', data['Bedroom'].min(), data['Bedroom'].max())
    Space = st.sidebar.number_input('Average Space', data['Space'].min(), data['Space'].max())
    Room = st.sidebar.number_input('Average Room', data['Room'].min(), data['Room'].max())
    Lot = st.sidebar.number_input('Area Lot', data['Lot'].min(), data['Lot'].max()) 
    Tax = st.sidebar.number_input('Average Tax', data['Tax'].min(), data['Tax'].max())
    Bathroom = st.sidebar.number_input('Average Bathroom', data['Bathroom'].min(), data['Bathroom'].max())
    Garage = st.sidebar.number_input('Average Garage', data['Garage'].min(), data['Garage'].max())

# Create input variables DataFrame
input_vars = pd.DataFrame({ 
    'Bedroom': [Bedroom],
    'Space': [Space],
    'Room': [Room],
    'Lot': [Lot],
    'Tax': [Tax],
    'Bathroom': [Bathroom],
    'Garage': [Garage],
})

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h5 style='margin: -30px; color: olive; font-family: helvetica'>User Input Variable</h5>", unsafe_allow_html=True)
st.dataframe(input_vars)

st.markdown("<br>", unsafe_allow_html=True)

# Predict the house price
predicted = model.predict(input_vars)
st.success(f'The Predicted price of your house is {predicted[0]}')