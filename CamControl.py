import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#####################################
wCam, hCam = 640, 480
frameR = 100
smoothening = 7
#####################################

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(detectionCon=0.7, maxHands=2)

devices = AudioUtilities.GetSpeakers()
volume = devices.EndpointVolume
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
volBar = 400
volPer = 0

pLocX, pLocY = 0, 0
cLocX, cLocY = 0, 0
wScr, hScr = pyautogui.size()

pTime = 0

while True:
    success, img = cap.read()
    if not success:
        break
        
    img = cv2.flip(img, 1)
    
    img = detector.findHands(img)
    
    if detector.results.multi_hand_landmarks:
        for i, hand_landmarks in enumerate(detector.results.multi_hand_landmarks):
            
            lmList, bbox, handType = detector.findPosition(img, handNo=i, draw=True)
            
            if len(lmList) != 0:
                if handType == "Right":  
                    
                    x1, y1 = lmList[8][1:]
                    x2, y2 = lmList[12][1:]
                    
                    fingers = detector.fingersUp(handType)
                    
                    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                                (255, 0, 255), 2)
                    
                    if fingers[1] == 1 and fingers[2] == 0:
                        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                        y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
                        
                        cLocX = pLocX + (x3 - pLocX) / smoothening
                        cLocY = pLocY + (y3 - pLocY) / smoothening
                        
                        try:
                            pyautogui.moveTo(cLocX, cLocY)
                        except:
                            pass
                        
                        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                        pLocX, pLocY = cLocX, cLocY
                        
                    if fingers[1] == 1 and fingers[2] == 1:
                        length, img, lineInfo = detector.findDistance(8, 12, img)
                        if length < 40:
                            cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                            pyautogui.click()
                
                elif handType == "Left": 
                    
                    length, img, lineInfo = detector.findDistance(4, 8, img)
                    
                    volBar = np.interp(length, [30, 120], [400, 150])
                    volPer = np.interp(length, [30, 120], [0, 100])
                    
                    volume.SetMasterVolumeLevelScalar(volPer / 100, None)
                    
                    if length < 50:
                        cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    
                    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
                    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
                    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cTime = time.time()
    try:
        fps = 1 / (cTime - pTime)
    except ZeroDivisionError:
        fps = 0
    pTime = cTime
    
    cv2.putText(img, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    
    cv2.imshow("Combined Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break