import os
from pathlib import Path

HERE = Path(os.path.dirname(os.path.abspath("__file__")))

TEST = Path(r'C:\Users\xavim\Desktop\License_plates\test_images\Test\Test')
# los imagenes son de aqui: https://www.kaggle.com/datasets/andrewmvd/car-plate-detection?resource=download


FRONTAL = TEST / 'Frontal\Frontal'
LATERAL = TEST / 'Lateral\Lateral'

DATASET_IMG = Path(r"C:\Users\xavim\Desktop\Datos_vision\archive (5)")
DATASET_CARS = Path(r"C:\Users\xavim\Desktop\Datos_vision\archive (4)")





