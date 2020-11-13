''' Ruler 1         2         3         4         5         6         7        '
/*******************************************************************************
*                                                                              *
*					   /$$$$$$$$                                               *
*					  | $$_____/                                               *
*					  | $$     /$$$$$$    /$$$$$$$   /$$$$$$                   *
*					  | $$$$$ |____  $$  /$$_____/  /$$__  $$                  *
*					  | $$__/  /$$$$$$$ | $$       | $$$$$$$$                  *
*					  | $$    /$$__  $$ | $$       | $$_____/                  *
*					  | $$   |  $$$$$$$ |  $$$$$$$ |  $$$$$$$                  *
*					  |__/    \_______/  \_______/  \_______/                  *
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

import numpy as np
import cv2


#------------------------------------------------------------------------------#
#                                  FACE DETECTOR                               #
#------------------------------------------------------------------------------#

prototxtPath = r".\Face_Detect\deploy.prototxt"
weightsPath = r".\Face_Detect\res10_300x300_ssd_iter_140000.caffemodel"

def face_detect(frame):

	faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(frame, 1.0, (224, 224), (104.0, 177.0, 123.0))

	faceNet.setInput(blob)
	detections = faceNet.forward()

	locs = []

	for i in range(0, detections.shape[2]):
		confidence = detections[0, 0, i, 2]

		if confidence > 0.5:
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			(startX, startY) = (max(0, startX), max(0, startY))
			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

			locs.append((startX, startY, endX, endY))

	return locs