import os
from pathlib import Path

HERE = Path(os.path.dirname(os.path.abspath("__file__")))
TEST = Path(r'D:\NIL\Uni\licensplates\Test')
# los imagenes son de aqui: https://www.kaggle.com/datasets/andrewmvd/car-plate-detection?resource=download

#CAR_IMAGES_DIR = Path(r'D:\NIL\Uni\licensplates\Test') 

FRONTAL = TEST / 'Frontal'
LATERAL = TEST / 'Lateral'

DATASET_IMG = Path(r"D:\NIL\Uni\licensplates\images")
