import os
import sys
import warnings
import matplotlib.pyplot as plt
import cv2

import glob
import shutil 

from PIL import Image
from IPython.display import display
import streamlit as st
from tempfile import NamedTemporaryFile


import tensorflow as tf
from keras.preprocessing import image as image_utils
from keras.applications.imagenet_utils import decode_predictions
from keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.applications import VGG16
import numpy as np
import cv2

import time

st.write("""
         # Image Classification application 
         """
         )

file = st.file_uploader("Please upload image to be classified", type=["png","jpg"])
temp_file = NamedTemporaryFile(delete=False)         


if file is None:
  st.markdown("<div><span class='highlight green'><font color='white'>Please upload an image file in PNG or JPG format</font></span><div>", unsafe_allow_html=True)  
else:
  temp_file.write(file.getvalue())
  
  if not os.path.isdir("test"):
    os.mkdir("test")
    
  im = Image.open(temp_file)
  im.save("test/1.png")
  
  orig = plt.imread("test/1.png")
  image = tf.image.resize(orig, (224, 224))
  image = np.array(image)
  image = np.expand_dims(image, axis=0)
  image = preprocess_input(image)
  
  model = VGG16(weights="imagenet")

  preds = model.predict(image)

  P = decode_predictions(preds)

  A=plt.figure(figsize=(30,20))
    
  plt.axis("off")
  plt.imshow(Image.fromarray(orig))
  plt.grid(False)

  st.pyplot(A)
  
  for (i, (imagenetID, label, prob)) in enumerate(P[0]):
    st.write("""## """,i + 1,""" """,label,""" """,prob * 100)
    
  shutil.rmtree("test")  