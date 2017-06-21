import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
os.chdir('/home/mukesh-deo/Downloads')

cap=cv2.VideoCapture('Dash Cam - Car pool lane.mp4')
def draw_line(img,lines):
    try:
        i=1
        for line in lines:
            for i in range(0,len(line)):
                       
                coord=line[i]
                
                cv2.line(img,(coord[0],coord[1]),(coord[2],coord[3]),[255,255,255],3)
    except:
        pass
def process_img(p_img):
    
    
    p_img=cv2.cvtColor(p_img,cv2.COLOR_BGR2GRAY)
    p_img=cv2.Canny(p_img,threshold1=100,threshold2=120)
    p_img=cv2.GaussianBlur(p_img,(3,3),0)
    lines=cv2.HoughLinesP(p_img,1,np.pi/180,180,np.array([]),18,15)
    draw_line(p_img,lines)
    return p_img    

while True:
    ret,frame = cap.read()
    p_img=process_img(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('edge',p_img)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break

cap.release()
cv2.waitKey(0)& 0xFF == ord('q')
cv2.destroyAllWindows()

