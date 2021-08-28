from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .main import *
from .models import Prediction
from .forms import PredictionForm
from django.conf import settings

import os
import shutil


class IndexView(TemplateView):
    template_name = "index.html"


class PredictionView(FormView):
    template_name = "prediction.html"
    form_class = PredictionForm

    def post(self, request, *args, **kwargs):
        form = PredictionForm(request.POST)

        # 前回の画像をディレクトリごと消して更新
        shutil.rmtree("media")
        os.mkdir("media")
        predict = Prediction()
        predict.image = request.FILES.get("image")
        predict.save()

        input_img = Prediction.objects.order_by("-id").all()[0]
        input_img_path = str(settings.BASE_DIR)+input_img.image.url
        output_img = detect(input_img_path)
        params = {
            "form": self.form_class,
            "input_img": input_img,
            "output_img": output_img,
        }

        return render(request, self.template_name, params)


class ProcessingView(FormView):
    template_name = "processing.html"
    form_class = PredictionForm

    def post(self, request, *args, **kwargs):
        form = PredictionForm(request.POST)

        # 前回の画像をディレクトリごと消して更新
        shutil.rmtree("media")
        os.mkdir("media")
        predict = Prediction()
        predict.image = request.FILES.get("image")
        predict.save()

        input_img = Prediction.objects.order_by("-id").all()[0]
        input_img_path = str(settings.BASE_DIR)+input_img.image.url
        output_img = gray(input_img_path)
        params = {
            "form": self.form_class,
            "input_img": input_img,
            "output_img": output_img,
        }

        return render(request, self.template_name, params)