'''

   Raspberry Pie Application 'Gongs_pi.py'
   
   2020.12.30
   
   Seung-hyuk Yoo
   
'''

import RPi.GPIO as GPIO
import time
import cv2
import sys

df_time = 2   # Default delay time
chk_pin1 = 22 # GPIO Pin No.

def mouse_callback(event, x, y, flags, param):  # Mouse Event Handling
    global df_time
    if flags == 1:  # Click Left Button
        if x < 60 and y > 420:   # UpLeft = Decrease Default Time
            if df_time > 1:
                df_time -= 1
                #print("Decrease :",df_time)
        if x < 60 and y < 60:  # UpRight = Increase Default Time
            if df_time < 10:
                df_time += 1
                #print("Increase :",df_time)
        if x > 420 and y < 60: # DnRight = Exit Program
            cv2.destroyAllWindows()
            sys.exit()
        disp_time()    

def disp_time():
    global df_time
    #print("Push","/home/pi/Gongs/Numeric/%02d" % df_time + ".jpg")
    Img9 = cv2.imread("/home/pi/Gongs/Numeric/%02d" % df_time + ".jpg") # Display Time Bar
    cv2.namedWindow('vol', cv2.WINDOW_AUTOSIZE)
    cv2.moveWindow('vol', 80, 30)
    cv2.imshow('vol', Img9)
    for i in range(500):
        cv2.waitKey(1)
    cv2.destroyWindow('vol')
    time.sleep(1)
    

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(chk_pin1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# Init Screen
Img1 = cv2.imread('/home/pi/Gongs/screen01.jpg')
Img2 = cv2.imread('/home/pi/Gongs/screen02.jpg')

cv2.namedWindow('original', cv2.WINDOW_NORMAL)          
cv2.setWindowProperty('original', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.setMouseCallback('original', mouse_callback)
cv2.imshow('original', Img1)

Img0 = Img1 # Display Image
chk  = 0

while True:
    cv2.imshow('original', Img0)
    cv2.waitKey(1)

    if chk != 0 and int(time.time()) <= (now + df_time):  # Check GPIO & Delay
        continue

    chk = GPIO.input(chk_pin1)   # Check GPIO Pin  

    Img0 = Img1    

    if chk != 0:        
        Img0 = Img2
        now  = int(time.time())
 
 
#cv2.destroyAllWindows()
