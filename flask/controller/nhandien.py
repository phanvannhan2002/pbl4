from flask import request, redirect, url_for
from PIL import Image
from io import BytesIO
from flask_smorest import Blueprint
import os
import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

blp = Blueprint("NhanDien", "nhandien", description="Operations on items")

@blp.post("/getImage")
def getImage():
    blob_data = request.get_data()
    image = Image.open(BytesIO(blob_data))
    filename = 'test.jpg'
    file_path = os.path.join("models", filename)
    image.save(file_path, format='JPEG')
    img_height = 180
    img_width = 180
    class_names = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']

    sunflower_path = 'models/test.jpg'

    img = tf.keras.utils.load_img(
        sunflower_path, target_size=(img_height, img_width)
    )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    TF_MODEL_FILE_PATH = 'models/model.tflite'  # The default path to the saved TensorFlow Lite model

    interpreter = tf.lite.Interpreter(model_path=TF_MODEL_FILE_PATH)

    classify_lite = interpreter.get_signature_runner('serving_default')

    predictions_lite = classify_lite(sequential_1_input=img_array)['outputs']
    score_lite = tf.nn.softmax(predictions_lite)

    flower = class_names[np.argmax(score_lite)]
    os.remove(file_path)
    if flower == 'dandelion':
        return "Bồ công anh"
    elif flower == "roses":
        return "hoa hồng"
    elif flower == "sunflowers":
        return "Hướng dương"
    elif flower == "tulips":
        return "tulip"
    else:
        return "hoa cúc"


