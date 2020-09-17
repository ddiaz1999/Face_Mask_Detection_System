import cv2

# Link del video: https://www.youtube.com/watch?v=J1jlm-I1cTs

if __name__ == "__main__":

    # Insertar alguna imagen en la misma carpeta del proyecto, para hacer pruebas
    path = r'.\GGG2.jpeg'

    img = cv2.imread(path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    faces = face_classifier.detectMultiScale(img_gray,
                                             scaleFactor=1.1,
                                             minNeighbors=4,
                                             minSize=(30, 30),
                                             maxSize=(300,300))

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Test', img)
    cv2.waitKey(0)