
import os.path
from sklearn.model_selection import train_test_split
import shutil
import os 

images = [os.path.join('/imatge/miriam.elbaz/workspace/Dataset/images/', x) for x in os.listdir('/imatge/miriam.elbaz/workspace/Dataset/images/')]
labels = [os.path.join('/imatge/miriam.elbaz/workspace/Dataset/labels/', x) for x in os.listdir('/imatge/miriam.elbaz/workspace/Dataset/labels/') if x[-3:] == "txt"]

images.sort()
labels.sort()

#Split the dataset in train-val-test

train_img, val_img, train_lbl, val_lbl = train_test_split(images, labels, test_size = 0.2, random_state = 1)
val_img, test_img, val_lbl, test_lbl = train_test_split(val_img, val_lbl, test_size = 0.5, random_state = 1)

os.system("mkdir /imatge/miriam.elbaz/workspace/Dataset/images/train")
os.system("mkdir /imatge/miriam.elbaz/workspace/Dataset/images/val")
os.system("mkdir /imatge/miriam.elbaz/workspace/Dataset/images/test")
os.system("mkdir /imatge/miriam.elbaz/workspace/Dataset/labels/train") 
os.system("mkdir /imatge/miriam.elbaz/workspace/Dataset/labels/val") 
os.system("mkdir /imatge/miriam.elbaz/workspace/Dataset/labels/test")

def move_files(list_files, dest_folder):
	for f in list_files: 
		try: 
			shutil.move(f, dest_folder)
		except: 
			print(f)
			assert False


move_files(train_img, '/imatge/miriam.elbaz/workspace/Dataset/images/train')
move_files(val_img, '/imatge/miriam.elbaz/workspace/Dataset/images/val')
move_files(test_img, '/imatge/miriam.elbaz/workspace/Dataset/images/test')
move_files(train_lbl, '/imatge/miriam.elbaz/workspace/Dataset/labels/train')
move_files(val_lbl, '/imatge/miriam.elbaz/workspace/Dataset/labels/val')
move_files(test_lbl, '/imatge/miriam.elbaz/workspace/Dataset/labels/test')

