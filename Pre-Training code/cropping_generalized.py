import numpy as np
import cv2

#Open the file, read the first line, close the file
video_name = '/imatge/miriam.elbaz/workspace/Yolov5_StrongSORT_OSNet/barcelona_videos/BikeBi/VID_20220427_151533.mp4'
f = open('/imatge/miriam.elbaz/workspace/Yolov5_StrongSORT_OSNet/runs/track/exp9/tracks/VID_20220427_151533.txt', 'r')
lines = f.readlines()
f.close()

for line in lines:
	i = 0
	n = line.split(" ")
	#Extract the frame number
	frame_no = int(n[i])

	#Get the video frame
	cap = cv2.VideoCapture(video_name)
	cap.set(1,(frame_no-1)) 
	ret, frame = cap.read()  #Read the frame; Grabs, decodes and returns the next video frame.
	
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
	
	ima = frame[tly:(bry+1),tlx:(brx+1)]

	#save cropped image
	cv2.imwrite('/imatge/miriam.elbaz/workspace/cropped/VID_20220427_151533_frame_' + str(frame_no) + '_ID_' + str(ID) +'.jpg', ima)
