from tkinter import LabelFrame
from flask import Flask
import tensorflow as tf
import numpy as np
from keras.preprocessing import image
import os

from model import labels_image, preprocess_image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello"

@app.route('/predict', methods=['POST'])
def predict():
    model = tf.keras.models.load_model('model10june.h5')
    img = image.open('./image kulit.jpg')
    img = preprocess_image
    prediction = LabelFrame[np.argmax(prediction)]
    confident = prediction[0][np.argmax(prediction)]

    print("terdeteksi penyakit {} dengan tingkat kepercayaan {}").format(labels_image,confident)
    
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port='80')

