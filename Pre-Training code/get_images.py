import numpy as np
import cv2
import pandas as pd

#Abrir los videos seleccionados, coger los frames que contienen deteccion y guardar los frames en la carpeta dataset/images


#Abrir archivo framelist.txt y leer linia a linia. 
df = pd.read_csv("/imatge/miriam.elbaz/workspace/Pre-Training code/framelist.txt", sep ="/", names = ["dataset", "labels", "Name"])
#df = pd.DataFrame(dataframe) no cal

n = 19 #Number of video name chars
nframe = 4 #frame location 


for row_ind in range(len(df["dataset"])):
	name = np.array(df.iloc[[row_ind]]['Name'])
	vid = name[0][0:n]
	frame_no = int(name[0].split("_")[nframe].replace(".txt", ""))
	
	video_name = '/imatge/miriam.elbaz/workspace/Yolov5_StrongSORT_OSNet/barcelona_videos/BikeBi/' + vid + '.mp4'
	
	#Get the video frame
	cap = cv2.VideoCapture(video_name)
	cap.set(1,(frame_no - 1)) 
	ret, frame = cap.read()  #Read the frame; Grabs, decodes and returns the next video frame.
	
	cv2.imwrite('/imatge/miriam.elbaz/workspace/Dataset/images/'+ vid + '_frame_' + str(frame_no) + '.jpg', frame)
	
