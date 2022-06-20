#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import numpy as np
import cv2
from matplotlib import pyplot as plt
from picamera.array import PiRGBArray 
from picamera import PiCamera
import base64
from time import sleep

 
def publish_message():
    pub = rospy.Publisher('message_py', String, queue_size=10)
    rospy.init_node('simple_python_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    cap = cv2.VideoCapture(0)
    while not rospy.is_shutdown():
        face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
        ret, frame = cap.read()
        img = frame
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        if faces == ():
            hello_str = "Human Face Not Detected" 
            
        else:
            hello_str = "Human Face Detected"
            
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h,x:x+w]

        _,s=cv2.imencode('.jpg',img)#image to string , t or f  
        s=base64.b64encode(s).decode()# 
        pub.publish(s+"$"+hello_str)   
        rospy.loginfo(hello_str)
        
        rate.sleep()
    cap.release()
 
if __name__ == '__main__':
    try:
        publish_message()
    except rospy.ROSInterruptException:
        pass
