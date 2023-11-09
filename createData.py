import cv2 as cv
import os
import time

myPath = "data/images"

cameraNo = 0
cameraBrightness = 190
moduleValu = 10  # Save Every ITH frame to avoid repetition
minBlur = 1000  # threshold for bluriness, because Smaller Value means more bluriness
gray_Image = False  # images saved colored or gray
saveData = True  # Save Data flag
showImage = True  # Image Display flag
imgWidth = 180
imgHeight = 120

global countFolder

cap = cv.VideoCapture(cameraNo)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, cameraBrightness)

count = 0
countSave = 0


def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists(os.path.join(myPath, str(countFolder))):
        countFolder = countFolder + 1
    os.makedirs(myPath + str(countFolder))

if saveData:saveDataFunc()

while True:
    success, img = cap.read()
    img = cv.resize(img, (imgWidth, imgHeight))
    if gray_Image:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    if saveData:
        blur = cv.Laplacian(img, cv.CV_64F).var()
        if count % moduleValu == 0 and blur > minBlur:
            nowTime = time.time()
            cv.imwrite(os.path.join(myPath, str(countFolder), f"{countSave} {int(blur)} {nowTime}.png"), img)
            countSave += 1
        count += 1

    if showImage:
        cv.imshow("image", img)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv.destroyAllWindows()
