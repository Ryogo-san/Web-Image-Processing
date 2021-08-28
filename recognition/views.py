from django.shortcuts import render
from django.views.generic import TemplateView
from .main import *
from .models import Prediction
from .forms import PredictionForm
from .operationView import OperationView


class IndexView(TemplateView):
    template_name = "index.html"


class PredictionView(OperationView):
    template_name = "prediction.html"
    form_class = PredictionForm

    def post(self, request, *args, **kwargs):
        form = PredictionForm(request.POST)

        super().upload(request, Prediction)
        input_img, input_img_path = super().before_operation(Prediction)

        output_img = detect(input_img_path)
        params = {
            "form": self.form_class,
            "input_img": input_img,
            "output_img": output_img,
        }

        return render(request, self.template_name, params)


class ProcessingView(OperationView):
    template_name = "processing.html"
    form_class = PredictionForm

    def post(self, request, *args, **kwargs):
        form = PredictionForm(request.POST)

        super().upload(request, Prediction)
        input_img, input_img_path = super().before_operation(Prediction)

        output_img = gray(input_img_path)
        params = {
            "form": self.form_class,
            "input_img": input_img,
            "output_img": output_img,
        }

        return render(request, self.template_name, params)
