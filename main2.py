import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/rishabh/PycharmProjects/Digital Health App/heartDisease_model.sav', 'rb'))


# creating a function for Prediction

def heartDisease_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not suffering from heart disease'
    else:
        return 'The person is suffering from heart disease'


def main():
    # giving a title
    st.title('Heart Prediction Web App')

    # getting the input data from the user
    age = st.text_input('age')
    sex = st.text_input('sex')
    cp = st.text_input('cp')
    trestbps = st.text_input('trestbps')
    cholestrol = st.text_input('cholestrol')
    fbs = st.text_input('fbs')
    restecg = st.text_input('restecg')
    thalach = st.text_input('thalach')
    exang = st.text_input('exang')
    oldpeak = st.text_input('oldpeak')
    slope = st.text_input('slope')
    ca = st.text_input('ca')
    thal = st.text_input('thal')
    target = st.text_input('target')
    # code for Prediction
    diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Test Result'):
        diagnosis = heartDisease_prediction(
            [age, sex, cp, trestbps, cholestrol, fbs, restecg, thalach, exang, oldpeak, slope,ca, thal])
    if(target==0):
        diagnosis='The person is not suffering from heart disease'
    else:
        diagnosis = 'The person is suffering from heart disease'
    st.success(diagnosis)


if __name__ == '__main__':
    main()
