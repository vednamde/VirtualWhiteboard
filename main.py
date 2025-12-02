import cv2
import numpy as np
import time
import os
from utils.hand_tracking import HandDetector

#######################
brushThickness = 15
eraserThickness = 50
########################

folderPath = "header"
# We can add header images later if needed, for now we will use color rectangles
drawColor = (255, 0, 255) # Default color

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.85)
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:
    # 1. Import image
    success, img = cap.read()
    if not success:
        break
    img = cv2.resize(img, (1280, 720))
    img = cv2.flip(img, 1)

    # 2. Find Hand Landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        # tip of index and middle fingers
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # 3. Check which fingers are up
        fingers = detector.fingersUp()
        # print(fingers)

        # 4. If Selection Mode - Two finger are up
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            # print("Selection Mode")
            # Checking for the click
            if y1 < 125:
                # Brush Sizes
                if 20 < x1 < 80:
                    brushThickness = 15
                elif 100 < x1 < 150:
                    brushThickness = 30
                elif 170 < x1 < 230:
                    brushThickness = 50
                
                # Colors
                elif 250 < x1 < 450:
                    drawColor = (255, 0, 255)
                elif 550 < x1 < 750:
                    drawColor = (255, 0, 0)
                elif 800 < x1 < 950:
                    drawColor = (0, 255, 0)
                elif 1050 < x1 < 1200:
                    drawColor = (0, 0, 0)
            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)

        # 5. If Drawing Mode - Index finger is up
        if fingers[1] and not fingers[2]:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            # print("Drawing Mode")
            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

            xp, yp = x1, y1
        
        # Clear Canvas when all fingers are up
        if all(x == 1 for x in fingers):
             imgCanvas = np.zeros((720, 1280, 3), np.uint8)

    # Drawing the UI Header
    cv2.rectangle(img, (0, 0), (1280, 125), (0, 0, 0), cv2.FILLED) # Header Background
    
    # Brush Sizes
    cv2.circle(img, (50, 60), 10, (255, 255, 255), cv2.FILLED) # Small
    cv2.circle(img, (120, 60), 20, (255, 255, 255), cv2.FILLED) # Medium
    cv2.circle(img, (200, 60), 30, (255, 255, 255), cv2.FILLED) # Large

    # Colors
    cv2.rectangle(img, (250, 10), (450, 115), (255, 0, 255), cv2.FILLED) # Pink
    cv2.rectangle(img, (550, 10), (750, 115), (255, 0, 0), cv2.FILLED) # Blue
    cv2.rectangle(img, (800, 10), (950, 115), (0, 255, 0), cv2.FILLED) # Green
    cv2.rectangle(img, (1050, 10), (1200, 115), (255, 255, 255), cv2.FILLED) # Eraser (White block for now)
    cv2.putText(img, "Eraser", (1080, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)


    # 6. Image Merging
    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)


    cv2.imshow("Image", img)
    # cv2.imshow("Canvas", imgCanvas)
    # cv2.imshow("Inv", imgInv)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('s'):
        cv2.imwrite("whiteboard_art.jpg", imgCanvas)
        print("Image Saved!")

cap.release()
cv2.destroyAllWindows()
