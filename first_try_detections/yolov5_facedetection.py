from retinaface import RetinaFace
import numpy as np

resp = RetinaFace.detect_faces("/imatge/miriam.elbaz/Downloads/bikebi.jpg")
#np.savetxt('face_detection_out.txt',np.array(resp))

file1 = open("face_detection_out_bikebi.txt", "w") 
file1.write("%s = %s\n" %("resp", resp))
file1.close()
