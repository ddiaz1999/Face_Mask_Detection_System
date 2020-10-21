from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2

def mask_detect(frame, bndbox):
    bndbox = np.array(bndbox)

    if bndbox.shape == (1, 4):
        maskDetectionModelPath = r".\Mask_Detect\mask_detector.model"
        maskNet = load_model(maskDetectionModelPath)

        startX, startY, endX, endY = bndbox[0][0], bndbox[0][1], bndbox[0][2], bndbox[0][3]

        face = frame[startY:endY, startX:endX]
        face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
        face = cv2.resize(face, (224, 224))
        face = img_to_array(face)
        face = preprocess_input(face)

        predict = maskNet.predict(face)

	return predict