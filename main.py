import numpy as np
import cv2
#import threading

try:
    import winsound
except ImportError:
    import os
    def playsound(frequency,duration):
        
        os.system('beep -f %s -l %s' % (frequency,duration))
else:
    def playsound(frequency,duration):
        winsound.Beep(frequency,duration)
        
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def beep():
  for i in range(4):
    winsound.Beep(1500, 250)

cam = cv2.VideoCapture(0)
count = 0                
iters = 0                
while(True):             
      ret, cur = cam.read()
      gray = cv2.cvtColor(cur, cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors=1, minSize=(10,10))
      for (x,y,w,h) in faces:
      	#cv2.rectangle(cur,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = cur[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) == 0:
          print ("Eyes closed")
        else:
          print ("Eyes open")
        count += len(eyes)
        iters += 1
        if iters == 2:
          iters = 0
          if count == 0:
            print ("Drowsiness Detected!!!")
            #thread.start_new_thread(beep,())
          count = 0
        for (ex,ey,ew,eh) in eyes:
        	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh), (0,255,0),2)
      cv2.imshow('frame', cur)
      if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

