from logging import exception
from keras.models import load_model
import os






model_path = 'backend\models\Cnn_Surface_detection v1.1.h5'

def model_loading():
    """
    ***we setup the model bu using h5 file and keras***
    returns the model id
    """
    calling_cnn = load_model(model_path)
    print("Model Loaded")
    return calling_cnn


print(model_loading)    




