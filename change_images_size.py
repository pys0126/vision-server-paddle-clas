"""
改变图片大小
"""
import os
import cv2
import fire


def get_images(images_dir: list[str], base_dir: str):
    image_list = []
    for image in images_dir:
        if image.split(".")[-1] not in ["png", "jpg", "jpeg"]:
            continue
        image_path = os.path.join(base_dir, image)
        image_list.append(image_path)
    return image_list


def resize_images_dir(images: list[str], target_size: list[int]):
    for image in images:
        mat = cv2.imread(image)
        resized = cv2.resize(mat, target_size)
        cv2.imwrite(image, resized)


def resize_image(image: str, target_size: list[int]):
    mat = cv2.imread(image)
    resized = cv2.resize(mat, target_size)
    cv2.imwrite(image, resized)


def run(base_dir_or_image: str, target_size: list[int], is_dir: bool):
    if is_dir:
        images_dir = os.listdir(base_dir_or_image)
        resize_images_dir(get_images(images_dir, base_dir_or_image), target_size)
    else:
        resize_image(base_dir_or_image, target_size)


if __name__ == "__main__":
    fire.Fire(run)
