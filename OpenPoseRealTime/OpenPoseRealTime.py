# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 18:55:13 2019

@author: admin
"""

import cv2
import time
import numpy as np
from dataPath import DATA_PATH


# Load a Caffe Model
protoFile = r"C:\Users\admin\Desktop\Opencv Course\Week10\week10-python\models" +"\mpi.prototxt"
weightsFile = r"C:\Users\admin\Desktop\Opencv Course\Week10\week10-python\models" +"\pose_iter_160000.caffemodel"
filename = DATA_PATH + "images/man.jpg"
# Specify number of points in the model
nPoints = 15
POSE_PAIRS = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ]
net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

cap=cv2.VideoCapture('meeting.mp4')
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
outmp4 = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc(*'XVID'), 10, (frame_width,frame_height))
while True:
    # Read Image
    ret, frame = cap.read()
    if ret == True:
        im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        inWidth = im.shape[1]
        inHeight = im.shape[0]
        
        
        # Convert image to blob
        netInputSize = (368, 368)
        inpBlob = cv2.dnn.blobFromImage(im, 1.0 / 255, netInputSize, (0, 0, 0), swapRB=True, crop=False)
        net.setInput(inpBlob)
        
        
        # Run Inference (forward pass)
        output = net.forward()
        
        # Extract points
        
        # X and Y Scale
        scaleX = float(inWidth) / output.shape[3]
        scaleY = float(inHeight) / output.shape[2]
        
        # Empty list to store the detected keypoints
        points = []
        
        # Confidence treshold
        threshold = 0.1
        
        for i in range(nPoints):
            # Obtain probability map
            probMap = output[0, i, :, :]
        
            # Find global maxima of the probMap.
            minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
        
            # Scale the point to fit on the original image
            x = scaleX * point[0]
            y = scaleY * point[1]
        
            if prob > threshold :
                # Add the point to the list if the probability is greater than the threshold
                points.append((int(x), int(y)))
            else :
                points.append(None)
        
        
        # Display Points & Skeleton
        
        imPoints = im.copy()
        imSkeleton = im.copy()
        # Draw points
        for i, p in enumerate(points):
            cv2.circle(frame, p, 8, (255, 255,0), thickness=-1, lineType=cv2.FILLED)
            cv2.putText(frame, "{}".format(i), p, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, lineType=cv2.LINE_AA)
        
        # Draw skeleton
        for pair in POSE_PAIRS:
            partA = pair[0]
            partB = pair[1]
        
            if points[partA] and points[partB]:
                cv2.line(frame, points[partA], points[partB], (255, 255,0), 2)
                cv2.circle(frame, points[partA], 8, (255, 0, 0), thickness=-1, lineType=cv2.FILLED)
        outmp4.write(frame)
        
        cv2.imshow("Keypoints", frame)
        if cv2.waitKey(10) == ord('q'):#wait until 'q' key is pressed
            break
    else:
        break

cap.release()
outmp4.release()
cv2.destroyAllWindows()

