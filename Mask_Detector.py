''' Ruler 1         2         3         4         5         6         7        '
/*******************************************************************************
*                                                                              *
*                  /$$      /$$                        /$$                     *
*                 | $$$    /$$$                       | $$                     *
*                 | $$$$  /$$$$   /$$$$$$    /$$$$$$$ | $$   /$$               *
*                 | $$ $$/$$ $$  |____  $$  /$$_____/ | $$  /$$/               *
*                 | $$  $$$| $$   /$$$$$$$ |  $$$$$$  | $$$$$$/                *
*                 | $$\  $ | $$  /$$__  $$  \____  $$ | $$_  $$                *
*                 | $$ \/  | $$ |  $$$$$$$  /$$$$$$$/ | $$ \  $$               *
*                 |__/     |__/  \_______/ |_______/  |__/  \__/               *
*                                                                              *
*		 /$$$$$$$                /$$                              /$$          *
*		| $$__  $$              | $$                             | $$          *
*		| $$  \ $$   /$$$$$$   /$$$$$$     /$$$$$$    /$$$$$$$  /$$$$$$        *
*		| $$  | $$  /$$__  $$ |_  $$_/    /$$__  $$  /$$_____/ |_  $$_/        *
*		| $$  | $$ | $$$$$$$$   | $$     | $$$$$$$$ | $$         | $$          *
*		| $$  | $$ | $$_____/   | $$ /$$ | $$_____/ | $$         | $$ /$$      *
*		| $$$$$$$/ |  $$$$$$$   |  $$$$/ |  $$$$$$$ |  $$$$$$$   | $$$$/       *
*		|_______/   \_______/    \___/    \_______/  \_______/    \___/        *
*                                                                              *
*                                                                              *
*                  Developed by:                                               *
*                                                                              *
*                            Jhon Hader Fernandez                              *
*                     - jhon_fernandez@javeriana.edu.co                        *
*                                                                              *
*                            Diego Fernando Diaz                               *
*                        - di-diego@javeriana.edu.co                           *
*                                                                              *
*                          Oscar Geovanny Baracaldo                            *
*                       - obaracaldo@javeriana.edu.co                          *
*                                                                              *
*                       Pontificia Universidad Javeriana                       *
*                            Bogota DC - Colombia                              *
*                                  Nov - 2020                                  *
*                                                                              *
*****************************************************************************'''

#------------------------------------------------------------------------------#
#                          IMPORT MODULES AND LIBRARIES                        #
#------------------------------------------------------------------------------#

from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2


#------------------------------------------------------------------------------#
#                                  MASK DETECTOR                               #
#------------------------------------------------------------------------------#

predict = []

maskDetectionModelPath = r".\Mask_Detect\mask_detector.model"
maskNet = load_model(maskDetectionModelPath)

def mask_detect(frame, bndbox):

    if len(bndbox) >= 1:
        bndbox = np.array(bndbox)
        bndbox = bndbox[0]
        startX, startY, endX, endY = bndbox[0][0], bndbox[0][1], bndbox[0][2], bndbox[0][3]

        face = frame[startY:endY, startX:endX]
        face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
        face = cv2.resize(face, (224, 224))
        face = img_to_array(face)
        face = preprocess_input(face)
        face = np.array([face])
        predict = maskNet.predict(face)

    return [predict]