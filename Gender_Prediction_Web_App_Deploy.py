import numpy as np
import pickle
import streamlit as st

def loaded_data():
    return pickle.load(open(r'C:\Users\Muhammed Thouyib TK\Model_Deployment\Model_Deploy.sav','rb'))

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
     long_hair = st.number_input('Is your hair long [yes==1 , no==0]')
     forehead_width_cm = st.number_input('Enter your forhead width [cm]')
     forehead_height_cm = st.number_input('Enter your forhead height [cm]')
     nose_wide = st.number_input('Is your nose is wide [yes==1 , no==0]')
     nose_long =  st.number_input('Is your nose long [yes==1 , no==0]')
     lips_thin =  st.number_input('Is your lips thin [yes==1 , no==0]')
     distance_nose_to_lip_long = st.number_input('Is distance b/w nose and lip are too long [yes==1 , no==0]')


     # code for button
     if st.button('Predict Gender'):
          data = np.array([[long_hair,forehead_width_cm,forehead_height_cm,nose_wide,nose_long,lips_thin,distance_nose_to_lip_long]],dtype=float)
          result = predictions(data)
          st.success(result)

if __name__ == '__main__':
     main()