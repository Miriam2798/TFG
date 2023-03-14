#Considerar pandas dataframe y os.path. /Tendre que guardar las imagenes originales. 
import pandas as pd
import os.path 
import numpy as np
import cv2

#Abrir archivo imglist.txt y leer linia a linia. 
df = pd.read_csv("imglist.txt", index_col = None, sep ="/", names = ["Tag", "Images", "Name"])
#df = pd.DataFrame(dataframe, columns = ["Tag", "Images", "Name"], index = None)

#Buscar el track correspondiente(nombre video)
#Get video name, frame and ID from dataset. Later we will have to generalize

#Definitions
#Image size:
height_img = 1920
width_img = 1080

n = 19 #Number of video name chars
nframe = 4 #frame location 
nid = 6 #id location

#df.reset_index(drop=True, inplace=True)
#tag = str(df.iloc[[0]]['Tag'])

tags = list(df["Tag"])
tag = tags[0]
print(tag)

#print(df.head())
#print(tag)
