import numpy as np
import cv2

#Open the file, read the first line, close the file
f = open('/imatge/miriam.elbaz/workspace/Yolov5_StrongSORT_OSNet/runs/track/exp9/tracks/VID_20220427_151533.txt', 'r')
m = f.readline()
f.close()

#Data and initializations
n = m.split(" ")
i = 0
video_name = '/imatge/miriam.elbaz/workspace/Yolov5_StrongSORT_OSNet/barcelona_videos/BikeBi/VID_20220427_151533.mp4'

#Extract the frame number
frame_no = int(n[i])

#Get the video frame
cap = cv2.VideoCapture(video_name)
cap.set(1,frame_no) 
ret, frame = cap.read()  #Read the frame
cv2.imwrite('/imatge/miriam.elbaz/workspace/frame.jpg', frame) #Save

#ID
ID = n[i+1] 

#Crop the frame 
#File format: bb_left, bb_top, bb_width, bb_height

bb_left = int(n[i+2])
bb_top = int(n[i+3])
bb_width = int(n[i+4])
bb_height = int(n[i+5])

tly = bb_top
bry = bb_top + bb_height
tlx = bb_left
brx = bb_left + bb_width

ima = frame[tly:bry,tlx:brx]

#save cropped image
cv2.imwrite('/imatge/miriam.elbaz/workspace/cropped.jpg', ima)

#generalizar para todos los frames --> como guardar con numero de frame o id o both
#generalizar para todos los videos
#etiquetar


