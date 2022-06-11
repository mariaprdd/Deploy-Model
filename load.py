import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io
import urllib3.request
import traceback

model = keras.models.load_model("model10june.h5")


with open('herpes zoster.jpg', 'rb') as file:
    image_bytes = file.read()
    pillow_img = Image.open(io.BytesIO(image_bytes)).convert('L')


imgs = []

path = 'benign.jpg'
  
img = load_img(path, target_size=(224, 224))
img = img.img_to_array(img)/255
imgs = np.expand_dims(img, axis=0)


predictions = model(imgs)
pred = np.argmax(predictions, axis=1)

print(pred)

