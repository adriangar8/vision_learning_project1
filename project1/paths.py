import os
from pathlib import Path

HERE = Path(os.path.dirname(os.path.abspath("__file__")))
TEST = Path(r"C:\Users\34644\Desktop\Firts Semester\Vision and learning\Test")
# los imagenes son de aqui: https://www.kaggle.com/datasets/andrewmvd/car-plate-detection?resource=download

CAR_IMAGES_DIR = Path(r'C:\Users\34644\Desktop\Firts Semester\Vision and learning\archive (4)\images') 

DATASET = Path(r"C:\Users\34644\Desktop\Firts Semester\Vision and learning\archive (5)")


FRONTAL = TEST / 'Frontal'
LATERAL = TEST / 'Lateral'

DATASET_IMG = DATASET / "images"