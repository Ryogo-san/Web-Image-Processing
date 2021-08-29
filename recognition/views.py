from django.shortcuts import render
from django.views.generic import TemplateView
from .main import *
from .models import InputImage
from .forms import InputImageForm
from .operation_view import OperationView

from detectron2.config import get_cfg
from detectron2 import model_zoo


class IndexView(TemplateView):
    template_name = "index.html"


class PredictionView(OperationView):
    template_name = "prediction.html"
    form_class = InputImageForm

    cfg = get_cfg()
    cfg.MODEL.DEVICE = "cpu"
    cfg.merge_from_file(model_zoo.get_config_file(
        "COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"))
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(
        "COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml")

    def post(self, request, *args, **kwargs):
        form = InputImageForm(request.POST)

        super().upload(request, InputImage)
        input_img, input_img_path = super().before_operation(InputImage)

        output_img = detect(self.cfg, input_img_path)
        params = {
            "form": self.form_class,
            "input_img": input_img,
            "output_img": output_img,
        }

        return render(request, self.template_name, params)


class ProcessingView(OperationView):
    template_name = "processing.html"
    form_class = InputImageForm

    def post(self, request, *args, **kwargs):
        form = InputImageForm(request.POST)

        super().upload(request, InputImage)
        input_img, input_img_path = super().before_operation(InputImage)

        output_img = gray(input_img_path)
        params = {
            "form": self.form_class,
            "input_img": input_img,
            "output_img": output_img,
        }

        return render(request, self.template_name, params)
