import os
from pathlib import Path

HERE = Path(os.path.dirname(os.path.abspath("__file__")))
TEST = Path(r'C:\Users\34644\Desktop\Firts Semester\Vision and learning\Test')
# los imagenes son de aqui: https://www.kaggle.com/datasets/andrewmvd/car-plate-detection?resource=download

#CAR_IMAGES_DIR = Path(r'D:\NIL\Uni\licensplates\Test') 

FRONTAL = TEST / 'Frontal'
LATERAL = TEST / 'Lateral'

DATASET_IMG = Path(r"C:\Users\34644\Desktop\Firts Semester\Vision and learning\archive (5)")
DATASET_CARS = Path(r"C:\Users\34644\Desktop\Firts Semester\Vision and learning\archive (4)")

