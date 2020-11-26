''' Ruler 1         2         3         4         5         6         7        '
/*******************************************************************************
*                                                                              *
*       /$$$$$$    /$$                                                         *
*      /$$__  $$  | $$                                                         *
*     | $$  \__/ /$$$$$$     /$$$$$$    /$$$$$$    /$$$$$$   /$$$$$$/$$$$      *
*     |  $$$$$$ |_  $$_/    /$$__  $$  /$$__  $$  |____  $$ | $$_  $$_  $$     *
*      \____  $$  | $$     | $$  \__/ | $$$$$$$$   /$$$$$$$ | $$ \ $$ \ $$     *
*      /$$  \ $$  | $$ /$$ | $$       | $$_____/  /$$__  $$ | $$ | $$ | $$     *
*     |  $$$$$$/  |  $$$$/ | $$       |  $$$$$$$ |  $$$$$$$ | $$ | $$ | $$     *
*      \______/    \___/   |__/        \_______/  \_______/ |__/ |__/ |__/     *
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
*        /$$$$$$$                /$$                              /$$          *
*       | $$__  $$              | $$                             | $$          *
*       | $$  \ $$   /$$$$$$   /$$$$$$     /$$$$$$    /$$$$$$$  /$$$$$$        *
*       | $$  | $$  /$$__  $$ |_  $$_/    /$$__  $$  /$$_____/ |_  $$_/        *
*       | $$  | $$ | $$$$$$$$   | $$     | $$$$$$$$ | $$         | $$          *
*       | $$  | $$ | $$_____/   | $$ /$$ | $$_____/ | $$         | $$ /$$      *
*       | $$$$$$$/ |  $$$$$$$   |  $$$$/ |  $$$$$$$ |  $$$$$$$   | $$$$/       *
*       |_______/   \_______/    \___/    \_______/  \_______/    \___/        *
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

from Face_Detector import *
from Mask_Detector import *


#------------------------------------------------------------------------------#
#                                    DRAW FACE                                 #
#------------------------------------------------------------------------------#

def draw_face(frame, bndbox, predict, verbose=False):

	if len(bndbox) >= 1:
		bndbox = np.array(bndbox)
		bndbox = bndbox[0]

		predict = predict[0]
		index = np.where(predict == np.max(predict))[0][0]

		if verbose == True:
			print('Class: ', classes[index], 'Probability: ', predict[index])

		class_predict = classes[index]
		color = classes_color[class_predict]

		startX, startY = bndbox[0], bndbox[1]
		endX, endY = bndbox[2], bndbox[3]
		start_point, end_point = (startX, startY), (endX, endY)

		FONT, FONT_SCALE, thickness = cv2.FONT_HERSHEY_DUPLEX, 1.3, 2

		(label_width, label_height) = cv2.getTextSize(class_predict, FONT,
					                      FONT_SCALE, thickness)[0]
		org = ( (endX - startX)//2 + startX - label_width//2, startY - 10 )

		frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
		frame = cv2.putText(frame, class_predict, org, FONT, FONT_SCALE, color,
							thickness)

	return frame



#------------------------------------------------------------------------------#
#                                       MAIN                                   #
#------------------------------------------------------------------------------#

if __name__ == "__main__":

	classes = ['mask_weared_incorrect','with_mask', 'without_mask']
	classes_color = {'mask_weared_incorrect': (0, 127, 255),
		             'with_mask': (0, 255, 0),
			         'without_mask': (0, 0, 255)}

	vid = cv2.VideoCapture(0)
	predict = []
	while (True):

		ret, frame = vid.read()
		bndbox = face_detect(frame)
		predict = mask_detect(frame, bndbox)
		frame = draw_face(frame, bndbox, predict, verbose=True)
		cv2.imshow('frame', frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	vid.release()
	cv2.destroyAllWindows()
