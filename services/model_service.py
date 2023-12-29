import pickle
import numpy as np


class ModelService:
    def __init__(self, model_path):
        with open(model_path, 'rb') as model_file:
            self.model = pickle.load(model_file)

    def predict_lgo(self, features):
        input_data = np.array([list(features.values())])
        prediction = self.model.predict(input_data)
        return prediction[0]
