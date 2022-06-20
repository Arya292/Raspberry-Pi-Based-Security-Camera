#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import base64
import cv2
import numpy as np
import os
from time import sleep

i=0
 
def callback(data):
    global i
    img,label=(data.data).split("$")
    rospy.loginfo(label)
    raw=base64.b64decode(img)
    jpg=np.frombuffer(raw,dtype=np.uint8) 
    img=cv2.imdecode(jpg,flags=1)
    cv2.imshow("Face Detection",img)
    cv2.waitKey(1)
    if label=="Human Face Detected":
        cv2.imwrite(f'Detected/face{i}.jpg',img)
    i+=1
     
def receive_message():
    rospy.init_node('simple_python_subscriber', anonymous=True)
    rospy.Subscriber("message_py", String, callback)
    rospy.spin()
    cv2.destroyAllWindows()
 
if __name__ == '__main__':
    if not os.path.isdir('Detected'):
        os.mkdir('Detected')
    
    receive_message()
