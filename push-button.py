import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
import os
import pandas as pd
import time
import datetime
from datetime import datetime
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
while True:
    print("please give opinion")
    button_statem = GPIO.input(buttonm)
    buton_statea = GPIO.input(buttona)
    if(button_statem == False):
        print("mannal state")
    else:
        print("button is not pressed")
    if(button_statea == False):
        print('Automatic operation')
    else:
        print("Automatic operation")
    if(button_statee == False):
        print("exit the program")
    else:
        print("button not pressed")
    


                
def mannual_option():
    name = ("chirunjeevi")
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
        
    
        