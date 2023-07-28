"""
改变目录下所有图片为png格式
"""
import fire
import os


def start(images_path: str = "./mydata/images"):
    if not os.path.exists(images_path):
        raise FileNotFoundError(f"`{images_path}`不存在！")
    for image in os.listdir(images_path):
        image_path = os.path.join(images_path, image)
        print(f"mv {image_path} .{''.join(image_path.split('.')[:-1]) + '.png'}")
        os.system(f"mv {image_path} .{''.join(image_path.split('.')[:-1]) + '.png'}")


if __name__ == "__main__":
    fire.Fire(start)
