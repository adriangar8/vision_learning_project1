import torch
from torchvision import datasets, transforms

def get_dataloader(dataset_path):
    voc_dataset = datasets.VOCDetection(root=dataset_path, image_set='train', download=False)

    transform = transforms.Compose([transforms.Resize((224, 224)),
                                    transforms.ToTensor()])

    dataloader = torch.utils.data.DataLoader(voc_dataset, batch_size=32, shuffle=True, transform = transform)
    
    return dataloader