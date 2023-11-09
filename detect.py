import cv2 as cv
import numpy as np

path = "./data/haarcascade_frontalface_default.xml"
cameraNo = 0
objectName = 'FACE'
frameWidth = 640
frameHeight = 480
color= (255,0,255)

cap = cv.VideoCapture(cameraNo)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

def empty(a):
    pass

# Create tracker
cv.namedWindow("Result")
cv.resizeWindow("Result", frameWidth, frameHeight+100) 
cv.createTrackbar("Scale", "Result", 400, 1000,empty)
cv.createTrackbar("Neig", "Result", 8,20,empty)
cv.createTrackbar("Min Area", "Result", 0,100000,empty)
cv.createTrackbar("Brightness", "Result", 180,255,empty)

# load the classifier Downloaded

cascade = cv.CascadeClassifier(path)

while True:
    cameraBrightness = cv.getTrackbarPos("Brightness", "Result")
    cap.set(10, cameraBrightness)

    success, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    scaleValu = 1 + (cv.getTrackbarPos("Scale","Result") / 1000)
    neig = cv.getTrackbarPos("Neig", "Result")
    objects = cascade.detectMultiScale(gray, scaleValu, neig)

    for(x,y,w,h) in objects:
        area = w*h
        minArea = cv.getTrackbarPos("Min Area", "Result")
        if area > minArea:
            cv.rectangle(img,(x,y), (x+w,y+h),color,3)
            cv.putText(img, objectName, (x,y-5),cv.FONT_HERSHEY_COMPLEX_SMALL,1, color,2)
            roi_color= img[y:y+h, x:x+w]

    cv.imshow("Result",img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break