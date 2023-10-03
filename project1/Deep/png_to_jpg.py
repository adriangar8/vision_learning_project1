from PIL import Image
import os

# Path to the folder containing your PNG images
input_folder = r"C:\Users\xavim\Desktop\Uni\3er\1\Vision\License_plates\Dataset\VOCdevkit\VOC2012\PEGImages"

# Path where the new JPEG images will be saved
output_folder = r"C:\Users\xavim\Desktop\Uni\3er\1\Vision\License_plates\Dataset\VOCdevkit\VOC2012\JPEGImages"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate over all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        # Open an image file
        img = Image.open(os.path.join(input_folder, filename)).convert("RGB")
        
        # Save it as a JPEG in the output folder
        img.save(os.path.join(output_folder, filename[:-4] + ".jpg"))