from cProfile import label
from tkinter import LabelFrame
from flask import Flask
import tensorflow as tf
import numpy as np
from keras.preprocessing import image
import os


model = tf.keras.models.load_model('model10june.h5')

def preprocess_image(image_path, target_size):
    img = image.preprocess_image(image_path, target_size(224, 224))
    img_array = image.img_to_array(img)/225
    img_batch = np.expand_dims(img_array,axis=0)
    prediction = model.predict(img_batch)

def labels_image(labels_path):
    labels =  np.array(open(labels_path).read().splitlines())
    prediction = labels[np.argmax(prediction)]
    confident = prediction[0][np.argmax(prediction)]

    print("terdeteksi penyakit {} dengan tingkat kepercayaan {}".format(labels_image,confident))