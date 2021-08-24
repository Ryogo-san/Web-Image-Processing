import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

import numpy as np
import os, json, cv2, random
import warnings
warnings.filterwarnings("ignore")

from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog

from django.conf import settings


def detect(img):
    """
    img: path of input image
    """
    input_img=cv2.imread(img)
    cfg=get_cfg()
    cfg.MODEL.DEVICE="cpu"
    cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"))
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST=0.5
    cfg.MODEL.WEIGHTS=model_zoo.get_checkpoint_url("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml")
    predictor=DefaultPredictor(cfg)
    outputs=predictor(input_img) # predict

    # visualize (create image)
    v=Visualizer(input_img[:,:,::-1],MetadataCatalog.get(cfg.DATASETS.TRAIN[0]),scale=1.2)
    out=v.draw_instance_predictions(outputs["instances"].to("cpu"))
    result_img=out.get_image()[:,:,::-1]
    output="/media/result.png"
    # save and return
    cv2.imwrite("media/result.png",result_img)
    return output


def gray(img):
    input_img=cv2.imread(img)
    out=cv2.cvtColor(input_img,cv2.COLOR_BGR2GRAY)
    output="media/gray.png"
    cv2.imwrite(output,out)
    return output
