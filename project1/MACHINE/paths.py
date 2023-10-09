import os
from pathlib import Path

HERE = Path(os.path.dirname(os.path.abspath("__file__")))
TEST = Path(r'C:\Users\34644\Desktop\Firts Semester\Vision and learning\Test')
# los imagenes son de aqui: https://www.kaggle.com/datasets/andrewmvd/car-plate-detection?resource=download

 

FRONTAL = TEST / 'Frontal'
LATERAL = TEST / 'Lateral'

# You need to put here your paths to the datasets
# DATASET_ARCHIVE_4 = https://www.kaggle.com/datasets/andrewmvd/car-plate-detection?resource=download
DATASET_ARCHIVE_4 = Path(r"C:\Users\34644\Desktop\Firts Semester\Vision and learning\archive (4)")

# DATASET_ARCHIVE_4 =
DATASET_ARCHIVE_5 = Path(r"C:\Users\34644\Desktop\Firts Semester\Vision and learning\archive (5)")