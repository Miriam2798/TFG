
#wandb
import wandb
import os

wandb.init(project="train-project", entity="tfg-imatge")

wandb.config = { #modificar quizas
  "learning_rate": 0.002,
  "epochs": 150,
  "batch_size": 24
}

#wandb.log({"loss": loss}) 

# Optional
#wandb.watch(model)

#os.system poner la comanda de entrenamiento. Nota: Workers parameter es cpu cores used per gpu
os.system("python yolov5/train.py --img 640 --cfg yolov5l.yaml --hyp hyp.scratch-med.yaml --batch 24 --epochs 150 --data people_data.yaml --weights yolov5m.pt --workers 4 --name people_det")

wandb.finish()
