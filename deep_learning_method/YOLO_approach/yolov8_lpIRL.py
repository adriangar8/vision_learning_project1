from ultralytics import YOLO

# load pretrained YOLOv5 model
model = YOLO('YOLOv8_ANPR50.pt')

# run inference on the source
results = model(source=0, show=True, conf=0.4, save=True) # generator of results
