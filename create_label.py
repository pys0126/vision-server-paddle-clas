"""
构造label.txt
"""
import os

BASE_DIR = "./gallery"
label_txt_path = os.path.join(BASE_DIR, "label.txt")

classes = ["是正方体", "不是正方体"]
labels = []
for label in os.listdir(BASE_DIR):
    if os.path.isdir(os.path.join(BASE_DIR, label)):
        labels.append(label)

labels.sort()
with open(label_txt_path, "w", encoding="u8") as f:
    for label in labels:
        label_dir = os.path.join(BASE_DIR, label)
        for image in os.listdir(label_dir):
            f.write(os.path.join(label, image) + f"\t{classes[labels.index(label)]}\n")
            print(image)
