# importing necessory libraries

import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import OrdinalEncoder
import numpy as np
from PIL import Image
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu


# Setting up page configuration
icon = Image.open("Final project\profile.png")
st.set_page_config(page_title= "Retail sales prediction | By Aravinth",
                   page_icon= icon,
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This dashboard app is created by *Aravinth*!"""}
                  )

# Creating option menu in the side bar
with st.sidebar:
    selected = option_menu("Menu", ["Home","Overview","Predict"], 
                           icons=["house","graph-up-arrow","bar-chart-line"],
                           menu_icon= "menu-button-wide",
                           default_index=0,
                           styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#74b5f5"},
                                   "nav-link-selected": {"background-color": "#3467f5"}}
                          )                  

# HOME PAGE
if selected == "Home":
    # Title Image
    st.image("Final project\Home.png")
    col1,col2 = st.columns(2,gap= 'medium')
    col1.markdown("## :blue[Domain] : Retail_Sales_Forecast")
    col1.markdown("## :blue[Technologies used] : Python, Pandas, Plotly, Streamlit, ML, seaborn")
    col1.markdown("## :blue[Overview] : Predict the department-wide sales for each store for the following year,Provide recommended actions based on the insights drawn, with prioritization placed on largest business impact ")
    col2.markdown("#   ")    

# OVERVIEW PAGE
if selected == "Overview":
    st.markdown("In the dynamic landscape of retail, accurate sales predictions are crucial for optimizing inventory, managing resources efficiently, and enhancing overall business performance. Our Retail Sales Prediction Project leverages cutting-edge data analytics and machine learning techniques to forecast sales trends, providing valuable insights for strategic decision-making.")
    st.markdown("    ")
    st.markdown("    ")
    image=Image.open('Final project\EDA.png')   
    st.image(image)                  

# PREDICT PAGE

if selected =="Predict":
    with open(r'E:\my projects\Final project\model.pkl', 'rb') as file:
        _model = pickle.load(file)   

    col1,col2 = st.columns(2)
    with col1:
        year = st.text_input('Enter the Year of sales')
        type_ = st.selectbox('Enter the Sales Type(A:1,B:0,C:-1)',(-1,0,1))
        dept = st.selectbox('Enter the Department code No',( 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 16, 17, 18,
                19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
               36, 37, 38, 40, 41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56,
               58, 59, 60, 67, 71, 72, 74, 79, 80, 81, 82, 83, 85, 87, 90, 91, 92,
               93, 94, 95, 97, 98, 78, 96, 99, 77, 39, 50, 43, 65))
        cpi = st.text_input('CPI')
        fuel = st.text_input("Estimated Fuel Prize")
        size = st.text_input('Area size of the Shop {Generally 30K to 250K}')


    with col2:
        month = st.text_input('Enter the Month of sales')
        day = st.text_input('Enter the Day of the month')
        store = st.selectbox('Enter the Store No',( 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
               18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
               35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45))
        temp = st.text_input('Temperature')
        unemp = st.text_input('UnEmployment Rate {Generally ranges between 1 to 20}')
        holiday = st.selectbox('Is it a Holiday day {True:1,False:0} ',(0,1))
        

    c1,c2,c3 = st.columns([3,1,3])
    with c2:
        submit = st.button("Predict")
        if submit:
            data = np.array([[store, dept, holiday, temp, fuel, cpi, unemp, type_, size, year, month, day]])
            y_pred = _model.predict(data)
            # Assuming y_pred is a numeric value
            st.success("The Weekly sales are {}".format(y_pred))    