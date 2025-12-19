import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui

#####################################
wCam, hCam = 640, 480
frameR = 100 # frame raduction
smoothening = 5
#####################################

pTime = 0
# previousLocation
pLocX, pLocY = 0,0
# currentLocation
cLocX, cLocY = 0,0

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 648)
cap.set(4, 480)
wScr, hScr = pyautogui.size()
detector = htm.handDetector(maxHands=1)
# print(wScr, hScr)

while True:
    # 1. Find hand Landmarks
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # 2. Get the tip of the index and middle fingers
    if len(lmList)!=0:
        # [id, x, y]
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # print(x1, y1, x2, y2)
    
        # 3. Check which finger are up
        fingers = detector.fingersUp()
        # print(fingers)
        cv2.rectangle(img,(frameR,frameR),(wCam-frameR, hCam-frameR),
                          (255,0,255), 2)
        # 4. Only Index Finger : Moving Mode
        if fingers[1]==1 and fingers[2]==0:
            # 5. Convert Coordinates
            x3 = np.interp(x1, (frameR, wCam-frameR),(0,wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR),(0,hScr))

            # 6. Smoothen Values
            cLocX = pLocX +(x3 - pLocX) / smoothening
            cLocY = pLocY +(y3 - pLocY) / smoothening


            # 7. Move Mouse
            pyautogui.moveTo(cLocX,cLocY)
            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
            pLocX, pLocY = cLocX, cLocY

        # 8. Both Index and middle fingers are up: Clicking Mode
        if fingers[1]==1 and fingers[2]==1:

            # 9. Find distance between fingers
            length, img, lineInfo = detector.findDistance(8,12,img)
            # print(length)

            # 10. Click mouse if distance short
            if length < 40:
                cv2.circle(img,(lineInfo[4],lineInfo[5]),
                           15,(0,255,0),cv2.FILLED)
                pyautogui.click()
    # 11. Frame Rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,
                (255,0,0),3)
    # 12. Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)