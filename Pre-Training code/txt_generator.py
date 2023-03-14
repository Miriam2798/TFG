
#Considerar pandas dataframe y os.path. /Tendre que guardar las imagenes originales. 
import pandas as pd
import os.path 
import numpy as np
import cv2

#Abrir archivo imglist.txt y leer linia a linia. 
df = pd.read_csv("/imatge/miriam.elbaz/workspace/Pre-Training code/imglist.txt", sep ="/", names = ["Tag", "Images", "Name"])
#df = pd.DataFrame(dataframe) No cal. 

#Buscar el track correspondiente(nombre video)
#Get video name, frame and ID from dataset. Later we will have to generalize

#Definitions
#Image size:
height_img = 1920
width_img = 1080

n = 19 #Number of video name chars
nframe = 4 #frame location 
nid = 6 #id location

tags = list(df["Tag"])

for row_ind in range(len(df["Tag"])):
	name = np.array(df.iloc[[row_ind]]['Name'])
	vid = name[0][0:n]
	frame = int(name[0].split("_")[nframe])
	ID = int(str(name[0].split("_")[nid]).replace(".jpg", ""))
	#Tag:
	tag = tags[row_ind]

	if tag == 'Bike': 
		ntag = "0"
	elif tag == 'E-scooter':
		ntag = "1"
	else: 
		ntag = "2" #Pedestrian
		
	#With pandas dataframe. Buscar el frame y el ID en el txt del track
	track = pd.read_csv("/imatge/miriam.elbaz/workspace/Tracks/" + vid + ".txt",index_col= False, sep =" ",  names = ["Frame", "ID", "bb_left", "bb_top", "bb_width", "bb_height", "x", "y", "z", "0"])
	trackdf = pd.DataFrame(track)
	#print(len(trackdf))

	for i in range(len(trackdf)):
		if(int(trackdf.iloc[i]["Frame"]) == frame) and (int(trackdf.iloc[i]["ID"]) == ID):
			bb_left = float(trackdf.iloc[i]["bb_left"])/width_img
			bb_top = float(trackdf.iloc[i]["bb_top"])/height_img
			bb_width = float(trackdf.iloc[i]["bb_width"])/width_img
			bb_height = float(trackdf.iloc[i]["bb_height"])/height_img
			x_center = bb_left + (bb_width/2) 
			y_center = bb_top + (bb_height/2)
		
	#Escribir en un txt etiqueta, bbxes. SI hay mas de 1 detecion en un frame se escriben varias linias. Guardar txt como vid_frame
	#Mirar si un frame esta repetido:	
	if os.path.isfile('/imatge/miriam.elbaz/workspace/Dataset/labels/' + str(vid) + '_frame_' + str(frame) + '.txt'): #Si el archivo existe: fopen con la 'a' (append en lugar de write)
		f = open('/imatge/miriam.elbaz/workspace/Dataset/labels/' + str(vid) + '_frame_' + str(frame) + '.txt', 'a')
	else:
		f = open('/imatge/miriam.elbaz/workspace/Dataset/labels/' + str(vid) + '_frame_' + str(frame) + '.txt', 'w')

	f.write(ntag + " " + str(x_center) + " " + str(y_center) + " " + str(bb_width) + " " + str(bb_height) +"\n") #Escribimos
	f.close()

