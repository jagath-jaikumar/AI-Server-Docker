from torchvision import models, transforms
import torch
from image_encoder.image_encoder import decode
import json
import requests

alexnet = models.alexnet(pretrained=True)
alexnet.eval()

classes = []
with open('imagenet_classes.txt') as f:
    classes = [line.strip() for line in f.readlines()]


transform = transforms.Compose([
 transforms.Resize(256),
 transforms.CenterCrop(224),
 transforms.ToTensor(),
 transforms.Normalize(
 mean=[0.485, 0.456, 0.406],
 std=[0.229, 0.224, 0.225]
 )])



def predict(fpath):
    data = {}
    with open(fpath) as json_file:
        data = json.load(json_file)
    img = decode(data["image"])
    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t, 0)
    out = alexnet(batch_t)
    _, indices = torch.sort(out, descending=True)
    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100

    output = {}
    for idx in indices[0][:5]:
        output[classes[idx]] = percentage[idx].item()

    print(output)

    to_send = {"fpath":fpath, "result":{"object_detetction_results":output}}
    requests.post('http://imagedb:5000/append',json = to_send)

    return to_send



################ pika
from pika_listener import QueueListener

Q = QueueListener(predict)

if __name__ == "__main__":
    Q.run()
