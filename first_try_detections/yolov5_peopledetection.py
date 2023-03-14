import torch
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Model - we will use yolov5s
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# Image
img = plt.imread("/imatge/miriam.elbaz/Downloads/bikebi.jpg")
# Inference
results = model(img) # pass the image through our model

#return the predictions as a pandas dataframe
pdRes = results.pandas().xyxy[0]

#filter predictions
filtro = pdRes['class'] == 0
people = pdRes[filtro]

#save predictions
file1 = open("peopledetection_out_bikebi.txt", "w") 
file1.write("%s = %s\n" %("results", people))
file1.close()


#o en Terminal: 
#Interference on test images 
#!python detect.py --img 480 --conf 0.2 --classes 0 --source '/content/drive/MyDrive/Colab Notebooks/YOLO v5/Paseo_del_Prado_(Madrid)_01.jpg'
