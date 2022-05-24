# ====================== Packages ======================

# Libraries to perform file transfer operations, 
# calculating time of execution, find path of file.

import os
import sys
import glob
import time
import shutil 
import warnings

# Libraries that are used to read an image, preprocess 
# input data, plot figures and convert I/O byte into 
# equivalent file format.

import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from IPython.display import display
from tempfile import NamedTemporaryFile

# Library to connect backend operations with 
# frontend webpage of application.
import streamlit as st

# Libraries used to create deep learning models and 
# preprocessing dataset.

import tensorflow as tf
from tensorflow.keras.applications import VGG16
from keras.preprocessing import image as image_utils
from keras.applications.imagenet_utils import preprocess_input
from keras.applications.imagenet_utils import decode_predictions

# ====================== Function ======================

def preprocess_input_image(temp_file):
 
  """
    Apply preprocessing operations on image data.
    
    :Parameters:
    
        temp_file: I/O byte data of image.
            Shape : (256,1)
    :Returns:
        
        return: np.array()
            
    :Usage Example:
        >>>   image = preprocess_input(temp_file)
  """
 
  im = Image.open(temp_file)
  im = np.array(im)
  image = tf.image.resize(im, (224, 224))
  image = np.array(image)
  image = np.expand_dims(image, axis=0)
  image = preprocess_input(image)
  return image

# Give title to the webpage.

st.write("""
         # Image Classification application 
         """
         )

# Read input image in PNG or JPG format and 
# store into I/O byte format for further operations.

file = st.file_uploader("Please upload image to be classified", type=["png","jpg"])
temp_file = NamedTemporaryFile(delete=False)         

# Check whether the user provides the file.

if file is None:
  st.markdown("<div><span class='highlight green'><font color='white'>Please upload an image file in PNG or JPG format</font></span><div>", unsafe_allow_html=True)  
else:
  temp_file.write(file.getvalue())

  # Preprocess image before prediction. 

  image = preprocess_input_image(temp_file)

  # Initialize a VGG16 model with the weights of Imagenet.

  model = VGG16(weights="imagenet")

  # Perform prediction.

  preds = model.predict(image)

  # Extract details of classified image.

  P = decode_predictions(preds)

  # Display top categories classified for input image.

  for (i, (imagenetID, label, prob)) in enumerate(P[0]):
    st.write("""## """,i + 1,""" """,label,""" """,prob * 100)
