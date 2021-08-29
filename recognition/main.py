import cv2
from detectron2.data import MetadataCatalog
from detectron2.utils.visualizer import Visualizer
from detectron2.engine import DefaultPredictor
import warnings
import numpy as np

from detectron2.utils.logger import setup_logger
setup_logger()

warnings.filterwarnings("ignore")


def detect(cfg, img):
    """
    入力画像に対して物体検出を行う

    Input:
        cfg : config
        img (str): アップロードされた画像の相対パス

    Output:
        output (str): 検出後の画像の相対パス
    """
    input_img = cv2.imread(img)

    predictor = DefaultPredictor(cfg)
    
    import time
    start=time.time()
    outputs = predictor(input_img)
    print("prediction time: ",time.time()-start)
    # visualize (create image)
    start2=time.time()
    v = Visualizer(
        input_img[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
    del cfg,predictor
    out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
    result_img = out.get_image()[:, :, ::-1]
    output = "/media/result.png"
    print("result time: ",time.time()-start2)
    # save and return
    cv2.imwrite("media/result.png", result_img)
    del v,result_img,out
    return output


def gray(img):
    input_img = cv2.imread(img)
    out = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
    output = "media/gray.png"
    cv2.imwrite(output, out)
    return output
