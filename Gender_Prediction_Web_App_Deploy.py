import numpy as np
import pickle
import streamlit as st
import os

def loaded_data():
    file_path = "Model_Deploy.sav"
    return pickle.load(open(file_path, 'rb'))

model = loaded_data()

def predictions(data):
    pred=model.predict(data)
    if pred[0] == 0:
        return 'Your Gender is Female'
    else:
        return 'Your Gender is Male'

def main():
     # title of the web app
     st.title('Gender Prediction Web App')

     # to get input from the user
     long_hair = st.number_input('Is your hair long [yes=1 , no=0]',min_value=0, max_value=1, step=1)
     forehead_width_cm = st.number_input('Enter your forhead width [cm]',format="%.2f")
     forehead_height_cm = st.number_input('Enter your forhead height [cm]',format="%.2f")
     nose_wide = st.number_input('Is your nose is wide [yes=1 , no=0]',min_value=0, max_value=1, step=1)
     nose_long =  st.number_input('Is your nose long [yes=1 , no=0]',min_value=0, max_value=1, step=1)
     lips_thin =  st.number_input('Is your lips thin [yes=1 , no=0]',min_value=0, max_value=1, step=1)
     distance_nose_to_lip_long = st.number_input('Is distance b/w nose and lip are too long [yes=1 , no=0]',min_value=0, max_value=1, step=1)


     # code for button
     if st.button('Predict Gender'):
          data = np.array([[long_hair,forehead_width_cm,forehead_height_cm,nose_wide,nose_long,lips_thin,distance_nose_to_lip_long]])
          result = predictions(data)
          st.success(result)

if __name__ == '__main__':
     main()