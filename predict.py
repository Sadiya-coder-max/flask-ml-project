import joblib
import numpy as np

model = joblib.load("models/random_forest.pkl")

def predict(input_data):
    data = np.array(input_data).reshape(1, -1)
    return model.predict(data)

print(predict([5.1, 3.5, 1.4, 0.2])) 
