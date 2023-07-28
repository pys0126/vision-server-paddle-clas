import paddleclas
import fire


def start(gallery_image_root: str = "./mydata/gallery",
          model_name: str = "PP-ShiTuV2",
          index_dir: str = "./mydata/index",
          gallery_data_file: str = "./mydata/gallery/label.txt"):
    """
    构造索引
    :param gallery_image_root: gallery目录
    :param model_name: 模型名称
    :param index_dir: index目录
    :param gallery_data_file: label.txt路径
    :return:
    """
    paddleclas.PaddleClas(build_gallery=True, model_name=model_name, gallery_image_root=gallery_image_root,
                          index_dir=index_dir, gallery_data_file=gallery_data_file)


if __name__ == "__main__":
    fire.Fire(start)
