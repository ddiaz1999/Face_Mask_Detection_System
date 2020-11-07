from Face_Detector import *
from Mask_Detector import *

def draw_face(frame, bndbox, predict):
	bndbox = np.array(bndbox)

	if bndbox.shape == (1, 4):
		#bndbox = bndbox[0]

		predict = predict[0][0]
		print(predict, type(predict))
		index = np.where(predict == np.max(predict))[0][0]
		print(index,predict[index])
		class_predict = classes[index]
		#print('class predict',class_predict, 'max', max(predict[0][0]))
		color = classes_color[class_predict]

		startX, startY, endX, endY = bndbox[0][0], bndbox[0][1], bndbox[0][2], bndbox[0][3]
		start_point, end_point = (startX, startY), (endX, endY)

		FONT, FONT_SCALE, thickness = cv2.FONT_HERSHEY_DUPLEX, 1.3, 2

		(label_width, label_height) = cv2.getTextSize(class_predict, FONT, FONT_SCALE, thickness)[0]
		org = ( (endX - startX)//2 + startX - label_width//2, startY - 10 )

		frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
		frame = cv2.putText(frame, class_predict, org, FONT, FONT_SCALE, color, thickness)

	return frame

if __name__ == "__main__":

	classes = ['mask_weared_incorrect','with_mask', 'without_mask']
	classes_color = {'mask_weared_incorrect': (0,127,255),
		'with_mask': (0, 255, 0),
			  'without_mask': (0, 0, 255)
			 }


	# mal_puesta = cv2.imread('mal_puesto.jpg')
	# bndbox = face_detect(mal_puesta)
	# print(bndbox)
	# predict = mask_detect(mal_puesta, bndbox)
	# print(predict)
	# frame = draw_face(mal_puesta, bndbox, predict)
	# cv2.imshow('frmae',frame)
	# cv2.waitKey(0)


	vid = cv2.VideoCapture(0)

	while (True):

		ret, frame = vid.read()
		bndbox = face_detect(frame)
		predict = mask_detect(frame, bndbox)
		print(predict)
		frame = draw_face(frame, bndbox, predict)
		cv2.imshow('frame', frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	vid.release()
	cv2.destroyAllWindows()
	



