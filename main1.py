import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/rishabh/PycharmProjects/Digital Health App/parkinsons_model.sav', 'rb'))


# creating a function for Prediction

def parkinsons_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not suffering from parkinsons disease'
    else:
        return 'The person is suffering from parkinsons disease'


def main():
    # giving a title
    st.title('Parkinson Prediction Web App')

    # getting the input data from the user
    fo = st.text_input('fo')
    fhi = st.text_input('fhi')
    flo = st.text_input('flo')
    jitter = st.text_input('jitter')
    jitter_abs = st.text_input('jitter_abs')
    rap = st.text_input('rap')
    ppq = st.text_input('ppq')
    ddp = st.text_input('ddp')
    shimmer = st.text_input('shimmer')
    shimmer_db = st.text_input('shimmer_db')
    shimmer_apq3 = st.text_input('shimmer_apq3')
    shimmer_apq5 = st.text_input('shimmer_apq5')
    shimmer_apq = st.text_input('shimmer_apq')
    dda = st.text_input('dda')
    nhr = st.text_input('NHR')
    hnr = st.text_input('HNR')
    rpde = st.text_input('RPDE')
    dfa = st.text_input('Single fractal scaling component')
    spread1 = st.text_input('Spread1')
    spread2 = st.text_input('Spread2')
    d2 = st.text_input('D2')
    ppe = st.text_input('PPE')
    status = st.text_input('status')
    # code for Prediction
    diagnosis = ''

    # creating a button for Prediction

    if st.button('Parkinson Test Result'):
        diagnosis = parkinsons_prediction(
            [fo, fhi, flo, jitter, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, shimmer_apq3,
             shimmer_apq5, shimmer_apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe])
    if(status==0):
        diagnosis='The person is not suffering from parkinsons disease'
    else:
        diagnosis = 'The person is suffering from parkinsons disease'
    st.success(diagnosis)


if __name__ == '__main__':
    main()
