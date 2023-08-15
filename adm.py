import streamlit as st
import pickle
import numpy as np
import pandas as pd
# import the model
model = pickle.load(open('model.pkl','rb'))
ds = pickle.load(open('dataset.pkl','rb'))

st.title("Admission Predictor")

test_conversion_dict = {
    'GRE': 340,
    'GMAT': 800,
    'SAT': 1600,
    'ACT': 36,
    # Add more conversions here
}
test_taken = st.selectbox('Choose the Test', list(test_conversion_dict.keys()))
if test_taken in test_conversion_dict:
    test_score = st.number_input(f'Enter your {test_taken} score:')
    converted_test_score = test_conversion_dict[test_taken]
    gre = (test_score / converted_test_score) * 340

conversion_dict = {
    'DUOLINGO ENGLISH TEST': 160,
    'IELTS': 9,
    'PTE': 90,
    'TOEFL': 120,
    'Cambridge English Scale': 110,
    # Add more conversions here
}

english_test = st.selectbox('Choose the English Test', list(conversion_dict.keys()))

if english_test in conversion_dict:
    english_score = st.number_input(f'Enter your {english_test} score:')
    converted_toefl = conversion_dict[english_test]
    # Convert the English test score to equivalent TOEFL score
    toefl = (english_score / converted_toefl) * 120  # Scaling to TOEFL range



rating = st.selectbox('University Rating',[1,2,3,4,5])


sop = st.number_input('SOP')


lor = st.number_input('LOR')


gpa = st.number_input('CGPA')


research = st.selectbox('Reseach Experience',[0,1])

if st.button('Predict Price'):



    query = np.array([gre,toefl,rating,sop,lor,gpa,research])

    query = query.reshape(1,7)
    predicted_chance = model.predict(query)[0]
    adjusted_chance = max(predicted_chance - 0.20, 0.10)

    st.title("The predicted chance of admission is {:.2f}%".format(adjusted_chance * 100))