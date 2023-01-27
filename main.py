# -*- coding: utf-8 -*-

import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('C:/Users/rishabh/PycharmProjects/Digital Health App/parkinsons_model.sav', 'rb'))


input_data = (252.45500,261.48700,182.78600,0.00185,0.000007,0.00092,0.00113,0.00276,0.01152,0.10300,0.00614,0.00730,0.00860,0.01841,0.00432,26.80500,0.610367,0.635204,-7.319510,0.200873,2.028612,0.086398

)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is not suffering from parkinsons disease')
else:
  print('The person is suffering from parkinsons disease')



