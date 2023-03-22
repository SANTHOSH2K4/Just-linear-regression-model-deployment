import pickle
import numpy as np


# Load the model from a file
with open('D:\Codes\ML Models by orange\model.pkcls', 'rb') as f:
    model = pickle.load(f)

# Use the model to make predictions
X_test = np.array([[1]])

# Use the model to make predictions
predictions = model.predict(X_test)
predictions=int(predictions[0])
print("predicted value is : ",predictions)