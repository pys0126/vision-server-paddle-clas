"""
通用主体识别
"""
from pprint import pprint
import change_images_size
import paddleclas
import fire


def start(model_name: str = "PP-ShiTuV2",
          index_dir: str = "./index_library/cube/index",
          input_data: str = "./predict-images/cube/no-one.png") -> dict:
    """
    单个图片识别
    :param model_name: 模型名称
    :param index_dir: index索引目录
    :param input_data: 待识别图像
    :return: 识别结果Dict
    """
    image_size = [181, 181]
    change_images_size.run(base_dir_or_image=input_data, target_size=image_size, is_dir=False)            
    model = paddleclas.PaddleClas(model_name=model_name, index_dir=index_dir)
    return next(model.predict_shitu(input_data=input_data))[0]


if __name__ == "__main__":
    result = fire.Fire(start)
    pprint(result)
