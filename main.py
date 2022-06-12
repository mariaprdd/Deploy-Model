import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import io
import tensorflow as tf
from tensorflow import keras
import keras.preprocessing.image as image 
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import urllib3.request
import traceback

from flask import Flask, request, jsonify

 
model = tf.keras.models.load_model('model10june.h5')

def transform_image(img):
    imgs = []
    img = img.resize(224, 224)
    img = image.img_to_array(img)/255
    image = np.expand_dims(img, axis=0)
    
    return image

    
def predict(x):
    predictions = model(x)
    pred = np.argmax(predictions)
    return pred

   
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({"error": "no file"})

        try:
            image_bytes = file.read()
            pillow_img = Image.open(io.BytesIO(image_bytes))
            prediction = predict(transform_image(pillow_img))
            data = {"prediction": int(prediction)}
            return jsonify(data)
        except Exception as e:
            return jsonify({"error": str(e)})

    return "OK"


if __name__ == "__main__":
    app.run(debug=True)