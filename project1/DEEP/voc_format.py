import random
import os

# Generate the list of image IDs
number_files = len(os.listdir(r'C:\Users\34644\Desktop\Firts Semester\Vision and learning\archive (4)\VOCdevkit\VOC2012\ImageSets')) - 1
image_ids = [f"Cars{i}" for i in range(number_files)]  # Assuming the images range from Cars0.png to Cars429.png

# Shuffle the list
random.shuffle(image_ids)

# Calculate the number of images to use for training (80%)
num_train = int(0.8 * len(image_ids))

# Split into training and validation sets
train_ids = image_ids[:num_train]
val_ids = image_ids[num_train:]

# Write to train.txt
with open(r'C:\Users\34644\Desktop\Firts Semester\Vision and learning\archive (4)\VOCdevkit\VOC2012\ImageSets\Main\train.txt', "w") as f:
    for id in train_ids:
        f.write(f"{id}\n")

# Write to val.txt
with open(r'C:\Users\34644\Desktop\Firts Semester\Vision and learning\archive (4)\VOCdevkit\VOC2012\ImageSets\Main\val.txt', "w") as f:
    for id in val_ids:
        f.write(f"{id}\n")