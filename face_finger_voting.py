import cv2
import RPi.GPIO as GPIO
import numpy as np
import os
import pandas as pd
import time
import datetime
from datetime import datetime
import csv
import sys
GPIO.setmode(GPIO.BCM)
buttonx = 17
buttony = 27
buttonz = 22
buttonm = 10
buttona = 9
buttone = 11
GPIO.setup(buttonx, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttony, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonz, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonm, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttona, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttone, GPIO.IN, pull_up_down=GPIO.PUD_UP)
user_name = input('enter your name:')

                
def m():
    time.sleep(2)
    while True:
        markattendance(user_name)
    

def fingerprint():
    test_original = cv2.imread("chiru.jpg")
    cv2.imshow("Original", cv2.resize(test_original, None, fx=1, fy=1))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    for file in [file for file in os.listdir("database")]:
        fingerprint_database_image = cv2.imread("./database/"+file)
        sift = cv2.xfeatures2d.SIFT_create()
        keypoints_1, descriptors_1 = sift.detectAndCompute(test_original, None)
        keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_database_image, None)

    matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10), 
                 dict()).knnMatch(descriptors_1, descriptors_2, k=2)

    match_points = []
    for p, q in matches:
        if p.distance < 0.1*q.distance:
            match_points.append(p)
    keypoints = 0
    if len(keypoints_1) <= len(keypoints_2):
        keypoints = len(keypoints_1)            
    else:
        keypoints = len(keypoints_2)
    if (len(match_points) / keypoints)>0.95:
        print("% match: ", len(match_points) / keypoints * 100)
        print("Figerprint ID: " + str(file))
        finger_id = (file)
        print(finger_id)
        result = cv2.drawMatches(test_original, keypoints_1, fingerprint_database_image, 
                                  keypoints_2, match_points, None) 
        result = cv2.resize(result, None, fx=0.5, fy=0.5)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(result)
        return finger_id

    
        
    

def markattendance(name):
    button_state = GPIO.input(buttonx)
    if(button_state == False):
        print("you voted for X party")
        vote = ("X")
        print(vote)
        with open('attendance.csv','r+') as f:
            print("file is opened")
            myDatalist = f.readlines()
            namelist = []
            for line in myDatalist:
                print("list is prepared")
                entry = line.split(',')
                namelist.append(entry[0])
            if name not in namelist:
                print("name not in list")
                now = datetime.now()
                dtstring = now.strftime('%H:%M')
                dstring = now.strftime('%A,%B%d,%Y')
                f.writelines(f'\n{name},{dtstring},{dstring},{vote}')
                print('marked')
                time.sleep(5)
    
            else:
                print("Alert fraud")
    else:
        print("button not pressed")
        
    button_state = GPIO.input(buttony)
    if(button_state == False):
        print("you voted for Y party")
        vote = ("Y")
        print(vote)
        with open('attendance.csv','r+') as f:
            print("file is opened")
            myDatalist = f.readlines()
            namelist = []
            for line in myDatalist:
                print("list is prepared")
                entry = line.split(',')
                namelist.append(entry[0])
            if name not in namelist:
                print("name not in list")
                now = datetime.now()
                dtstring = now.strftime('%H:%M')
                dstring = now.strftime('%A,%B%d,%Y')
                f.writelines(f'\n{name},{dtstring},{dstring},{vote}')
                print('marked')
                time.sleep(5)
        
            else:
                print("Alert fraud")
    else:
        print("button not pressed")

    button_state = GPIO.input(buttonz)
    if(button_state == False):
        print("you voted for Z party")
        vote = ("Z")
        print(vote)
        with open('attendance.csv','r+') as f:
            print("file is opened")
            myDatalist = f.readlines()
            namelist = []
            for line in myDatalist:
                print("list is prepared")
                entry = line.split(',')
                namelist.append(entry[0])
            if name not in namelist:
                print("name not in list")
                now = datetime.now()
                dtstring = now.strftime('%H:%M')
                dstring = now.strftime('%A,%B%d,%Y')
                f.writelines(f'\n{name},{dtstring},{dstring},{vote}')
                print('marked')
                time.sleep(5)
    
            else:
                print("Alert fraud")
    else:
        print("button not pressed")

def automatic():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer.yml')
    face_cascade_Path = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(face_cascade_Path)
    font = cv2.FONT_HERSHEY_SIMPLEX
    id = 0
    # names related to ids: The names associated to the ids: 1 for Mohamed, 2 for Jack, etc...
    names = ['None','rikwith','saiteja','venkat','chiru'] # add a name into this list
    #Video Capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)
    # Min Height and Width for the  window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                # Unknown Face
                id = "Who are you ?"
                confidence = "  {0}%".format(round(100 - confidence))
            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
            
        cv2.imshow('camera', img)
        time.sleep(1)
        # Escape to exit the webcam / program
        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break
    id_final = (id+str(".jpg"))
    print("\n [INFO] Analysing.")
    cam.release()
    cv2.destroyAllWindows()
    
    return id_final
face = automatic()
print(face)
finger = fingerprint()
print(finger)
sys.exit()

      #  if(id_final == finger_id):
       #     print("Autherized User")
          #  while True:
           #     markattendance(id)
            #    time.sleep(5)
             #   sys.exit()       
       # else:
        #    print("unAutherized user")
         #   sys.exit()
   # else:
    #    print("unAutherized user")
       # sys.exit()


while True:
    print("please give opinion")
    button_statem = GPIO.input(buttonm)
    button_statea = GPIO.input(buttona)
    button_statee = GPIO.input(buttone)
    if(button_statem == False):
        print("mannal state")
        m()
        time.sleep(5)
    else:
        print("button is not pressed")
    if(button_statea == False):
        print('Automatic operation')
        automatic()
    else:
        print("button not pressed")
    if(button_statee == False):
        print("exiting the program")
        sys.exit()
    else:
        print("button not pressed")

