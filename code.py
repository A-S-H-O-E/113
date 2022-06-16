import cv2 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
image = cv2.imread('C:/Users/Aashu/Downloads/Python/Class-113 (Face Recog)/test.jpg')
cv2.waitKey(1000)
faces = face_cascade.detectMultiScale(image,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),5)
cv2.imshow('face detected', image)
cv2.waitKey()